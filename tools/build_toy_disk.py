#!/usr/bin/env python3
"""Build an HFS disk with the original Macintosh Daft Punk sequencer.
Requires unar and hfsutils. Preserve the Macintosh data and resource forks.
"""
import binascii
from pathlib import Path
import struct
import subprocess
import sys
import tempfile

root=Path(sys.argv[1] if len(sys.argv)>1 else "public").resolve()
source=root/"daftpunk.sit.hqx"
target=root/"daft-punk-toy.img"

def run(*args):
    print("+", " ".join(map(str,args)),flush=True)
    subprocess.run([str(x) for x in args],check=True)

def apple_double(path):
    if not path.is_file(): return b"",None
    blob=path.read_bytes()
    if len(blob)<26 or struct.unpack_from(">I",blob)[0]!=0x00051607:
        raise ValueError("Invalid AppleDouble resource fork: "+str(path))
    count=struct.unpack_from(">H",blob,24)[0]
    parts={}
    for i in range(count):
        kind,offset,size=struct.unpack_from(">III",blob,26+i*12)
        if offset+size>len(blob): raise ValueError("Bad AppleDouble fork bounds")
        parts[kind]=blob[offset:offset+size]
    return parts.get(2,b""),parts.get(9)

def as_macbinary(name,data,rsrc,kind,creator):
    nb=name.encode("mac_roman")
    if not 1<=len(nb)<=63: raise ValueError("Bad Mac file name")
    h=bytearray(128)
    h[1]=len(nb)
    h[2:2+len(nb)]=nb
    h[65:69]=kind
    h[69:73]=creator
    struct.pack_into(">I",h,83,len(data))
    struct.pack_into(">I",h,87,len(rsrc))
    struct.pack_into(">H",h,124,binascii.crc_hqx(h[:124],0))
    def pad(b):return b+b"\0"*((-len(b))%128)
    return bytes(h)+pad(data)+pad(rsrc)

if not source.is_file():raise SystemExit("Missing original daftpunk.sit.hqx")
with tempfile.TemporaryDirectory() as temp:
    scratch=Path(temp)
    run("unar","-quiet","-forks","visible","-output-directory",scratch,source)
    def app_files():
        return [p for p in scratch.rglob("*") if p.is_file() and p.name.lower()=="phoenixobot.dcr"]
    candidates=app_files()
    if not candidates:
        sit_files=[p for p in scratch.rglob("*") if p.is_file() and p.suffix.lower()==".sit"]
        for p in sit_files:
            run("unar","-quiet","-forks","visible","-output-directory",scratch/"expanded",p)
        candidates=app_files()
    if not candidates:raise SystemExit("Original phoenixobot.dcr not found after extraction")
    app=candidates[0]
    companion=app.with_name("._"+app.name)
    if not companion.exists():companion=app.with_name(app.name+".rsrc")
    rsrc,finder=apple_double(companion)
    data=app.read_bytes()
    if not rsrc:raise SystemExit("Missing Mac resource fork: refusing incomplete application")
    kind,creator=(finder[:4],finder[4:8]) if finder and len(finder)>=8 else (b"APPL",b"PJ97")
    if kind!=b"APPL": raise SystemExit("Expected Macintosh application, got "+repr(kind))
    print("Original application:",app.name,"data fork",len(data),"resource fork",len(rsrc),kind,creator,flush=True)
    mb=scratch/"phoenixobot.bin"
    mb.write_bytes(as_macbinary(app.name,data,rsrc,kind,creator))
    with target.open("wb") as f:f.truncate(16*1024*1024)
    run("hformat","-l","DAFT PUNK TOY",target)
    run("hmount",target)
    try:
        run("hcopy","-m",mb,":")
        readme=scratch/"READ ME.txt"
        readme.write_bytes(b"DAFT PUNK SEQUENCER TOY\r\rDouble-click phoenixobot.dcr to start.\rOriginal 1998 Macintosh application.\r")
        run("hcopy","-r",readme,":READ ME")
        run("hls","-l")
    finally:
        run("humount")
    print("Wrote original sequencer disk",target,target.stat().st_size,flush=True)
