# ALS TDI index, Release 2.5: columns

The ALS TDI release index has one row per participant and one column per element below. Release 2.5 is the Release 2 index with 19 columns renamed to the Answer ALS Release 8 names; rows and cell values are the same as Release 2, and Release 2 is still the staged index on the portal. The set is three files: ALS_TDI_ReleaseIndex_r2.5.csv (the rows), ALS_TDI_ElementsDefinition_r2.5.csv and ALS_TDI_HierarchyTree_r2.5.csv. This page is written from the last two only. It describes columns, never values.

The columns read the same way as on index-answer-als-r8.md:

- Element Name: the column header in the index.
- Display Name: the label on the portal.
- Type: Edm.String is text, Edm.Int32 a whole number, Edm.Double a decimal.
- Facet: Yes means the column is a filter on the portal search page.
- Field: Yes means the column shows in the portal data table.
- Group: the facet group from the HierarchyTree, or "Data table only".
- Meaning: the Description, cut to one sentence.

For the original Release 2 name of each renamed column, see index-shared-columns.md or als-tdi/index/CROSSWALK.csv on the board.

| Element Name | Display Name | Type | Facet | Field | Group | Meaning |
|---|---|---|---|---|---|---|
| Participant_ID | Participant ID | Edm.String | No | Yes | Data table only | Participant identifier: the cohort prefix CASE- or CTRL- followed by the GUID. |
| GUID | GUID | Edm.String | No | Yes | Data table only | Global Unique Identifier. |
| Country | Country | Edm.String | No | Yes | Data table only | Participant Country. |
| Region | Region | Edm.String | No | Yes | Data table only | Participant State or Province. |
| HAS_GENOMICS | Genomic Data | Edm.String | Yes | Yes | OMIC Data | Is genomic data available. |
| Genomic_Sequencing_DNA_Source | Genomic Sequencing DNA Source | Edm.String | No | Yes | Data table only | DNA Source for genomic data sequencing. |
| GENOMICS_TIMEPOINTS_AVAILABLE | Genomics Timepoints Available | Edm.String | No | Yes | Data table only | Genomics sample timepoints available for the participant, comma-separated when there is more than one. |
| HAS_PROTEOMICS | Proteomic Data | Edm.String | Yes | Yes | OMIC Data | Is proteomic data available. |
| Proteomics_Sequencing_Source | Proteomics Sequencing Source | Edm.String | No | Yes | Data table only | Sample source for proteomics (the description says DNA, but it means source). |
| HAS_PROTEOMICS_TIMEPOINT | Proteomic Timepoints | Edm.String | No | Yes | Data table only | Available proteomics timepoints, comma-separated; declared and left empty (owner deferred). |
| HAS_TRANSCRIPTOMICS | Transcriptomic Data | Edm.String | Yes | Yes | OMIC Data | Is transcriptomic data available. |
| Transcriptomic_Sequencing_DNA_Source | Transcriptomic Sequencing DNA Source | Edm.String | No | Yes | Data table only | DNA Source for transcriptomic data sequencing. |
| HAS_TRANSCRIPTOMICS_TIMEPOINT | Transcriptomic Timepoints | Edm.String | No | Yes | Data table only | Available transcriptomics timepoints, comma-separated; declared and left empty (owner deferred). |
| TRANSCRIPTOMICS_TIMEPOINTS_AVAILABLE | Transcriptomics Timepoints Available | Edm.String | No | Yes | Data table only | Transcriptomics sample timepoints available for the participant, comma-separated when there is more than one. |
| RACE | Race | Edm.String | Yes | Yes | DEMOGRAPHICS | Race and ethnicity in one field (the ALS TDI Ethnicity column under the Answer ALS name). |
| AGE_AT_SYMPTOM_ONSET | Age At Symptom Onset | Edm.Int32 | Yes | Yes | CLINICAL INFORMATION | Participant age at symptom onset. |
| Age_At_Sign_Up | Age At Sign Up | Edm.Int32 | Yes | Yes | CLINICAL INFORMATION | Participant age at sign up. |
| Current_Age | Current Age | Edm.Int32 | No | Yes | Data table only | Participant age at the time of the current Neuromine release. |
| Sporadic_Familial | Sporadic vs Familial | Edm.String | Yes | Yes | DEMOGRAPHICS | Family history of ALS flag (the ALS TDI Family_with_Als column under the Answer ALS name). |
| SEX | Sex | Edm.String | Yes | Yes | DEMOGRAPHICS | Participant Sex. |
| SUBJECT_GROUP | Subject Group | Edm.String | Yes | Yes | DEMOGRAPHICS | Cohort category (see the vocabulary table). |
| Total_Blood_Draw | Total Blood Draws | Edm.Int32 | Yes | Yes | NUMBER OF TIMEPOINTS | Participant total blood draws conducted. |
| Total_ALSFRS | Total ALSFRS | Edm.Int32 | Yes | Yes | NUMBER OF TIMEPOINTS | Participant total ALSFRS-R questionnaires completed. |
| Total_Tracker | Total Accelerometer Sessions | Edm.Int32 | Yes | Yes | NUMBER OF TIMEPOINTS | Participant total accelerometer sessions completed. |
| Total_Voice_Recording | Total Voice Recordings | Edm.Int32 | Yes | Yes | NUMBER OF TIMEPOINTS | Participant total voice recordings submitted and scored. |
| Sign_Up_Date_Year | Sign Up Year | Edm.Int32 | No | Yes | Data table only | Participant Sign Up Year. |
| IS_DECEASED | Deceased | Edm.String | Yes | Yes | CLINICAL INFORMATION | Whether the participant is deceased. |
| Three_or_More_Data_Points | Participant has 3 or more data points contributed to any given task | Edm.String | Yes | Yes | NUMBER OF TIMEPOINTS | Whether the participant contributed 3 or more data points to any one task (ALSFRS-R entries, voice recordings or accelerometer sessions). |
| REVISED_EL_ESCORIAL_CRITERIA | Revised El Escorial Criteria | Edm.String | Yes | Yes | CLINICAL INFORMATION | Diagnosis based on the El Escorial criteria. |
| Site_of_Onset | Site of Onset | Edm.String | Yes | Yes | CLINICAL INFORMATION | Body site where the participant reports symptom onset; can list more than one site. |
| ALSFRS_R_PROGRESSION_SLOPE | ALSFRS-R Progression Slope | Edm.Double | Yes | Yes | CLINICAL INFORMATION | ALSFRS-R slope in points per month from simple linear regression. |
| EH_C9orf72 | C9orf72 Expansion Hunter | Edm.String | Yes | Yes | Expansion Hunter Data | Availability flag: C9orf72 Expansion Hunter data exists. |
| C9orf72_repeat_length | Repeat Length (C9) | Edm.Int32 | Yes | Yes | Expansion Hunter Data | Expansion Hunter C9orf72 repeat count, the higher of the two alleles (same as C9orf72_repeat_length_allele_2). |
| C9orf72_repeat_length_allele_1 | C9orf72 Allele 1 | Edm.Int32 | Yes | Yes | Expansion Hunter Data | Expansion Hunter C9orf72 repeat count of the lower allele. |
| C9orf72_repeat_length_allele_2 | C9orf72 Allele 2 | Edm.Int32 | Yes | Yes | Expansion Hunter Data | Expansion Hunter C9orf72 repeat count of the higher allele. |
| EH_ATXN2 | ATXN2 Expansion Hunter | Edm.String | Yes | Yes | Expansion Hunter Data | Availability flag: ATXN2 Expansion Hunter data exists. |
| ATXN2_repeat_length | Repeat Length (ATXN2) | Edm.Int32 | Yes | Yes | Expansion Hunter Data | Expansion Hunter ATXN2 repeat count, the higher of the two alleles (same as ATXN2_repeat_length_allele_2). |
| ATXN2_repeat_length_allele_1 | ATXN2 Allele 1 | Edm.Int32 | Yes | Yes | Expansion Hunter Data | Expansion Hunter ATXN2 repeat count of the lower allele. |
| ATXN2_repeat_length_allele_2 | ATXN2 Allele 2 | Edm.Int32 | Yes | Yes | Expansion Hunter Data | Expansion Hunter ATXN2 repeat count of the higher allele. |

## Fixed vocabularies

Taken from the Description text of the definition file only.

| Element Name | Categories named in the definition |
|---|---|
| SUBJECT_GROUP | ALS Patient, ALS Patient - Reversals, Asymptomatic Carrier, Healthy Volunteer |
| GENOMICS_TIMEPOINTS_AVAILABLE, TRANSCRIPTOMICS_TIMEPOINTS_AVAILABLE | Timepoint numbers as one comma-separated string, for example "1, 2" |
| HAS_PROTEOMICS_TIMEPOINT, HAS_TRANSCRIPTOMICS_TIMEPOINT | Same comma-separated form; both are empty in this release |
| Site_of_Onset | Free body-site text, more than one site allowed |

The other categorical columns (SEX, RACE, Sporadic_Familial, REVISED_EL_ESCORIAL_CRITERIA, the HAS_ and EH_ flags) have no categories in the definition file. Their known differences from Answer ALS are on index-shared-columns.md.

## Facet ranges

The Values column holds the edges of the ranges the portal slider uses, not a vocabulary.

| Element Name | Range edges in Values |
|---|---|
| AGE_AT_SYMPTOM_ONSET | 19, 29, 39, 49, 59, 69, 79 |
| Age_At_Sign_Up | 19, 29, 39, 49, 59, 69, 79 |
| Total_Blood_Draw | 2, 5, 9 |
| Total_ALSFRS | 10, 25, 50, 75, 100, 125, 150 |
| Total_Tracker | 5, 10, 25, 50, 75, 100 |
| Total_Voice_Recording | 5, 10, 25, 50, 75, 100, 125 |
| ALSFRS_R_PROGRESSION_SLOPE | -5, -3, -2, -1, 0, 1, 2 |
| C9orf72_repeat_length | 25, 50, 100, 200, 400, 800 |
| C9orf72_repeat_length_allele_1 | 4, 6, 8, 10 |
| C9orf72_repeat_length_allele_2 | 25, 50, 100, 200, 400, 800 |
| ATXN2_repeat_length | 24, 28, 32 |
| ATXN2_repeat_length_allele_1 | 18, 22, 23 |
| ATXN2_repeat_length_allele_2 | 24, 28, 32 |

## Source

als-tdi/index/r2.5/ALS_TDI_ElementsDefinition_r2.5.csv and ALS_TDI_HierarchyTree_r2.5.csv on the board.
