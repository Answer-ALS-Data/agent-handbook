# Index columns shared by Answer ALS and ALS TDI

25 ALS TDI index columns have an Answer ALS Release 8 counterpart. In ALS TDI Release 2.5 they carry the Answer ALS name; in Release 2 (still the staged index) they carry the ALS TDI name. A shared name does not mean shared values: only names were changed, no value was recoded. This page tells you which columns you can put side by side and which need a recode first.

Compare means:

- Yes: same meaning and the same vocabulary or unit.
- After recode: same meaning, but labels or case differ; map the labels first.
- With care: same meaning and unit, but measured or derived differently.
- No: the two columns hold different things under one name.

| ALS TDI r2 name | Name in r2.5 and Answer ALS r8 | Match | Compare | Why |
|---|---|---|---|---|
| Participant_ID | Participant_ID | exact | No | Join key only. Both are prefix plus GUID; the two cohorts are different people. |
| GUID | GUID | exact | No | Join key only. |
| HAS_GENOMICS | HAS_GENOMICS | exact | Yes | Yes or blank in both. |
| GENOMICS_DNA_SOURCE | Genomic_Sequencing_DNA_Source | same-meaning | Yes | Both use Blood. |
| HAS_PROTEOMICS | HAS_PROTEOMICS | exact | Yes | Yes or blank in both. |
| PROTEOMICS_DNA_SOURCE | Proteomics_Sequencing_Source | same-meaning | No | ALS TDI proteomics come from blood, Answer ALS from iPSC derived motor neuron lines. The ALS TDI name says DNA but means sample source. |
| HAS_TRANSCRIPTOMICS | HAS_TRANSCRIPTOMICS | exact | Yes | Yes or blank in both. |
| TRANSCRIPTOMICS_DNA_SOURCE | Transcriptomic_Sequencing_DNA_Source | same-meaning | No | ALS TDI is blood, Answer ALS is iPSC derived motor neuron lines. |
| Ethnicity | RACE | partial | No | ALS TDI mixes race and ethnicity in one field (Caucasian/White, Hispanic, African American/Black, Middle Eastern and others). Answer ALS splits RACE (White, Black/African American, Asian, comma combinations) from ETHNIC_CATEGORY. |
| Onset_Age | AGE_AT_SYMPTOM_ONSET | same-meaning | Yes | Age in years at symptom onset. The portal range edges differ. |
| Family_with_Als | Sporadic_Familial | partial | No | ALS TDI is a TRUE/FALSE family history flag for everyone. Answer ALS is a derived Sporadic/Familial/Unknown class for ALS subjects only. |
| Sex | SEX | same-meaning | After recode | ALS TDI: male, female, other, prefer not to say (lower case). Answer ALS: Male, Female. |
| Participant_Type | SUBJECT_GROUP | same-meaning | After recode | ALS TDI: ALS Patient, ALS Reversal, Asymptomatic Carrier, Healthy Volunteer. Answer ALS: ALS, Non-ALS MND, Asymptomatic ALS Gene carrier, Healthy Control. |
| Deceased | IS_DECEASED | same-meaning | Yes | Yes/No in both. |
| Diagnosis | REVISED_EL_ESCORIAL_CRITERIA | same-meaning | After recode | ALS TDI: definitive, probable, possible, suspected, lab-supported_probable, healthy, asymptomatic, in mixed case. Answer ALS: Definite, Probable, Possible, Suspected. |
| Site_of_Onset | Site_of_Onset | exact | No | Same name, different content. ALS TDI holds body parts and comma lists (Tongue, Right Hand, Left Leg, Right Leg). Answer ALS holds Limb, Bulbar, Axial, Multiple, Other. |
| ALSFRS_Slope | ALSFRS_R_PROGRESSION_SLOPE | same-meaning | With care | Both points per month. ALS TDI uses simple linear regression; Answer ALS is calculated by NeuroBank from baseline and latest scores. |
| Has_EH_C9orf72 | EH_C9orf72 | same-meaning | After recode | Availability flag. ALS TDI: Yes or blank. Answer ALS: Yes or No. |
| EH_C9orf72 | C9orf72_repeat_length | same-meaning | Yes | Repeat count of the higher allele. |
| EH_C9orf72_allele_1 | C9orf72_repeat_length_allele_1 | same-meaning | Yes | Lower allele repeat count. |
| EH_C9orf72_allele_2 | C9orf72_repeat_length_allele_2 | same-meaning | Yes | Higher allele repeat count. |
| Has_EH_ATXN2 | EH_ATXN2 | same-meaning | After recode | Availability flag. ALS TDI: Yes or blank. Answer ALS: Yes or No. |
| EH_ATXN2 | ATXN2_repeat_length | same-meaning | Yes | Repeat count of the higher allele. |
| EH_ATXN2_allele_1 | ATXN2_repeat_length_allele_1 | same-meaning | Yes | Lower allele repeat count. |
| EH_ATXN2_allele_2 | ATXN2_repeat_length_allele_2 | same-meaning | Yes | Higher allele repeat count. |

## The EH name trap

In ALS TDI Release 2, EH_C9orf72 and EH_ATXN2 are repeat lengths and Has_EH_C9orf72 / Has_EH_ATXN2 are the availability flags. In Answer ALS, and in ALS TDI Release 2.5, EH_C9orf72 and EH_ATXN2 are the availability flags. So EH_C9orf72 means a different column depending on which ALS TDI release you hold. Check the release before you read an EH column.

## Columns with no counterpart

The other 14 ALS TDI columns have no Answer ALS match and keep their ALS TDI name: Country, Region, GENOMICS_TIMEPOINTS_AVAILABLE, HAS_PROTEOMICS_TIMEPOINT, HAS_TRANSCRIPTOMICS_TIMEPOINT, TRANSCRIPTOMICS_TIMEPOINTS_AVAILABLE, Age_At_Sign_Up, Current_Age, Total_Blood_Draw, Total_ALSFRS, Total_Tracker, Total_Voice_Recording, Sign_Up_Date_Year and Three_or_More_Data_Points. Total_Blood_Draw counts blood draws and is not the same as Answer ALS Number_of_Visits, which counts clinic visits.

## Source

als-tdi/index/CROSSWALK.csv (names and match type) and als-tdi/index/NOTES.md (vocabulary differences) on the board.
