# Missing original Shockwave Audio — archival inventory (2026-10-30)

**Goal:** recover authentic binary SWA files referenced by the 1998 Daft Punk Homework site, not substitute modern recordings.

## Result
No original SWA binary recovered. Twenty-three SWA references remain unresolved.

Main site: swa/world.swa, swa/burnin.swa, swa/revolution.swa, swa/dafunk.swa, swa/musique.swa, swa/6.swa, swa/9.swa.
Discography: disco/swa/1.swa through disco/swa/16.swa. These correspond to all sixteen Homework tracks in album order, per the original page titles.

## Verified archival searches
77 archive-index requests against Internet Archive CDX and Arquivo.pt, examining 1997–2010, both apex and www hostnames. All eight main and discography sound-directory prefix indexes (www and apex, both services) returned empty results. Exact-file requests for the seven main SWA paths returned empty results; some individual discography lookups were refused at the connection level and should not be counted as negative evidence.

Results are in audio_index_results.json. No index hits does not prove that originals cannot survive in unindexed WARC records, an alternate hostname, old offline mirrors, personal backups, or caches.

## Next leads
1. Contact Internet Archive regarding unindexed WARC captures of audio files.
2. Search Flashpoint Archive's URL database for daftpunk.com/swa and daftpunk.com/disco/swa.
3. Seek 1997–2001 local fan-site backups, downloaded mirrors, or period browser caches.
4. If originals cannot be recovered, a distinct, explicitly labelled playable reconstruction using appropriately licensed album audio could restore functionality; do not falsely represent it as original SWA.

## Flashpoint comparison (October 30, 2026)

Flashpoint's current searchable database identifies the original **Daft Punk Website** as Shockwave, release year 1997, developer credit DaftTrax, source capture April 29 1999, UUID `1dadf50d-0fe9-4e29-a7ec-12690cc51747`, with status Partial; Playable.

Its preservation notes state "All .swf and .swa files are lost." This is imprecise for SWFs: the actual package includes `charles2.swf` (34,733 bytes), but it contains **zero** original `.swa` files.

The source game ZIP was retrieved directly from the public Flashpoint storage:
https://download.unstable.life/gib-roms/Games/1dadf50d-0fe9-4e29-a7ec-12690cc51747-1738978032425.zip
It contains the previously recovered HTML, graphics, nine DCR movies, and `charles2.swf` (a file inventory is in `flashpoint_package_audit.json`). No missing audio recovered from Flashpoint.

Flashpoint API searches were executed using both the live https://flashpointarchive.org/api/search endpoint and older https://db-api.unstable.life/search. Flashpoint search results and original URLs are preserved in `flashpoint_search_results.json`.

## Private mirror and personal-archive leads

Internet searches for the filenames `world.swa`, `burnin.swa`, `revolution.swa`, and the path `disco/swa/` did not locate a publicly indexed third-party copy. GitHub code searches for original site paths also returned no matches.

- **The Daft Punk Historian / Wub (Luke Perez)**: https://thedaftpunkhistorian.weebly.com/ . This collector maintains backups of archival Daft Punk documents and the historic official-site timeline, and lists older fan sites such as uuuu.org (1997–2001) and daftcrew.com (2000–2006). No claim that their archives include the original SWA files.
- **Daft Bootlegs / u/FinleyGomez**: https://www.reddit.com/r/DaftPunk/comments/1mu8xs6/definitive_daft_punk_bootleg_archive_1994_to_2003/ . Collector with experience recovering rare 1990s recordings, though the public collection concerns live recordings, not web assets.
- **Flashpoint Discord / web-cache channel**: https://flashpointarchive.org/datahub/Recovering_Files_from_Browser_Cache . Official guide describes recovering original assets from old Netscape/Internet Explorer caches. Historical caches or private full-site backups now look more promising than further conventional Wayback indexing.

**Next concrete action:** make a narrowly targeted request to these collectors for full `daftpunk.com` site mirrors or local browser caches dated 1997–2001, specifically the 23 SWA paths. Do not describe substitute recordings as recovered originals. No external parties have yet been contacted.


## Expanded search: public catalogs, manifests and alternate hostnames (October 30, 2026)

An additional 28 cross-domain archive queries examined www/non-www daftpunk.net, daft-punk.com, ftp.daftpunk.com, port-80 variants, and period fan sites uuuu.org and daftcrew.com, for the relative sound directories. None produced an indexed `.swa` match. These queries only searched the specified directories; mirrors could have stored files in differently named paths.

A separate public-catalog search queried the Internet Archive Advanced Search and scraping API for related website backups, title and description variants, and the distinctive SWA filenames. None of the plausible archive-item listings proved to contain a binary website backup. `grep.app` returned HTTP 429 for all ten attempted filename/code searches, so these are *inconclusive*, not negative evidence. GitHub indexed searches for distinctive original-site paths produced no matches.

**New item discovered:** https://archive.org/details/19971998-daftpunk.com-daft-questions (`19971998-daftpunk.com-daft-questions`). Its manifest was downloaded and inspected. It contains a 2026 QuickTime screen recording of a 1997–1998 Daft Punk self-interview and video derivatives, but no `swa` file, DCR movie, or website ZIP. Machine-readable manifest: `internet_archive_daftpunk_find.json`.

Internet Archive general-purpose index results are stored in `deep_mirror_hunt.json`. Alternate-domain raw results are in `cross_domain_audio_results.json`.

**Protoweb:** project maintains a large curated set of restored 1990s websites and a Wayback proxy, but the public list of restored sites does not include daftpunk.com. Its project documentation says the server-side archives are not generally provided as downloadable collections. No proprietary Protoweb holdings were directly inspected; this avenue requires a curator response.

### Evidence summary
- Original SWA audio files recovered: 0 of 23.
- Checked independently preserved Flashpoint package: 0 SWA (although some DCR/SWF material survives).
- Confirmed Wayback and Arquivo.pt captures under the exact original and alternate domain audio paths: 0.
- Additional physical archives, CD-ROM collections and private browser caches are not publicly searchable in aggregate; absence from these sources **cannot** be established.

### Most promising remaining contacts
1. The Daft Punk Historian (preserves official website history; may know original website developer or old fan collectors): https://thedaftpunkhistorian.weebly.com/article--interview-database.html
2. Flashpoint web-cache preservation group: https://flashpointarchive.org/datahub/Recovering_Files_from_Browser_Cache
3. Protoweb restoration curators: https://protoweb.org/.

The practical next step is human outreach requesting any 1997–2001 full-site backups or Netscape/Internet Explorer caches. It would be inaccurate to claim exhaustive coverage of all privately held data.