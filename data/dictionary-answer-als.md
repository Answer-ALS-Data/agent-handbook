# Answer ALS clinical dictionary

Every field of the Answer ALS clinical forms, one table per form, generated from the clinical dictionary __Clinical_Dictionary_Sep_2026.csv (Release 8). The dictionary ships inside the clinical package and has one row per form column. Form Name is the CSV file name without .csv.

Columns: Field name is the column header in the form CSV. Label is the dictionary's New Field Label. Type is numeric or text. Coded values are the codes and labels for a coded field, as "code, label" pairs separated by a pipe, as the dictionary gives them. Coded fields are stored as the code. Text is written in ASCII (curly quotes and dashes become plain ones) and a # before a number is written as the word number, and a web link is replaced by the words (web link in the dictionary file).

Source: __Clinical_Dictionary_Sep_2026.csv. Written from the dictionary rows only, never from a data file.

The full dictionary passes 1,000 lines on one page, so it is split into one page per form group. This page lists every form, its field count (dictionary rows) and the page that holds its table.

## Parts

- dictionary-answer-als-assessments.md: Clinical assessments.
- dictionary-answer-als-history.md: Diagnosis, history and demographics.
- dictionary-answer-als-events-and-samples.md: Events, logs, labs and samples.

## Forms

| Form Name | Form label | Fields | Page |
|---|---|---|---|
| AALSDXFX | ALS Diagnosis | 28 | dictionary-answer-als-history.md |
| AALSHXFX | ALS History | 29 | dictionary-answer-als-history.md |
| ALS_CBS | ALS Cognitive Behavioral Screen | 81 | dictionary-answer-als-assessments.md |
| ALS_Gene_Mutations | Self-reported ALS Gene Mutations | 28 | dictionary-answer-als-history.md |
| ALSFRS_R | ALS Functional Rating Scale (Revised) | 28 | dictionary-answer-als-assessments.md |
| ANSASFD | ANSWER-ALS Subject Final Disposition | 9 | dictionary-answer-als-events-and-samples.md |
| ANSWER_ALS_Medications_Log | Medication Log | 15 | dictionary-answer-als-events-and-samples.md |
| ANSWER_ALS_MobileApp | Mobile App Form | 6 | dictionary-answer-als-events-and-samples.md |
| Ashworth_Spasticity_Scale | Ashworth Spasticity Scale | 14 | dictionary-answer-als-assessments.md |
| Auxiliary_Chemistry | Auxiliary Chemistry 2 | 31 | dictionary-answer-als-events-and-samples.md |
| Auxiliary_Chemistry_Labs | Auxiliary Chemistry 1 | 31 | dictionary-answer-als-events-and-samples.md |
| Cerebrospinal_Fluid | Cerebrospinal Fluid Collection Log | 30 | dictionary-answer-als-events-and-samples.md |
| CNS_Lability_Scale | Central Nervous System Lability Scale | 19 | dictionary-answer-als-assessments.md |
| Demographics | Demographics | 14 | dictionary-answer-als-history.md |
| Diaphragm_Pacing_System_Device | Diaphragm Pacing System Device Log | 7 | dictionary-answer-als-events-and-samples.md |
| DNA_Sample_Collection | DNA Sample Collection Log | 16 | dictionary-answer-als-events-and-samples.md |
| Environmental_Questionnaire | Environmental Questionnaire | 58 | dictionary-answer-als-history.md |
| Family_History_Log | Family History Log | 44 | dictionary-answer-als-history.md |
| Feeding_Tube_Placement | Feeding Tube Placement | 25 | dictionary-answer-als-events-and-samples.md |
| Grip_Strength_Testing | Grip Strength Testing | 19 | dictionary-answer-als-assessments.md |
| Hand_Held_Dynamometry | Hand Held Dynamometry | 134 | dictionary-answer-als-assessments.md |
| Medical_History | Medical History | 9 | dictionary-answer-als-history.md |
| Mortality | Mortality | 14 | dictionary-answer-als-events-and-samples.md |
| NEUROLOG | Neurological Disease Log | 22 | dictionary-answer-als-history.md |
| NIV_Log | Non-invasive Ventilation Log | 11 | dictionary-answer-als-events-and-samples.md |
| PBMC_Sample_Collection | PBMC Sample Collection Log | 11 | dictionary-answer-als-events-and-samples.md |
| Permanent_Assisted_Ventilation | Permanent Assisted Ventilation Log | 6 | dictionary-answer-als-events-and-samples.md |
| Plasma_Sample | Plasma Collection Log | 27 | dictionary-answer-als-events-and-samples.md |
| Reflexes | Reflexes | 67 | dictionary-answer-als-assessments.md |
| Serum_Sample | Serum Collection Log | 27 | dictionary-answer-als-events-and-samples.md |
| subjects | Study Disease Group Assignment | 3 | dictionary-answer-als-history.md |
| Tracheostomy | Tracheostomy | 10 | dictionary-answer-als-events-and-samples.md |
| Vital_Capacity | Vital Capacity | 38 | dictionary-answer-als-assessments.md |
| Vital_Signs | Vital Signs | 25 | dictionary-answer-als-assessments.md |
