# Answer ALS index, Release 8: columns

The Answer ALS release index has one row per participant and one column per element below. It ships as three files that are versioned together: ReleaseIndex_r8.csv (the rows), ElementsDefinition_r8.csv (one row per column) and HierarchyTree_r8.csv (how the portal groups the facets). This page is written from the last two only. It describes columns, never values.

How to read the table:

- Element Name: the column header in the index.
- Display Name: the label on the portal. (blank) means the definition file leaves it empty.
- Type: the portal data type. Edm.String is text, Edm.Int32 a whole number, Edm.Double a decimal.
- Facet: Yes means the column is a filter on the portal search page.
- Field: Yes means the column shows in the portal data table.
- Group: the facet group from the HierarchyTree. "Data table only" means the column is not a leaf of the tree.
- Meaning: the definition file's Description, cut to one sentence.

| Element Name | Display Name | Type | Facet | Field | Group | Meaning |
|---|---|---|---|---|---|---|
| Participant_ID | Participant ID | Edm.String | No | Yes | Data table only | Answer ALS identifier: the cohort prefix CASE- or CTRL- followed by the GUID. |
| GUID | GUID | Edm.String | No | Yes | Data table only | Global Unique Identifier. |
| NYGC_CGND_ID | NYGC CGND ID | Edm.String | No | Yes | Data table only | New York Genome Center sample ID (CGND, Center for Genomics of Neurodegenerative Disease). |
| HAS_GENOMICS | Genomics | Edm.String | Yes | No | OMICS | Whole Genome Sequence Data is available. |
| HAS_EPIGENOMICS | Epigenomics | Edm.String | Yes | No | OMICS | Epigenomics Data is available. |
| HAS_TRANSCRIPTOMICS | Transcriptomics | Edm.String | Yes | No | OMICS | Transcriptomics Data is available. |
| HAS_SPLICING | Splicing | Edm.String | Yes | No | OMICS | Splicing Data is available. |
| HAS_QTL | QTL | Edm.String | Yes | No | OMICS | QTL Data is available. |
| HAS_PROTEOMICS | Proteomics | Edm.String | Yes | No | OMICS | Proteomics data is available. |
| HAS_NFL | NfL Data | Edm.String | Yes | Yes | External Data | Whether the participant has neurofilament light chain (NfL) data or not (Source: Serum). |
| NFL_TIMEPOINTS_AVAILABLE | NfL Timepoints Available | Edm.String | No | Yes | Data table only | The NfL timepoints available for the participant. |
| HAS_SOMASCAN | SomaScan Data | Edm.String | Yes | Yes | External Data | Whether the participant has SomaScan Proteomics data or not (Source: Plasma). |
| SOMASCAN_TIMEPOINTS_AVAILABLE | SomaScan Timepoints Available | Edm.String | No | Yes | Data table only | The SomaScan timepoints available for the participant. |
| Number_of_Visits | Number of Visits | Edm.Int32 | Yes | Yes | DISEASE STATUS | Number of clinical visits; longitudinal data was collected every 3 to 6 months. |
| SEX | Sex | Edm.String | Yes | Yes | DEMOGRAPHICS | Sex at birth, if known (see the vocabulary table). |
| estimated_sex | Estimated Sex | Edm.String | No | Yes | Data table only | Sex of the sample as inferred from both expression of Y-chromosomal genes and presence of regions of open chromatin on the Y chromosome. |
| ETHNIC_CATEGORY | Ethnicity | Edm.String | Yes | Yes | DEMOGRAPHICS | Ethnicity in three categories (see the vocabulary table). |
| RACE | Race | Edm.String | Yes | Yes | DEMOGRAPHICS | Race in five categories (see the vocabulary table). |
| SUBJECT_GROUP | Subject Group | Edm.String | Yes | Yes | DISEASE STATUS | Subject group in four categories (see the vocabulary table). |
| Sporadic_Familial | Sporadic vs Familial | Edm.String | Yes | Yes | DISEASE STATUS | Sporadic, Familial or Unknown class of an ALS diagnosis, derived from the Family History Log and the ALS Gene Mutations form; ALS subjects only. |
| SUBJECT_SUBGROUP | PLS Subgroup | Edm.String | Yes | Yes | DISEASE STATUS | A subcategory of Non-ALS Motor Neuron Disease (MND). |
| External_Control | External Control | Edm.String | Yes | Yes | DISEASE STATUS | Yes if the participant is an external control, No if internal; a subset of Healthy Control. |
| REVISED_EL_ESCORIAL_CRITERIA | Revised El Escorial Criteria | Edm.String | Yes | Yes | DISEASE STATUS | Revised El Escorial category used to diagnose ALS (see the vocabulary table). |
| Site_of_Onset | Site of Onset | Edm.String | Yes | Yes | DISEASE STATUS | Site of disease onset (see the vocabulary table). |
| Bulbar_Onset | Bulbar | Edm.String | Yes | Yes | Data table only | Whether onset was bulbar. |
| Axial_Onset | Axial | Edm.String | Yes | Yes | Data table only | Whether onset was axial. |
| Limb_Onset | Limb | Edm.String | Yes | Yes | Data table only | Whether onset was in a limb. |
| Other_Onset | Other | Edm.String | Yes | Yes | Data table only | Whether onset was somewhere other than bulbar, axial or limb. |
| AGE_AT_SYMPTOM_ONSET | Age At Symptom Onset | Edm.Int32 | Yes | Yes | DISEASE STATUS | Patient age (in years) at the time of symptom onset as defined by weakness or spasticity. |
| AGE_AT_DEATH | Age At Death | Edm.Int32 | No | Yes | Data table only | Age at death in years. |
| IS_DECEASED | Deceased | Edm.String | Yes | No | DISEASE STATUS | Indicates if the participant is deceased. |
| ALSFRS_R_Baseline_Value | ALSFRS-R Baseline | Edm.Int32 | No | Yes | Data table only | ALSFRS-R total score at the first medical visit. |
| ALSFRS_R_Latest_Value | ALSFRS-R Latest | Edm.Int32 | No | Yes | Data table only | ALSFRS-R total score at the most recent medical visit. |
| ALSFRS_R_PROGRESSION_SLOPE | ALSFRS-R Progression Slope | Edm.Double | Yes | Yes | DISEASE STATUS | ALSFRS-R progression in points per month, calculated by NeuroBank. |
| CBS_Baseline_Value | CBS Baseline | Edm.Int32 | No | Yes | Data table only | ALS Cognitive Behavioral Screen (CBS) score at the first medical visit. |
| CBS_Latest_Value | CBS Latest | Edm.Int32 | No | Yes | Data table only | ALS Cognitive Behavioral Screen (CBS) score at the most recent medical visit. |
| COGNITIVE_PROGRESSION_SLOPE | CBS Progression | Edm.Double | Yes | Yes | DISEASE STATUS | CBS progression in points per month, calculated by NeuroBank. |
| HasIPSC | iPSC | Edm.String | Yes | Yes | CELL LINES | Yes when an iPSC line exists for the participant (iPSCLine holds a line name); does not mean the line can be bought. |
| IPSC_For_Sale | iPSC Line For Sale | Edm.String | Yes | Yes | CELL LINES | Whether the participant's iPSC line is listed for sale in the Cedars-Sinai Biomanufacturing Center catalog under the Answer ALS project. |
| HasDIMN | diMNs | Edm.String | Yes | Yes | CELL LINES | Whether a diMN line was used to generate the omics data. |
| DIMN_For_Sale | diMN Line For Sale | Edm.String | Yes | Yes | CELL LINES | Whether the participant's Day 12 diMN line is listed for sale in the Cedars-Sinai Biomanufacturing Center catalog. |
| root_iPSC_Line | iPSC Root Line | Edm.String | No | Yes | Data table only | iPSC line name without the clone number, used to order the line from Cedars-Sinai or CIRM. |
| iPSCLine | iPSC Line Name | Edm.String | No | Yes | Data table only | iPSC line, with clone, used to make the motor neuron (diMN) line. |
| iPSCLine_Source | iPSC Line Source | Edm.String | No | Yes | Data table only | Where the iPSC line came from (see the vocabulary table). |
| diMNs_line | diMNs Line Name | Edm.String | No | Yes | Data table only | diMN line used to generate the omics data. |
| Primary_Tissue | Primary Tissue | Edm.String | No | Yes | Data table only | Tissue the cell line was derived from, from a controlled vocabulary. |
| Batch | Batch ID | Edm.String | No | Yes | Data table only | The diMN cell culture differentiation batch used for tracking lines to OMIC centers. |
| PCT_SMI32 | NEFH (SMI32) | Edm.Double | No | Yes | Data table only | diMN differentiation QC marker: percent of DAPI positive cells positive for NEFH (SMI32). |
| PCT_ISL1 | ISL1 | Edm.Double | No | Yes | Data table only | diMN differentiation QC marker: percent of DAPI positive cells positive for ISL1. |
| PCT_NKX61 | NKX6.1 | Edm.Double | No | Yes | Data table only | diMN differentiation QC marker: percent of DAPI positive cells positive for NKX6.1. |
| PCT_TUJ1 | TUBB3 (TuJ1) | Edm.Double | No | Yes | Data table only | diMN differentiation QC marker: percent of DAPI positive cells positive for TUBB3 (TuJ1). |
| PCT_S100b | s100b | Edm.Double | No | Yes | Data table only | diMN differentiation QC marker: percent of DAPI positive cells positive for s100b. |
| PCT_Nestin | Nestin | Edm.Double | No | Yes | Data table only | diMN differentiation QC marker: percent of DAPI positive cells positive for Nestin. |
| Staining_Details | Staining Notes | Edm.String | No | Yes | Data table only | Staining notes from the Cedars-Sinai Biomanufacturing Center. |
| Age_at_First_PBMC_Collection | Age at First PBMC Sample Collection | Edm.Int32 | No | Yes | Data table only | The age of the participant at the time of the first PBMC sample collection. |
| ClinReport_Mutations_Details | Self-reported Mutations | Edm.String | Yes | Yes | MUTATIONS | Mutations reported by the participant, family or physician during the health history. |
| HasVariant | WGS Variants | Edm.String | Yes | Yes | MUTATIONS | Genes in which whole genome sequencing found a SNP; whether the SNP relates to disease is not known. |
| EH_C9orf72 | (blank) | Edm.String | No | No | Data table only | Availability flag: Expansion Hunter data exists for C9orf72. |
| EH_ATXN2 | (blank) | Edm.String | No | No | Data table only | Availability flag: Expansion Hunter data exists for ATXN2. |
| C9orf72_repeat_length | Repeat Length (C9) | Edm.Int32 | Yes | No | MUTATIONS | Expansion Hunter C9orf72 repeat count, the higher of the two alleles (same as C9orf72_repeat_length_allele_2). |
| ATXN2_repeat_length | Repeat Length (ATXN2) | Edm.Int32 | Yes | No | MUTATIONS | Expansion Hunter ATXN2 repeat count, the higher of the two alleles (same as ATXN2_repeat_length_allele_2). |
| C9orf72_repeat_length_allele_1 | C9orf72 Allele 1 | Edm.Int32 | No | Yes | Data table only | Expansion Hunter C9orf72 repeat count of the lower allele. |
| C9orf72_repeat_length_allele_2 | C9orf72 Allele 2 | Edm.Int32 | No | Yes | Data table only | Expansion Hunter C9orf72 repeat count of the higher allele. |
| ATXN2_repeat_length_allele_1 | ATXN2 Allele 1 | Edm.Int32 | No | Yes | Data table only | Expansion Hunter ATXN2 repeat count of the lower allele. |
| ATXN2_repeat_length_allele_2 | ATXN2 Allele 2 | Edm.Int32 | No | Yes | Data table only | Expansion Hunter ATXN2 repeat count of the higher allele. |
| has_discordant_sample | Sample Discordance | Edm.String | No | Yes | Data table only | Whether the sample was part of a label discordance event in the MIT (April 2025) WGS vs ATAC-seq vs RNA-seq genotype concordance analysis. |
| Genomic_Sequencing_DNA_Source | Genomic Sequencing DNA Source | Edm.String | Yes | Yes | Assay and Metadata | Source of the DNA used for genome sequencing (see the vocabulary table). |
| WGS_Sequencing_Protocol_Used | WGS Library Preparation Used | Edm.String | Yes | Yes | Assay and Metadata | WGS library preparation used (see the vocabulary table). |
| Epigenomic_Sequencing_DNA_Source | Epigenomics Sequencing DNA Source | Edm.String | Yes | Yes | Assay and Metadata | Indicates the source of the Epigenomics Sequencing DNA. |
| Transcriptomic_Sequencing_DNA_Source | Transcriptomic Sequencing DNA Source | Edm.String | Yes | Yes | Assay and Metadata | Indicates the source of the Transcriptomic Sequencing DNA. |
| RIN_Value | RIN Value | Edm.Double | Yes | Yes | Assay and Metadata | RNA integrity number (RIN) value. |
| Proteomics_Sequencing_Source | Proteomics Sequencing Source | Edm.String | Yes | Yes | Assay and Metadata | Indicates the source of the Proteomics Sequencing. |
| Proteomic_Instrument | Proteomics Instrument Used | Edm.String | Yes | Yes | Assay and Metadata | Instrument used for proteomics processing. |
| Proteomic_Digestion_Batch | Digestion Batch | Edm.String | Yes | Yes | Assay and Metadata | Proteomics digestion batches. |

## Fixed vocabularies

Taken from the Description text of the definition file. These are the categories the definitions name; check the release notes before you rely on the exact spelling or case.

| Element Name | Categories named in the definition |
|---|---|
| SEX | Male, Female (sex at birth, if known) |
| ETHNIC_CATEGORY | Hispanic or Latino, Not Hispanic or Latino, Unknown |
| RACE | American Indian or Alaska Native, Asian, Black or African American, Native Hawaiian or Other Pacific Islander, White |
| SUBJECT_GROUP | ALS, Non-ALS Motor Neuron Disease (MND), Asymptomatic ALS gene carrier, Healthy Control |
| SUBJECT_SUBGROUP | Subcategories of Non-ALS MND (the display name says PLS) |
| Sporadic_Familial | Sporadic, Familial, Unknown (ALS subjects only) |
| External_Control | Yes (external), No (internal) |
| REVISED_EL_ESCORIAL_CRITERIA | Suspected, Possible, Probable, Probable Lab-Supported, Definite |
| Site_of_Onset | Limb, Bulbar, Axial, Multiple (the HierarchyTree text gives these as examples) |
| iPSCLine_Source | CIRM, Cedars-Sinai Biomanufacturing Center |
| IPSC_For_Sale | Always No for CIRM-derived lines, which are not in the Cedars-Sinai catalog |
| Genomic_Sequencing_DNA_Source | Blood, iPSC |
| WGS_Sequencing_Protocol_Used | TruSeq PCR-Free, TruSeq Nano (PCR dependent) |

The HAS_ columns, IS_DECEASED, the onset flags and the For_Sale flags are availability or yes/no flags. Their exact codes (Yes/No or Yes/blank) are not written in the definition file; see index-shared-columns.md for what the board has recorded.

## Facet ranges

The Values column of the definition file does not hold a vocabulary. For numeric facets it holds the edges of the ranges the portal slider uses.

| Element Name | Range edges in Values |
|---|---|
| Number_of_Visits | 2, 4, 6, 8, 10, 11 |
| AGE_AT_SYMPTOM_ONSET | 6, 16, 26, 36, 46, 56, 66, 76, 86, 96 |
| ALSFRS_R_PROGRESSION_SLOPE | -4.5, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5 |
| COGNITIVE_PROGRESSION_SLOPE | -1.5, -0.5, 0.5, 1.5, 2.5 |
| C9orf72_repeat_length | 25, 50, 100, 200, 400, 800 |
| ATXN2_repeat_length | 24, 28, 32 |
| C9orf72_repeat_length_allele_1 | 4, 6, 8, 10 |
| C9orf72_repeat_length_allele_2 | 25, 50, 100, 200, 400, 800 |
| ATXN2_repeat_length_allele_1 | 18, 22, 23 |
| ATXN2_repeat_length_allele_2 | 24, 28, 32 |
| RIN_Value | 8.6, 9.2, 9.6, 9.8 |

## Source

answer-als/index/r8/ElementsDefinition_r8.csv and HierarchyTree_r8.csv on the board, the r8.3 schema files.
