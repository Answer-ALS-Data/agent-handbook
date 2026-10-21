# File and folder naming

How Answer ALS and ALS TDI release files and folders are named. Names and patterns only. In a pattern, <N> is a release number, <Form> a form name, <Month> a full month name and <Mon> a three letter month.

## Release suffix and wording

- Release files carry the plain release suffix _r<N>, lower case r, before the extension: ReleaseIndex_r8.csv. ALS TDI adds its prefix: ALS_TDI_ReleaseIndex_r2.csv.
- Internal sub-releases (r8.1, r8.2, r8.3) are build labels. They never appear in a released file name or in a document for data users; the released files of every build carry the plain _r<N>.
- A bundle with a new shape gets its own decimal version in the file name, so the old bundle stays as it was. Example: the ALS TDI r2.5 trio, with renamed columns, next to the unchanged r2 trio.
- In text for data users, write "Release 8" or "Release 2". Never r8.3, R8.3 or a similar label. Short forms R8 and R2 appear only in document file names (below).
- The portal data table copy is named <cohort>_dataportal_datatable.csv and has the same bytes as the release index.

## Index trio

| Cohort | Release index | Elements definition | Hierarchy tree |
|---|---|---|---|
| Answer ALS | ReleaseIndex_r<N>.csv | ElementsDefinition_r<N>.csv | HierarchyTree_r<N>.csv |
| ALS TDI | ALS_TDI_ReleaseIndex_r<N>.csv | ALS_TDI_ElementsDefinition_r<N>.csv | ALS_TDI_HierarchyTree_r<N>.csv |

The three files of one version always share the same suffix and are released together. Any file name containing ReleaseIndex holds participant rows.

Data table copies: aals_dataportal_datatable.csv (Answer ALS) and als_tdi_dataportal_datatable.csv (ALS TDI).

## Clinical forms

| Cohort | Pattern | Notes |
|---|---|---|
| Answer ALS, raw drop | v_NB_IATI_<Form>.csv inside a folder AnswerALS_<DD><Mon><YYYY> | The export prefix and the drop date in the folder name. |
| Answer ALS, curated | <Form>.csv, for example ALSFRS_R.csv | Form Name in the dictionary equals the file name without .csv. |
| Answer ALS, participant table | aals_participants.csv in reference_tables/ | Built by its own script beside the curation script. |
| ALS TDI, as delivered | TDI_<TOPIC>_V<n>.xlsx, for example TDI_OVERVIEW_V2.xlsx | V<n> is the delivery version, not the release. |
| ALS TDI, published | TDI_<TOPIC>_V<n>.csv | Same stem as the delivered workbook. |
| ALS TDI, participant table | als_tdi_participants.csv | The participant file shape of the Release 1 portal. |

Folder names: the curated Answer ALS package folder is r<N>_full_clinical_data/.

## Dictionary

- Answer ALS: __Clinical_Dictionary_<Mon>_<YYYY>.csv, two leading underscores, named for the month it was settled, for example __Clinical_Dictionary_Sep_2026.csv. It ships inside the clinical package.
- ALS TDI: TDI_data_dictionary.xlsx as delivered, TDI_data_dictionary.csv as published.
- Inside the Answer ALS dictionary, Form Name equals the form file stem. Inside the ALS TDI dictionary, Form Name is the file stem without _V<n>.

## Sample mapping

- Answer ALS: Sample_Mapping_File_<Month>_<YYYY>.csv, for example Sample_Mapping_File_April_2026.csv. Named for the month it was made, not the release.
- ALS TDI: Sample_Mapping_File_ALS_TDI_R<N>.csv, named for the release.

## OMOP

- ALS TDI: one CSV per OMOP table, named for the table in lower case (person.csv, observation_period.csv, visit_occurrence.csv and so on), with a SHA256SUMS file beside them. Delivered names are kept unchanged.
- Answer ALS: tables are built by the OMOP notebook and named for the OMOP tables in upper case inside it (PERSON, VISIT_OCCURRENCE, ...). A release file name is not settled yet.

## Omics files and folders

Folders by data level, then participant, then sample:

| Modality | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|
| Genomics (G) | 1_fastq/ FASTQ | 2_bam/ CRAM | 3_vcf/ VCF | Joint VCF |
| Epigenomics (E) | 1_fastq/ FASTQ | 2_bam/ BAM | 3_peaks/ peaks | Matrix of consensus peak counts |
| Transcriptomics (T) | 1_fastq/ FASTQ | 2_bam/ BAM | counts | Matrix of counts |
| Proteomics (P) | 1_wiff/ WIFF | 2_mzML/ mzML | none | Matrix of intensities |

- Path shape: <level folder>/<Participant_ID>/<Participant_ID>-<vial>-<letter>/<Participant_ID>-<vial>-<letter><tail>, where <letter> is the modality letter above and <tail> is the pipeline suffix (for example _1.fastq.gz, .sorted.bam, _1.final.cram, .profile.mzML).
- Level 4 matrix files: <Program>-<participant count in matrix>-<letter>-v<version>-release<N>_<pipeline metadata>.csv, for example AnswerALS-<n>-T-v1-release<N>_rna-counts-matrix.csv.
- Level 5 holds comparisons between two groups (differential genes, peaks or proteins).
- ALS TDI timepoints carry -G (genomics) or -T (transcriptomics) after the timepoint number.
- A genomics Sample ID is the staged file name and is not renamed when a participant's ID changes.

## Splicing

- Matrices: ALS_all_batch_regtools_cluster_perind.counts.gz and ALS_all_batch_regtools_cluster_perind_numers.counts.gz, the same two names in every version.
- A changed set is labeled by version (v1 as delivered, v2 after columns were removed), not by renaming the files. REMOVED_COLUMNS.txt beside them lists removed sample headers.

## Release documents

- Answer ALS release notes: AnswerALS_R<N>_Release_Notes.md and .docx.
- ALS TDI: ALS_TDI_README and ALS_TDI_R<N>_Release_Notes, each as .md and .docx.
- The release notes say what changed in this release; the README says what stays true.

## SOP file names

- Pattern: <PREFIX>-SOP-<NNN>-V<n>. <Title>.docx, with a .pdf of the same name. NNN is a three digit number, V<n> the version, then a period, a space and the title in title case. Example: AALS-SOP-005-V1. Clinical Data Curation.docx.
- Prefixes: AALS for Answer ALS, ALSTDI for ALS TDI, and the Neuromine program name in capital letters for Neuromine.
- A new revision keeps the file name and adds a row to the revision table inside, until the version number is raised.

## Date forms

| Where | Form | Example shape |
|---|---|---|
| Dated folders and dates in text | YYYY-MM-DD | 2026-10-21 |
| Answer ALS raw drop folder | DDMonYYYY | AnswerALS_17Sep2026 |
| Answer ALS dictionary | Mon_YYYY | __Clinical_Dictionary_Sep_2026.csv |
| Answer ALS sample mapping | Month_YYYY | Sample_Mapping_File_April_2026.csv |
| SOP effective date | MM/DD/YYYY | in the SOP title table |
| Dates inside clinical data | relative days | days before (-) or after (+) day 0, never a calendar date |
| Answer ALS OMOP dates | fixed baseline plus relative days | not real calendar dates |

## Rules that hold everywhere

- ASCII file names: letters, digits, underscore, hyphen and period. SOP titles are the one place spaces appear.
- No participant identifier in a release-level file name. Participant identifiers appear only in omics paths, by the pattern above.
- CSV files are UTF-8. ALS TDI index and clinical CSVs are written with LF line ends and no BOM.
