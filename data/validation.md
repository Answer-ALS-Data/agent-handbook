# Validation checks

What is checked on a delivery coming in and on a release going out, and what passes. Each check names what it compares and the rule that makes it pass. No count or value from a data file is given here; every checker recomputes its own numbers from the files each time.

## How the checks work

- A delivery is checked before anything is built from it. A release is checked before it is staged.
- Each check is a script, run read-only on the inputs. A checker exits with failure on any mismatch.
- A finding is blocking (the build stops) or flagged (characterised, written down and the build goes on). The report lists defects only, each with who owns the fix: the provider, the data team, or accepted.
- Every number a report states is recomputed by its checker, and a number the checker does not assert fails the run.
- Checkers have a mutate mode: they break each output once on purpose, and every break must be caught.
- Builds are reproducible: a rebuild into a temporary folder must give every output byte for byte.

## Delivery: provider package in

### Answer ALS raw clinical drop

| Check | What against what | Pass rule |
|---|---|---|
| File presence | Forms in the drop against forms in the previous release | Every form present. A missing form blocks. |
| Encoding | Each file against UTF-8 | Every file decodes. A decode error blocks. |
| Row counts | Rows per form in the drop against the previous release | No form has fewer rows. A drop in rows blocks. |
| Columns | Columns per form against the previous release | No previous column missing and no leaked index column (Unnamed, index, row number). Either blocks. |
| Identifiers | SubjectUID, Visit_Name and Form_Name in every row | Never empty. An empty identifier blocks. |
| Day anchor | Relative day values against the previous release, row matched | Same values, or a shift of one or two days in every value that re-anchors the drop. Any other shift blocks. |
| Types | Values in numeric fields against the dictionary Field Type | Numeric. Identifier columns typed numeric but holding text are exempt. A mismatch is flagged. |
| Coded values | Values in coded fields against the dictionary code list | In the list. A value outside it is flagged. |
| Placeholders | Cells against literal NA, N/A, None and similar | Read as empty. Flagged with the count. |
| Duplicates | Rows against other rows of the same form | Exact duplicates are dropped by curation and listed. |
| Personal data columns | Column names against Initials and other free-text identity columns | Dropped by curation. |
| Previous drop | The drop against the previous drop of the same release, cell by cell | Every difference explained; no unexplained row. |
| Verdict | All blocking findings | Go for curation when there are none. Flagged findings go to the curation notes. |

### ALS TDI clinical delivery

| Check | What against what | Pass rule |
|---|---|---|
| Dictionary coverage | Delivered columns of each table against dictionary rows | Every column has a row. A column without one is a provider defect, listed. |
| Vendor counts | Counts in the provider's release notes against counts recomputed from the files | Equal. A difference is a provider defect; the recomputed count is the one published. |
| Re-delivery | A new delivery against the previous copy, cell by cell | Every difference listed in a diff table. |
| Participants | Delivered participants against the previous release, on the numeric Participant ID | Every change explained. Never diff on GUID, which can change. |
| OMOP roster | OMOP person against clinical participants, on the number in person_source_value | Every person joins; the OMOP prefix agrees with the clinical cohort. |
| OMOP documentation | Each OMOP table against what the provider's OMOP document says it holds | Agrees. A difference is a provider defect. |
| Omics roster | Delivery roster and sample mapping from the provider against the staging listing | Every staged sample is on the roster. A modality that is not staged rests on the provider mapping and is marked accepted. |
| Previous answers | Survey answers in the previous release against the delivery | Present in both, or the loss is listed as a provider defect. |

## Release: files out

### Index

| Check | What against what | Pass rule |
|---|---|---|
| Trio | ReleaseIndex header against ElementsDefinition element names and HierarchyTree leaves | Same names; the three files share one suffix and are released together. |
| Frozen columns | Every column not meant to change against the previous build, by sha256 | Byte for byte the same. |
| Derived clinical columns | IS_DECEASED, AGE_AT_DEATH and REVISED_EL_ESCORIAL_CRITERIA against a fresh computation from the clinical package | Equal. IS_DECEASED is Yes when a Mortality record exists; AGE_AT_DEATH is the floor of (death day minus birth day) over days per year; the El Escorial column maps the AALSDXFX conclusion code to its label. |
| Change list | The index against the previous build, cell by cell | The CHANGES list is exactly the cell diff. |
| Participant_ID | Prefix plus GUID against the study group | CTRL- for Healthy Control, CASE- for everyone else; the prefix never changes after enrollment. |
| WGS columns | NYGC id against WGS_Sequencing_Protocol_Used and the other WGS columns | Both filled or both empty. |
| Repeat lengths | C9orf72 and ATXN2 repeat length columns against WGS_Sequencing_Protocol_Used and NYGC id | Filled only for TruSeq PCR-Free genomes with an NYGC id. Empty for PCR amplified genomes. |
| Cell lines | HasIPSC and HasDIMN against iPSCLine and diMNs_line | Yes only when the line column is filled. |
| diMN details | diMNs_line against Batch and the staining percent columns (PCT_ISL1, PCT_NKX61, PCT_TUJ1, PCT_S100b, PCT_Nestin) | When a line is filled, all of them are filled. |
| Tissue | iPSCLine against Primary_Tissue | When a line is filled, the tissue is filled. |
| Ages | AGE_AT_SYMPTOM_ONSET and AGE_AT_DEATH against Age_Sample_Collection_Cedars | Onset and death are not before the collection age where both are known. |
| Mutation reports | ClinReport_Mutations_Details naming C9orf72 against NYGC id | An NYGC id is present. |
| Renamed bundle | A renamed-column index against its source index and the crosswalk | Header is the source header renamed in one pass; rows and every cell value unchanged; every new name exists in the target cohort's definitions; no old name left. |
| Data table copy | The portal data table file against the release index | Same bytes. |
| File format | Each ALS TDI index file against UTF-8, LF line ends and no BOM | All three hold. ALSFRS_Slope is never in scientific notation. |

### Clinical package

| Check | What against what | Pass rule |
|---|---|---|
| Provenance | Each curated form against a fresh run of the committed curation script on a copy of the raw drop | Byte for byte the same. |
| Shape | Columns of each form against the previous release | Same columns; columns marked for removal absent; Key Events forms carry no Visit_Date. |
| Rows | Rows per form against the de-duplicated raw drop | Same number. |
| Cells | Every cell against the raw drop | Equal, with placeholders turned to empty. No placeholder left. |
| Participant_ID | Participant_ID against SubjectUID and subjects.subject_group_id | CTRL- plus SubjectUID for Healthy Control, CASE- plus SubjectUID otherwise. |
| Dictionary | The dictionary against the previous dictionary plus the tabled changes | Exactly equal. Form Name equals the file stem. |
| Encoding | Each file against UTF-8 without BOM | Holds. |
| ALS TDI tables | Each published CSV against its delivered workbook | Equal except exactly the cells in the cleaning list, each with its before value. UTF-8, LF, no BOM. |
| ALS TDI participant file | The participant file against the delivered participants and the index | Same set, sorted, Case_Control follows the prefix, Sex agrees with the index on every row. |

### Sample mapping

| Check | What against what | Pass rule |
|---|---|---|
| Previous rows | The new mapping against the previous mapping | Every previous row survives unchanged. |
| New samples | New transcriptomics rows against the provider's sample list | One to one. |
| Timepoints | Timepoint against the rule | Numbered from 1 per participant and modality: genomics by ascending Vial ID, transcriptomics by ascending days since sign up. |
| Coverage | Delivered participants against mapping rows | Every delivered participant has a row. A sample with no clinical record is kept only on staged-file evidence, as accepted. |
| Keys | Participant ID against the index Participant_ID | Same form, joins. |
| Genomics rows | Genomics rows against the previous mapping | Untouched; Sample ID stays the staged file name. |

### OMOP

| Check | What against what | Pass rule |
|---|---|---|
| Copy | Each published OMOP CSV against the delivered file | Byte for byte the same, and listed with its sha256 in SHA256SUMS. |
| Table set | Published tables against delivered tables | Same set. |
| Person join | person_source_value number against the clinical Participant ID | Joins, and the prefix agrees with the cohort. |

### Splicing

| Check | What against what | Pass rule |
|---|---|---|
| Header only | What the check reads | Header row, field counts per line and the intron ID column only. No cell value is read. |
| Format | Line ends and header tokens against the input | LF kept, every header token quoted, leading chrom token kept. |
| Columns | Sample columns against the input minus the removed columns | Equal; no column of a sequestered participant; no duplicate header. |
| Renamed headers | Bad headers against canonical Sample IDs | The delivered name is gone and the canonical name is present. |
| Pair | perind and numers sample headers | Identical. |
| Rows | Line count and intron ID column against the input | Unchanged; every line has the expected number of fields. |
| Index | Participants in the headers against index HAS_SPLICING = Yes | The same set, both ways. |
| Sample mapping | Headers against the sample mapping | Only the known misses are missing. |
