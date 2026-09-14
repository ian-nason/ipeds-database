---
license: other
license_name: public-domain
tags:
  - education
  - ipeds
  - nces
  - higher-education
  - duckdb
  - datapond
pretty_name: IPEDS Database (NCES, 1997-2025)
size_categories:
  - 10M<n<100M
---

# IPEDS Database

Harmonized DuckDB database of NCES Integrated Postsecondary Education Data
System (IPEDS) complete data files: every U.S. postsecondary institution from
1997 to the 2025-26 provisional release -- directory, admissions, enrollment,
completions, tuition, financial aid, graduation rates, outcomes, staffing and
finance.

Build pipeline by [Paul Goldsmith-Pinkham](https://github.com/paulgp/ipeds-database)
(also published at `paulgp85/ipeds-db`); this copy is rebuilt from the datapond fork
https://github.com/ian-nason/ipeds-database with the files NCES released through
July 2026. Table list, row counts and the column dictionary: see `DICTIONARY.md`
and the `_metadata` / `_columns` tables inside the file.

## Query it remotely

```sql
INSTALL httpfs; LOAD httpfs;
ATTACH 'https://huggingface.co/datasets/Nason/ipeds-database/resolve/main/ipeds.duckdb' AS ipeds (READ_ONLY);
SELECT year, COUNT(*) AS institutions FROM ipeds.hd GROUP BY 1 ORDER BY 1 DESC LIMIT 5;
```

Or `pip install datapond` / `pak::pak("datapond-db/datapond-r")`, then connect to `ipeds-db`.

## Upload (maintainer notes)

```bash
hf upload Nason/ipeds-database ./hf_dataset_card.md README.md --repo-type dataset
hf upload Nason/ipeds-database ./DICTIONARY.md DICTIONARY.md --repo-type dataset
hf upload Nason/ipeds-database ./ipeds.duckdb ipeds.duckdb --repo-type dataset
```
Then point the registry entry's `huggingface`/`attach_url`/`github` at the new locations
and set `maintainer` to credit both people.
