# IPEDS Database

Query U.S. postsecondary institution data from NCES IPEDS: directory, admissions,
enrollment, completions, tuition, financial aid, graduation rates, staffing and finance.
The database covers 1997 through the available 2025 files, with harmonized historical
tables and separate source-preserving 2024 Cost survey tables.

**November 16, 2026 release:** 27,889,094 rows in 25 source tables, plus three views.
The 2,388,144,128-byte file applies 308 additional historical revision
partitions to the November 9 baseline. All 496 historical source partitions and both
2024 Cost inputs were rechecked. Twenty-five IC_PY status-flag fields are now text
to preserve revised letter codes; other schemas and all three views are preserved.
See [release provenance](https://huggingface.co/datasets/Nason/ipeds-database/resolve/main/sources-2026-11-16.json),
[the dictionary](DICTIONARY.md), and the [source/replay bundle](https://huggingface.co/datasets/Nason/ipeds-database/resolve/main/ipeds-source-replay-2026-11-16.zip).

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

- Checked the 436 historical partitions omitted from the November 9 audit and applied
  308 additional revised source members. Before every correction, the provisional
  source had to reproduce the baseline partition exactly under the existing harmonization.
- Re-downloaded the other 60 historical archives and both 2024 Cost inputs. Fifty-seven
  historical archives and both Cost files are byte-identical. The other three historical
  archives were repackaged, but every contained CSV member is byte-identical.
- Every changed partition matches its selected revised source after existing harmonization
  and type projection. Unchanged years match baseline row counts and full-row hash sums.
  Twenty-four table schemas and three view definitions match the baseline. IC_PY has
  the explicit status-flag type correction described below.
- Literal-dot numeric missing markers are kept as NULL. Existing lossy field conversions
  remain documented below. Raw source archives and field-specific reviews accompany the
  release; source equality does not mean lossless raw-text equality for historical tables.

The November 9 release added 11,273 records from the two provisional Cost surveys and
corrected 30 recent historical partitions. That immutable release remains the replay
baseline for this complete check of the existing historical scope.

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

## Status-flag type correction

The revised IC2011_PY file uses letter status codes in 25 fields whose historical
DuckDB types were DOUBLE. Those fields in `ic_py` are now VARCHAR so every `R` and
`A` code is retained. Other years retain the previous numeric values as text (which
may include a `.0` suffix), with missing values still NULL. Codes are not normalized
across years; consult the relevant NCES dictionary before interpreting them.

All non-2011 IC_PY rows round-trip exactly to their previous typed values. All 25
revised flag columns match raw-source code counts and have no coerced NULLs. The
release validation lists every affected column. Four newly added PY0/PY1/PY2/PY3
source placeholders are entirely empty and do not add substantive data.

## Known legacy harmonization limits

The revision corrections retain the existing schema rather than silently changing
column types. In `hd`, numeric `close_date` cannot represent 68 slash-formatted date
strings in the 2024 source and retains those as NULL. In `gr`, numeric `line` cannot
represent the source labels `29A`, `12A`, `18A` and `11A`; those labels remain NULL.
GR revisions may change the counts of these already unsupported labels. Raw label reviews are retained with the release.
Revision-table source comparisons therefore use the existing harmonization. The new
Cost tables, by contrast, are checked losslessly against the original source fields.

## Sources and reproduction

Underlying data: [NCES IPEDS](https://nces.ed.gov/ipeds/use-the-data), public domain.
Original build pipeline by [Paul Goldsmith-Pinkham](https://github.com/paulgp/ipeds-database),
maintained here for Datapond. The November 16 bundle supplies the historical revision scripts, 436 official source archives,
hashes, validation and replay instructions. The pinned November 9 baseline and bundle
retain the recent revisions and Cost inputs. No year beyond the existing scope is inferred.
Use DuckDB 1.5.5 for the pinned replay. Read-only Python and R consumer checks must
pass against the published file before treating a release as verified.

The [previous baseline](https://huggingface.co/datasets/Nason/ipeds-database/tree/ff0d8df3742249f33dfab5eb4fff91ad56c2e785)
is retained in repository history. No automatic refresh is promised.


## GitHub release sources

Use [releases/2026-11-16/REPLAY.md](releases/2026-11-16/REPLAY.md) for this snapshot.
The prior [November 9 release sources](releases/2026-11-09) remain available. The root
builder documents the older pipeline; it is not the replay entry point for this release.
