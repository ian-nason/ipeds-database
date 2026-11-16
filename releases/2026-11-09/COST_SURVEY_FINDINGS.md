# Cost survey coverage

The 2024–25 IPEDS redesign moved cost-of-attendance and tuition items out of Institutional Characteristics into a new Cost component. The Cost component also collects some former Student Financial Aid items used to calculate net price. NCES describes the change at https://nces.ed.gov/ipeds/survey-components/release-memo?type=fall&year=2025 .

The baseline database's `ic_ay` and `ic_py` tables end in 2023. This release adds distinct `cost1` and `cost2` tables rather than combining the redesigned source fields with the old IC schemas. Existing IC tables and the `v_tuition_trends` view are unchanged. Users seeking the new Cost coverage should query the new tables and consult the field dictionaries.

## Sources

- https://nces.ed.gov/ipeds/complete-data-files/COST1_2024.zip : 5,867 institution rows, 418 source columns, 678,341 compressed bytes and 5,255,676 CSV bytes. The fields cover cost of attendance across 2021–22 through 2024–25 and student charges for 2024–25.
- https://nces.ed.gov/ipeds/complete-data-files/COST2_2024.zip : 5,406 institution rows, 539 source columns, 1,506,481 compressed bytes and 6,473,443 CSV bytes. The dictionary describes average net price for 2023–24.
- https://nces.ed.gov/ipeds/complete-data-files/COST1_2024_Dict.zip
- https://nces.ed.gov/ipeds/complete-data-files/COST2_2024_Dict.zip

Both data files are provisional. Their HTTP Last-Modified dates are in December 2025; those dates are not field reporting periods. Exact hashes, archive members and HTTP metadata are retained in the provenance files. The included dictionaries cover all 418 COST1 and 539 COST2 source fields, including imputation flags.

## Representation and checks

Both tables have unique, non-null institution identifiers. `unitid` is BIGINT after an exact decimal-representation check. Other source fields are stored as VARCHAR to preserve codes, formatting and empty strings without numeric coercion. Source names are lowercased, and a BIGINT `year` column with value 2024 identifies the collection/file year. It does not mean that every measure refers to 2024.

Exact raw-value and full-row comparisons passed. The compatible tables also passed full-row comparison after portable export and were created and reopened with DuckDB 1.5.5. The new tables have 419 and 540 columns respectively after adding `year`, and add 11,273 rows in total.
