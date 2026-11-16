# Reproduce the November 16, 2026 IPEDS release

This release checks all 496 historical table/year partitions in the existing database,
plus both 2024 Cost inputs. It applies 308 additional historical revisions and
contains 27,889,094 rows in 25 source tables. This is a frozen source check, not an
automatic schedule or a guarantee against later publisher revisions.

## Inputs and commands

Use Python 3.11 or newer and the exact versions in requirements.replay.txt.
The immutable November 9 baseline is pinned by URL, size and SHA-256 in baseline.json.
The 436 historical archives are included in the Hugging Face replay bundle in sources/.
The GitHub source folder omits those large archives. Run `python download_inputs.py`
to obtain the baseline and any missing exact inputs; it rejects changed bytes.

1. Extract the source bundle into a fresh directory.
2. Install requirements with `python -m pip install -r requirements.replay.txt`.
3. Run `python verify_bundle.py` to verify included source bytes.
4. Run `python download_inputs.py` to obtain the pinned baseline.
5. Run `python refresh_history.py` to produce ipeds.duckdb and validation-intermediate.json.
6. Run `python repair_flag_types.py` to correct IC2011_PY status-flag types and produce validation.json.
   The final report must have blocked_count = 0. The intermediate file is not for publication.

The build refuses to overwrite an output. It uses one DuckDB thread, a 2 GiB buffer
pool and at most 1 GiB of temporary spill, with at least 6 GiB free before building.
Memory limits do not bound pandas or the entire Python process. Input identity checks,
full-row multiset comparisons for changed partitions, retained-data hash aggregates,
schema checks and metadata updates run as part of the build. Blocked partitions prevent
successful completion. The sole expected intermediate exception is IC2011_PY, resolved
by step 6 with a 25-column DOUBLE-to-VARCHAR correction. Physical file hashes can
differ on replay; compare data/schema
results as well as exact input hashes.

## Audit and legacy limitations

recent-60-recheck.json records fresh downloads of the previously audited 60 partitions.
Three ZIP containers changed, but recent-source-comparison.json proves every contained
CSV unchanged. Both Cost archives are unchanged; see cost-recheck.json. The pinned
November 9 source bundle retains those CSVs, Cost dictionaries and source comparisons.

The existing harmonizer is retained. Table types are retained except for the 25
IC_PY status fields corrected to VARCHAR in step 6. Numeric dot missing markers map
to NULL. The first executed pass stopped affected partitions for explicit review; the
reviewed repair script and validation record preserve that history. The replay builder
recognizes those missing markers and reviews the same four GR line labels directly.
Four entirely empty PY0/PY1/PY2/PY3 placeholders in the revised IC2011_PY file are
explicitly checked as empty and excluded from the existing schema. Other unsupported-value differences
still require a documented review. hd.close_date and gr.line retain their known legacy
losses; see the main README and field-specific evidence. No raw-text losslessness claim
is made for historical tables.

The designated file was closed, reopened in DuckDB 1.5.5, checked against all 25 table
counts, 24 unchanged schemas, the explicit 25-field IC_PY type correction, and all
three baseline view definitions. Other IC_PY years round-trip exactly to their previous
typed rows; the revised 2011 letter-code counts match the raw source.
