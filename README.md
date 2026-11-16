# IPEDS Database

Query U.S. postsecondary institution data from NCES IPEDS: directory, admissions,
enrollment, completions, tuition, financial aid, graduation rates, staffing and finance.
The database covers 1997 through the available 2025 files, with harmonized historical
tables and separate source-preserving 2024 Cost survey tables.

**November 9, 2026 release:** 27,889,050 rows in 25 source tables, plus three views.
The 1,416,376,320-byte file includes 30 verified final-revision corrections and adds
11,273 records from the two provisional 2024 Cost surveys. Existing table schemas
and views are unchanged. See [release provenance](https://huggingface.co/datasets/Nason/ipeds-database/resolve/9fd4840987da2e5496d7b98814678225f92b8514/sources-2026-11-09.json),
[the dictionary](https://huggingface.co/datasets/Nason/ipeds-database/resolve/9fd4840987da2e5496d7b98814678225f92b8514/DICTIONARY.md) and the [source/replay bundle](https://huggingface.co/datasets/Nason/ipeds-database/resolve/9fd4840987da2e5496d7b98814678225f92b8514/ipeds-source-replay-2026-11-09.zip).

## Query it remotely

```sql
INSTALL httpfs; LOAD httpfs;
ATTACH 'https://huggingface.co/datasets/Nason/ipeds-database/resolve/main/ipeds.duckdb' AS ipeds (READ_ONLY);
SELECT year, COUNT(*) AS institutions FROM ipeds.hd GROUP BY 1 ORDER BY 1 DESC LIMIT 5;
```

### R with DBI and duckdb

Install the dependencies once with `install.packages(c("DBI", "duckdb"))`.

```r
library(DBI)
con <- dbConnect(duckdb::duckdb())
dbExecute(con, "INSTALL httpfs")
dbExecute(con, "LOAD httpfs")
dbExecute(con, "ATTACH 'https://huggingface.co/datasets/Nason/ipeds-database/resolve/main/ipeds.duckdb' AS ipeds (READ_ONLY)")
dbGetQuery(con, "SELECT year FROM ipeds.hd LIMIT 5")
dbDisconnect(con, shutdown = TRUE)
```

DuckDB uses HTTP range requests; queries run on your machine and may need substantial memory or download data. A `LIMIT` does not guarantee a small scan.

Or install the Python `datapond` package or released R `datapond` package and connect to `ipeds-db`.

## What changed and what was checked

- Thirty existing table/year partitions were updated from provisional to revised/final
  source members. Their provisional inputs first had to reproduce the published baseline.
  The corrections add 799 net rows and also change values in existing rows.
- `cost1` adds 5,867 institution records and 419 columns including `year`.
  `cost2` adds 5,406 institution records and 540 columns including `year`.
  These are new tables, rather than incompatible replacements for older IC tuition tables.
- This release checked 60 of the 496 existing table/year source partitions. The remaining
  436 retain the previous publication and were not rechecked for newer revisions in this run.
  This is a bounded, verified update, not a claim that every historical vintage is current.
- The original 23 table schemas and three view definitions are preserved. Source identities,
  changes, validation results and reproducible inputs are included with the release.

## Cost data: preserve the source meaning

The Cost files are **provisional**. `year = 2024` identifies the source file/collection,
not the reporting period of every variable. COST1 includes periods from 2021-22 through
2024-25; COST2 includes average net price for 2023-24. Consult each variable's official
[Cost dictionary](https://huggingface.co/datasets/Nason/ipeds-database/resolve/9fd4840987da2e5496d7b98814678225f92b8514/cost-field-dictionary.json) before comparing periods or institutions.

`unitid` is BIGINT and joins to institution identifiers in other IPEDS tables. Other
original Cost fields are VARCHAR so codes, formatting, imputation flags and empty
strings remain exactly as published. An empty string is not converted to SQL NULL.
Cast numeric fields explicitly only after reviewing their documented codes.

```sql
SELECT unitid, year FROM ipeds.cost1 ORDER BY unitid LIMIT 5;
```

Avoid joining child tables without checking their grain. A table's row count is not
necessarily a count of institutions, and most historical joins need both `unitid` and `year`.

## Known legacy harmonization limits

The revision corrections retain the existing schema rather than silently changing
column types. In `hd`, numeric `close_date` cannot represent 68 slash-formatted date
strings in the 2024 source and retains those as NULL. In `gr`, numeric `line` cannot
represent the source labels `29A`, `12A`, `18A` and `11A`; those labels remain NULL.
The 2023 GR revision changes their record counts, not the set of affected label categories.
Revision-table source comparisons therefore use the existing harmonization. The new
Cost tables, by contrast, are checked losslessly against the original source fields.

## Sources and reproduction

Underlying data: [NCES IPEDS](https://nces.ed.gov/ipeds/use-the-data), public domain.
Original build pipeline by [Paul Goldsmith-Pinkham](https://github.com/paulgp/ipeds-database),
maintained here for Datapond. The release bundle supplies the bounded revision and
Cost-extension scripts, official source archives/dictionaries, hashes and replay instructions.
Use DuckDB 1.5.5 for the pinned replay. Read-only Python and R consumer checks must
pass against the published file before treating a release as verified.

The [previous baseline](https://huggingface.co/datasets/Nason/ipeds-database/tree/ff0d8df3742249f33dfab5eb4fff91ad56c2e785)
is retained in repository history. No automatic refresh is promised.


## GitHub release sources

The reviewed November 9 incremental rebuild and replay scripts are in [releases/2026-11-09](releases/2026-11-09). The hosted source bundle and provenance above preserve the exact published release. The root builder documents the earlier pipeline; use the release-specific instructions for this snapshot.
