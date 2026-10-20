# Sample mapping files: columns

A sample mapping file has one row per sample and ties each omics sample to its participant. There is one per cohort. This page is written from the header line of each file and the board's decisions. It describes columns, never values.

## Answer ALS

File: Sample_Mapping_File_March_2026.csv, made by the owner's script in data-scripts (Answer ALS/Data Curation/Sample Mapping File). Release 8 ships no new Answer ALS sample mapping; the portal links Sample_Mapping_File_April_2026.csv. The columns below are from the March 2026 header.

| Column | Meaning |
|---|---|
| Participant ID | The participant the sample belongs to, in the index Participant_ID form (CASE- or CTRL- plus the GUID). |
| Sample ID | The sample's name as used in the omics files. |
| GUID-Batch | The GUID joined to the batch, naming one participant's sample in one batch. |
| GUID | The participant GUID, without the cohort prefix. |
| Cell Line | The cell type or tissue the sample came from. |
| Batch # | The diMN differentiation batch (the index Batch column). |
| Vial ID | The biobank vial the sample was taken from. |
| Site | The clinical site that collected the sample. |
| Shipment | The shipment that carried the sample to the omics center. |
| Proteomic_Instrument | The instrument used for proteomics (the index Proteomic_Instrument column). |
| digestion_batch | The proteomics digestion batch (the index Proteomic_Digestion_Batch column). |

## ALS TDI

File: Sample_Mapping_File_ALS_TDI_R2.csv, the Release 2 final file. It mirrors the Answer ALS file without the Answer ALS-only columns, and adds Omic and Timepoint.

| Column | Meaning |
|---|---|
| Participant ID | The participant the sample belongs to, in the index Participant_ID form (CASE- or CTRL- plus the GUID). |
| Sample ID | The sample's name; for genomics it is the staged file name, kept as it is even when the participant's ID changes. |
| GUID | The participant GUID. |
| Cell Line | The sample tissue. Blood unless stated otherwise. |
| Omic | The modality: genomics or transcriptomics. |
| Vial ID | The biobank vial the sample was taken from. |
| Timepoint | The sample's timepoint for that participant and modality (rules below). |

The current header has seven columns. The als-tdi topic notes also name GUID-Batch and Batch #; those are not in the Release 2 file header.

## Timepoint rules (ALS TDI)

- Timepoints are numbered from 1 for each participant and each modality, with -G marking genomics and -T marking transcriptomics. Genomics and transcriptomics are numbered on their own.
- Genomics timepoints follow ascending numeric Vial ID.
- Transcriptomics timepoints follow ascending days since sign up, from the rnaseq timepoint mapping that ALS TDI delivered, because no transcriptomics files are staged yet.
- The index columns GENOMICS_TIMEPOINTS_AVAILABLE and TRANSCRIPTOMICS_TIMEPOINTS_AVAILABLE list a participant's timepoint numbers as one comma-separated string ("1, 2").
- When a participant's ID changes, only Participant ID is updated in the mapping; Sample ID stays the real file name.

## Joins

- Mapping to index: Participant ID equals the index Participant_ID, in both cohorts.
- Mapping to omics files: Sample ID is the name used in the omics data.
- Answer ALS has no Timepoint column in its mapping.

The meanings of the Answer ALS columns are read from their names and the matching index columns; no column description ships with the file.

## Source

Header lines of Sample_Mapping_File_March_2026.csv (data-scripts output) and Sample_Mapping_File_ALS_TDI_R2.csv, and als-tdi/CONTEXT.md decisions of 2026-08-05, 2026-08-07, 2026-08-28 and 2026-09-23.
