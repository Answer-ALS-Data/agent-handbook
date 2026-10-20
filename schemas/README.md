# schemas

These pages describe the columns and file layouts of the Answer ALS and ALS TDI releases. They describe columns, never values. No page here holds a participant row, a participant identifier or a count taken from a data file, and none may. They were written from the schema files, the dictionaries and the header lines of the data files only.

## How the pieces fit

Each cohort publishes four kinds of file. They are separate files that share keys.

| Piece | One row per | Answer ALS | ALS TDI | Page |
|---|---|---|---|---|
| Release index | participant | ReleaseIndex_r8.csv with ElementsDefinition_r8.csv and HierarchyTree_r8.csv | ALS_TDI_ReleaseIndex_r2 (staged) or r2.5 (renamed columns) with its two schema files | index-answer-als-r8.md, index-als-tdi-r2-5.md, index-shared-columns.md |
| Clinical package | form entry or visit | 34 form CSVs and __Clinical_Dictionary_Sep_2026.csv | 18 TDI_*_V2 tables and TDI_data_dictionary | clinical-answer-als.md, clinical-als-tdi.md |
| Sample mapping | sample | Sample_Mapping_File_<Month>_<Year>.csv | Sample_Mapping_File_ALS_TDI_R2.csv | sample-mapping.md |
| OMOP | OMOP record | built by the owner's ETL notebook | delivered by ALS TDI, CDM v5.4 | omop.md |

The index is the portal's view of a participant: availability flags, demographics, disease status and summary scores. The clinical package holds the detail. The sample mapping ties omics samples to participants. OMOP holds the clinical data again in a standard model for tools that read OMOP.

## Identifiers in words

- GUID: the participant's global unique identifier.
- Participant_ID (index): a cohort prefix, CASE- or CTRL-, followed by the GUID. The prefix is fixed at enrollment. In Answer ALS, CTRL- is used for healthy controls and CASE- for everyone else.
- ALS TDI also has a numeric ARC participant number, the Participant ID column of its clinical tables.

## Join keys

| From | To | Key |
|---|---|---|
| Answer ALS index | Answer ALS clinical forms | Participant_ID = Participant_ID |
| ALS TDI index | ALS TDI clinical package | index Participant_ID = package GUID (the package GUID column holds the prefix plus GUID form) |
| ALS TDI clinical tables | each other | numeric Participant ID |
| Either index | its sample mapping | Participant_ID = Participant ID |
| Answer ALS OMOP | Answer ALS clinical and index | person_source_value = Participant_ID |
| ALS TDI OMOP | ALS TDI clinical | person_source_value with its prefix stripped, as an integer, = numeric Participant ID |
| OMOP tables | each other | person_id (OMOP only) |

ALS TDI OMOP person_source_value is PREFIX_n, where PREFIX is CASE, CONTROL or ASYMP and n is the numeric participant number. Those prefixes do not match the clinical CASE- / CTRL- prefixes, so always join on the number, then check that the prefix agrees with the clinical cohort. Diff two ALS TDI releases on the numeric Participant ID, not on GUID.

## Comparing the two cohorts

The two indexes share 25 column meanings. ALS TDI Release 2.5 uses the Answer ALS names for them, but values were not recoded. index-shared-columns.md says which can be compared as they stand.

## Privacy line

- Read schema files, dictionaries and header lines. Do not read data rows.
- Write column names, types, codes from a dictionary and file layouts. Do not write values from a data file, participant identifiers, or counts taken from a data file.
- Published release-level counts are on the programs/ pages. Those are the only counts to repeat.

## Pages

- index-answer-als-r8.md: every Answer ALS Release 8 index column.
- index-als-tdi-r2-5.md: every ALS TDI Release 2.5 index column.
- index-shared-columns.md: the 25 shared names and their vocabulary differences.
- clinical-answer-als.md: Answer ALS clinical forms.
- clinical-als-tdi.md: ALS TDI clinical tables.
- sample-mapping.md: both sample mapping files and the ALS TDI timepoint rules.
- omop.md: OMOP tables per cohort, the mapping types and the join rules.
