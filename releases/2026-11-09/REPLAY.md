# Reproduce the IPEDS release

## Release scope

The combined database has 25 source tables and 27,889,050 rows. It updates 30 existing table/year partitions to final or revised NCES data and adds two provisional Cost tables. Relative to the baseline, the net increase is 12,072 rows: 799 from revisions and 11,273 from the Cost tables.

Only 60 of the baseline's 496 table/year source partitions were checked for this release. The other 436 partitions are preserved, not certified as current. This is not a complete historical refresh. Existing table schemas and view definitions are unchanged.

## Baseline

Download the baseline database from this immutable revision:

https://huggingface.co/datasets/Nason/ipeds-database/resolve/ff0d8df3742249f33dfab5eb4fff91ad56c2e785/ipeds.duckdb

Save it beside these files as `ipeds.original.duckdb`. Its required SHA-256 is `8df0b1a06af63f5724a3e883930f39ac1a80ac871f5d852b9eee75433388f429`, and its size is 1,360,801,792 bytes. The repository tree at the pinned commit confirms this LFS object identity. Details are in `baseline.json`. Do not substitute the repository's current `main` file.

## Replay

Use a fresh directory and Python 3.11 or newer. Install the exact package versions in `requirements.replay.txt`, including DuckDB 1.5.5, pandas 3.1.1 and NumPy 2.5.4. The artifact-writing scripts reject other DuckDB versions. Verify the bundle with `python verify_bundle.py` before running the build.

1. Run `python resolve_gr2023.py` to validate the documented GR 2023 label handling.
2. Run `python build_available.py` to create the limited revision database from the included source archives and verified baseline.
3. Run `python export_cost_compatible.py` to create the compatible Cost database from the included portable exports. These exports were checked against all raw Cost source values. `build_cost_addition.py` contains the original raw-source comparison logic.
4. Run `python compose_compatible.py` to combine the revision and Cost databases. The result is `ipeds.combined.duckdb155.candidate.duckdb`.

No additional NCES source downloads are required. Scripts refuse to overwrite existing candidate databases. The scripts and reports retain historical filenames for reproducibility; the word “candidate” in an output filename does not describe its data vintage.

The build checks all corrected partitions against their selected revised source members under the existing schema. It checks unchanged data by row counts and aggregate full-row hashes, and preserves existing schemas, metadata and views. Cost exports are checked using full-row comparisons. The final combination was created, closed, reopened and checked with DuckDB 1.5.5. Reports record artifact identities and exact validation scope. Replays can produce different database-file hashes because physical storage layout may differ; verify data and schema results as well as input hashes.

## Known legacy limitations

Revision-source equality is measured after the existing harmonization and schema projection, not against raw CSV text. The existing `hd.close_date` column is numeric, so date strings such as `07/31/2024` are represented as NULL. It is not repaired in this release.

The existing `gr.line` column is also numeric and cannot retain the source labels `29A`, `12A`, `18A` and `11A`. The GR 2023 revision changes the counts of those labels but introduces no new unsupported label category. This release preserves the existing schema. Retaining the labels requires a separate schema change.

## Cost data and typing

Both Cost files are provisional. COST1 contains cost-of-attendance fields spanning 2021–22 through 2024–25, together with 2024–25 student charges. COST2's documentation describes average net price for 2023–24. The added `year = 2024` column identifies the collection/file year, not the reporting period of every variable.

The `cost1` table has 5,867 rows and 419 columns including `year`. The `cost2` table has 5,406 rows and 540 columns including `year`. `unitid` is BIGINT after an exact decimal-representation check. Other source fields are VARCHAR to preserve codes, formatting and empty strings without numeric coercion. Column names are lowercased; no source fields are dropped. All 418 COST1 and 539 COST2 source fields are covered by the included NCES dictionaries and `cost_field_dictionary.json`.

## Software provenance

Earlier preparation used DuckDB 2.0.0. Its newly created Cost database used a storage format that DuckDB 1.5.5 could not read. That file is not included or designated for release. The compatible Cost and combined artifacts were created and reopened with DuckDB 1.5.5. The baseline-derived revision artifact was also successfully reopened with 1.5.5. The replay is pinned to 1.5.5.

## Included material

This bundle contains the 60 checked NCES source archives and their provenance, the two Cost source archives and official dictionaries, verified portable Cost exports, replay scripts, and relevant data-validation reports. It excludes database binaries. Source archives and portable-data bytes are unchanged. `replay_file_manifest.json` lists the SHA-256 and size of every included payload file.

The GR diagnostic counts unsupported labels directly in the raw CSV before harmonization, then reports losses during harmonization and casting separately. This avoids dependency-specific differences in where a label is converted to NULL. Numeric missing markers such as `.` are not treated as substantive labels. The public diagnostic was executed with DuckDB 1.5.5 and pandas 3.1.1; its checks passed.

## Clean replay validation

All documented replay commands were executed in a fresh directory with the exact pinned dependencies and the immutable baseline. The 30 revision partitions and both Cost tables rebuilt successfully. The replayed database matched the designated release database in all 25 source-table counts, complete schemas and full-row hash aggregates. Both metadata tables matched by full-row comparisons in both directions, and view definitions matched and executed. Physical database-file hashes differed, as expected when storage layout changes. The designated release database bytes were unchanged. See `full_replay_validation.json` for the dependency versions, per-table checks and artifact hashes.
