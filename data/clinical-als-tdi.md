# ALS TDI clinical package, Release 2: tables

The ALS TDI clinical package is one table per topic, delivered by ALS TDI as V2 workbooks and published as CSVs, plus a data dictionary. Release 2 has 18 tables (17 topic tables and the participant roster) plus the dictionary. This page is written from the dictionary that came with the delivery (TDI_data_dictionary.xlsx, published as TDI_data_dictionary.csv) and from the file names. It describes columns, never values.

## The dictionary

Columns: Form Name, Field Name, Values, Field Type, Additional Notes. Values holds codes and labels for the few coded fields, in the same "0, label / 1, label" form as the Answer ALS dictionary. Field Type is numeric or text.

The dictionary's Form Name is the file name without the _V2 suffix, with one spelling slip: TDI_ACTVITY in the dictionary is the TDI_ACTIVITY_V2 file. TDI_Participants_V2 has no dictionary rows.

## Rules that hold across tables

- Every table has Participant ID, the numeric ARC participant number. It is the join key inside the package.
- Dates are not calendar dates. Time is given as days since the participant signed up (columns named "... Days Since Sign Up") and, in some tables, days since symptom onset ("Days Since Onset").
- The participant table links the numeric Participant ID to the GUID column. In this package GUID holds the index Participant_ID form (CASE- or CTRL- plus the GUID), so the index joins to the package on index Participant_ID = package GUID.
- Diff two releases on Participant ID, never on GUID: one participant's GUID changed between Release 1 and Release 2.
- The survey tables are long: one row per answer, keyed by Question ID, Response ID and Answer ID, with the question text in Question Title (and Parent Question Title or Response Route when questions nest).

## Tables

Fields counts the dictionary rows for the table.

| File | What it collects | Fields | Key fields |
|---|---|---|---|
| TDI_ACTIVITY_V2 | At-home accelerometer sessions: average peak acceleration per limb task | 8 | Days Since Sign Up, Avg Actual LA, LW, RA, RW, RWLW, Avg Actual Total |
| TDI_ALSFRS-R_V2 | Self-reported ALSFRS-R items and total | 16 | Total Score, the twelve FRS item fields, Days Since Sign Up, Days Since Onset |
| TDI_CBC_CMP_V2 | Blood count and metabolic panel results with units in the field name | 45 | Days Since Sign Up, for example Creatinine (mg/dL), Platelet Count (10^3/mm3) |
| TDI_CLINICAL_TRIALS_V2 | Clinical trials the participant reports joining | 7 | NCT Number, Trial Name, Trial Joined and Stopped Date Days Since Sign Up |
| TDI_MEDICATIONS_V2 | Self-reported medications | 10 | Drug Name, Active Ingredient, Drug Dosage, Start and End Date Days Since Sign Up |
| TDI_OVERVIEW_V2 | One row per participant: type, diagnosis, onset, ages, demographics, C9orf72 status and task totals | 24 | Participant Type, Diagnosis, Onset Site Unnested, Onset Age, Age At Sign Up, Sex, Ethnicity, Family with Als, Deceased (Yes / No), C9orf72 Status Self Reported, C9orf72 Status TDI Reported, Total ALSFRS |
| TDI_Participants_V2 | Participant roster: numeric Participant ID, GUID and cohort | not in dictionary | Participant ID, GUID, Cohort |
| TDI_SUPPLEMENTS_V2 | Self-reported supplements | 12 | Supplement Product Name, Serving Size, Serving Size Unit, Start and End Date Days Since Sign Up |
| TDI_SURVEY_ALS_EXPERIENCE_V2 | ALS experience survey | 10 | Survey Title, Parent Question Title, Question Title, Response Route, Answer Value |
| TDI_SURVEY_CONDITIONS_V2 | Medical conditions survey | 8 | Question Title, Answer Value |
| TDI_SURVEY_FAMILYHX_V2 | Family history survey | 9 | Question Title, Response Route (links the answers about one relative), Answer Value |
| TDI_SURVEY_GENERAL_V2 | General health survey (for example height) | 9 | Parent Question Title, Question Title, Answer Value |
| TDI_SURVEY_GEOGRAPHY_V2 | Residence history survey | 10 | Question Title, Response Route (links the answers about one residence), Answer Value |
| TDI_SURVEY_HOSPITALIZATIONS_V2 | Hospitalizations survey | 8 | Question Title, Answer Value |
| TDI_SURVEY_INJURIES_V2 | Injuries survey | 8 | Question Title, Answer Value |
| TDI_SURVEY_LIFESTYLE_V2 | Lifestyle survey by age range | 10 | Parent Question Title, Question Title, Response Route (the age range), Answer Value |
| TDI_SURVEY_OCCUPATION_V2 | Job history survey | 10 | Question Title, Response Route (links the answers about one job), Answer Value |
| TDI_VOICE_SCORE_V2 | Voice recordings scored by the ALS TDI and Google speech algorithm | 4 | Score, Days Since Sign Up From Recording, Days Since Onset From Recording |

The published package also holds CHANGES.md (the cleaning actions applied) and als_tdi_participants.csv, a participant file in the Release 1 portal shape with Participant_ID, GUID, Case_Control, Sex and Cohort.

## Codes worth knowing

- TDI_OVERVIEW Participant Type: ALS Patient, Asymptomatic Carrier, Healthy Volunteer, ALS Patient - Reversals (people with an ALS diagnosis in the ALS Reversals program).
- TDI_OVERVIEW Diagnosis: definitive, probable, possible, suspected, healthy, asymptomatic.
- C9orf72 Status Self Reported means the participant said they tested positive for the C9orf72 repeat expansion at sign up; C9orf72 Status TDI Reported means ALS TDI confirmed it by testing.
- The ALSFRS-R items use the standard 0 to 4 scale, labels in the dictionary.

## What the dictionary does not cover

The Release 2 validation found 18 delivered clinical columns that have no dictionary row (ALS TDI to fix). Treat a column that is not in the dictionary as undocumented, not as an error in the file.

## Source

TDI_data_dictionary.xlsx from the Release 2 re-delivery (clinical_data_package), the file names of the published Release 2 package, and the ALS TDI curation decisions.
