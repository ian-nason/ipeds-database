# Changelog

## Unreleased — September 2026 refresh (datapond fork)

Fork of https://github.com/paulgp/ipeds-database maintained for the datapond
registry; the build pipeline and harmonization are Paul Goldsmith-Pinkham's.

- NCES moved the complete data files to `/ipeds/complete-data-files/`; the
  downloader tries that path first and falls back to the old
  `/ipeds/datacenter/data/` path.
- Manifest extended to the files released since March 2026: HD/IC/EFIA/EFFY/
  C/FLAGS 2025 (fall 2025-26 provisional), ADM/EF/GR/GR200/OM/EAP/SAL/AL 2024,
  SFA2324 and F2324 finance files (2024-25 winter/spring components). `IC{y}_AY`
  and `IC{y}_PY` stop at 2023 because tuition moved to the new Cost (CST)
  component, which NCES has not published as a complete data file.
- `process_survey()` now stages each year into DuckDB and combines them with
  `UNION ALL BY NAME` instead of concatenating every year in pandas (the old
  approach needed >16 GB for the completions table). DuckDB memory limit and
  thread count are configurable via `DATAPOND_MEMORY_LIMIT` / `DATAPOND_THREADS`.
- `publish_to_hf.py` (to add) publishes the refreshed file under the datapond
  maintainer's Hugging Face account.
