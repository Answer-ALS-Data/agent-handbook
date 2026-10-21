# ALS TDI clinical dictionary

Every field of the ALS TDI clinical tables, one table per form, generated from the data dictionary that came with the Release 2 delivery, TDI_data_dictionary.xlsx (published as TDI_data_dictionary.csv). Form names are as the dictionary gives them: the file name without the _V2 suffix, and TDI_ACTVITY is the TDI_ACTIVITY_V2 file. A table with no dictionary rows is not listed.

Columns: Field name is the column header in the table. Label is the dictionary's Additional Notes column, blank where the dictionary has none. Type is numeric or text. Coded values are the codes and labels for a coded field, as the dictionary gives them. Text is written in ASCII (curly quotes and dashes become plain ones) and a # before a number is written as the word number, and a web link is replaced by the words (web link in the dictionary file).

Source: TDI_data_dictionary.xlsx. Written from the dictionary rows only, never from a data file.

## TDI_ACTVITY

Fields: 8.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| Days Since Sign Up |  | numeric |  |
| Avg Actual LA | Average peak acceleration vector magnitude of Left Ankle (LA) while doing seated left leg extension movements | numeric |  |
| Avg Actual LW | Average peak acceleration vector magnitude of Left Wrist (LW) while doing seated left arm raises | numeric |  |
| Avg Actual RA | Average peak acceleration vector magnitude of Right Ankle (RA) while doing seated right leg extension movements | numeric |  |
| Avg Actual RW | Average peak acceleration vector magnitude of Right Wrist (LW) while doing seated right arm raises | numeric |  |
| Avg Actual RWLW | Average peak acceleration vector magnitude of Right and Left Wrist (RWLW) while doing seated toe touches | numeric |  |
| Avg Actual Total | Average peak acceleration vector magnitude of all limbs | numeric |  |

## TDI_ALSFRS-R

Fields: 16.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| Days Since Sign Up |  | numeric |  |
| Days Since Onset |  | numeric |  |
| Frs Climbing Stairs |  | numeric | 0, Cannot do \| 1, Needs assistance \| 2, Mild unsteadiness or fatigue \| 3, Slow \| 4, Normal |
| FRS Cutting Food |  | numeric | 0, Needs to be fed \| 1, Food must be cut by someone, but can still feed slowly \| 2, Can cut most foods, although clumsy and slow some help needed \| 3, Somewhat slow and clumsy, but no help needed \| 4, Normal |
| FRS Dressing Hygiene |  | numeric | 0, Total dependence \| 1, Needs attendant for self-care \| 2, Intermittent assistance or substitute methods \| 3, Independent and complete self-care with effort or decreased efficiency \| 4, Normal function |
| FRS Dyspnea |  | numeric | 0, Significant difficulty, considering using mechanical respiratory support \| 1, Occurs at rest, difficulty breathing when either sitting or lying \| 2, Occurs with one or more of the following: eating, bathing, dressing \| 3, Occurs when walking \| 4, None |
| FRS Handwriting |  | numeric | 0, Unable to grip pen \| 1, Able to grip pen but unable to write \| 2, Not all words are legible \| 3, Slow or sloppy all words are legible \| 4, Normal |
| FRS Orthopnea |  | numeric | 0, Unable to sleep without mechanical assistance \| 1, Can only sleep sitting up \| 2, Needs extra pillow in order to sleep (more than two) \| 3, Some difficulty sleeping at night due to shortness of breath, does not routinely use more than two pillows \| 4, None |
| FRS Respiratory Insufficiency |  | numeric | 0, Invasive mechanical ventilation by intubation or tracheostomy \| 1, Continuous use of NIPPV during the night and day \| 2, Continuous use of NIPPV during the night \| 3, Intermittent use of NIPPV \| 4, None |
| FRS Salivation |  | numeric | 0, Marked drooling requires constant tissue or handkerchief \| 1, Marked excess of saliva with some drooling \| 2, Moderately excessive saliva may have minimal drooling \| 3, Slight but definite excess of saliva in mouth may have nighttime drooling \| 4, Normal |
| FRS Speech |  | numeric | 0, Loss of useful speech \| 1, Speech combined with nonvocal communication \| 2, Intelligible with repeating \| 3, Detectable speech disturbances \| 4, Normal speech processes |
| FRS Swallowing |  | numeric | 0, NPO (exclusively parenteral or enteral feeding) \| 1, Needs supplemental tube feeding \| 2, Dietary consistency changes \| 3, Early eating problems - occasional choking \| 4, Normal eating habits |
| FRS Turning in Bed |  | numeric | 0, Helpless \| 1, Can initiate, but not turn or adjust sheets alone \| 2, Can turn alone or adjust sheets, but with great difficulty \| 3, Somewhat slow and clumsy, but no help needed \| 4, Normal |
| FRS Walking |  | numeric | 0, No purposeful leg movement \| 1, Nonambulatory functional movement only \| 2, Walks with assistance \| 3, Early ambulation difficulties \| 4, Normal |
| Total Score |  | numeric |  |

## TDI_CBC_CMP

Fields: 45.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| Days Since Onset |  | numeric |  |
| Days Since Sign Up |  | numeric |  |
| A/G Ratio |  | numeric |  |
| Albumin (g/dL) |  | numeric |  |
| Alkaline Phosphatase (U/L) |  | numeric |  |
| Basophils (%) |  | numeric |  |
| Basophils Abs (10^3/mm3) |  | numeric |  |
| Bilirubin Total (mg/dL) |  | numeric |  |
| BUN (mg/dL) |  | numeric |  |
| BUN/Creatinine Ratio |  | numeric |  |
| Calcium (mg/dL) |  | numeric |  |
| Chloride (MM01/L) |  | numeric |  |
| CO2 (MM01/L) |  | numeric |  |
| Creatinine (mg/dL) |  | numeric |  |
| EGFR (mL/min/1.3 sq m) |  | numeric |  |
| Eosinophils (%) |  | numeric |  |
| Eosinophils Abs (10^3/mm3) |  | numeric |  |
| Globulin (g/dL) |  | numeric |  |
| Glucose (mg/dL) |  | numeric |  |
| Hemoglobin (%) |  | numeric |  |
| Hematocrit (%) |  | numeric |  |
| IMM Grans (%) |  | numeric |  |
| IMM Grans Abs (10^3/mm3) |  | numeric |  |
| Lymphocytes (%) |  | numeric |  |
| Lymphocytes Abs (10^3/mm3) |  | numeric |  |
| MCH (PB) |  | numeric |  |
| MCHC (%) |  | numeric |  |
| MCV (FL) |  | numeric |  |
| Mean Platelet Volume (fL) |  | numeric |  |
| Monocytes (%) |  | numeric |  |
| Monocytes Abs (10^3/mm3) |  | numeric |  |
| Neutrophils (%) |  | numeric |  |
| Neutrophils Abs (10^3/mm3) |  | numeric |  |
| Nucleated RBC ()/WBC |  | numeric |  |
| Nucleated RBC Abs (10^3/mm3) |  | numeric |  |
| Platelet Count (10^3/mm3) |  | numeric |  |
| Potassium (MM01/L) |  | numeric |  |
| RDW (%) |  | numeric |  |
| Red Blood Cell Count (10^6/mm3) |  | numeric |  |
| SGOT (AST) (U/L) |  | numeric |  |
| SGPT (ALT) (U/L) |  | numeric |  |
| Sodium (MM01/L) |  | numeric |  |
| Total Protein (g/dL) |  | numeric |  |
| White Blood Cell Count (10^3/mm3) |  | numeric |  |

## TDI_CLINICAL_TRIALS

Fields: 7.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| NCT Number |  | text |  |
| Date Reported Days Since Sign Up |  | numeric |  |
| Trial Joined Date Days Since Sign Up |  | numeric |  |
| Trial Stopped Date Days Since Sign Up |  | numeric |  |
| Trial Name |  | text |  |
| Trial Link |  | text |  |

## TDI_MEDICATIONS

Fields: 10.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| Entry Days Since Sign Up | Day since sign up to when the information was reported | numeric |  |
| Drug Name |  | text |  |
| Start Date Days Since Sign Up | optional field, approx start date of medication | numeric |  |
| End Date Days Since Sign Up | optional field, approx end date of medication | numeric |  |
| Drug Dosage |  | text |  |
| Drug Form |  | text |  |
| Active Ingredient |  | text |  |
| Custom Dosage |  | text |  |
| Custom Form |  | text |  |

## TDI_OVERVIEW

Fields: 24.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| Participant Type |  | text | ALS Patient, Asymptomatic Carrier, Healthy Volunteer, ALS Patient - Reversals (patients received ALS dx and are included in Dr. Richard Bedlack's ALS Reversals program (web link in the dictionary file)) |
| Deceased (Yes / No) |  | text |  |
| Deceased Date Days Since Sign Up |  | numeric |  |
| Diagnosis |  | text | definitive, probable, possible, suspected, healthy, asymptomatic |
| Onset Site Unnested |  | text |  |
| Onset Date Days Since Sign Up |  | numeric |  |
| Formal Diagnosis Date Days Since Sign Up |  | numeric |  |
| Possible Diagnosis Date Days Since Sign Up |  | numeric |  |
| Age At Sign Up |  | numeric |  |
| Age At Death |  | numeric |  |
| Onset Age |  | numeric |  |
| C9orf72 Status Self Reported (Yes / No) | patient joined the study saying they've tested positive for C9 HRE. | text |  |
| C9orf72 Status TDI Reported | ALSTDI has confirmed with testing that patient has C9HRE | text |  |
| Country |  | text |  |
| Ethnicity |  | text |  |
| Family with Als |  | text |  |
| Region |  | text |  |
| Sex |  | text |  |
| Has Genomic Data (Yes / No) |  | text |  |
| Total ALSFRS |  | numeric |  |
| Total Blood Draw |  | numeric |  |
| Total Tracker |  | numeric |  |
| Total Voice Recording |  | numeric |  |

## TDI_SUPPLEMENTS

Fields: 12.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| Start Date Days Since Sign Up |  | numeric |  |
| End Date Days Since Sign Up |  | numeric |  |
| Custom Serving Size |  | numeric |  |
| Custom Serving Size Unit |  | text |  |
| Serving Size |  | numeric |  |
| Serving Size Unit |  | text |  |
| Supplement Assignment Frequency |  | numeric |  |
| Supplement Brand Name |  | text |  |
| Supplement Net Content Unit |  | text |  |
| Supplement Net Contents |  | numeric |  |
| Supplement Product Name |  | text |  |

## TDI_SURVEY_ALS_EXPERIENCE

Fields: 10.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| Question ID | ID associated with the Question | numeric |  |
| Response ID | ID associated with the Response | numeric |  |
| Answer ID | ID associated with the Answer | numeric |  |
| Date Submitted Date Days Since Sign Up |  | numeric |  |
| Survey Title | Overarching survey title | text |  |
| Parent Question Title | Title of top-level question, if subquestions are present (e.g, Since you developed ALS, have you had any of the following?) | text |  |
| Question Title | Title of top-level question if no subquestions are preset or title of subquestion (e.g., Pneumonia that required treatment with prescription medication) | text |  |
| Response Route | Title of third-level subquestion (e.g., Scattered muscle twitching?) | text |  |
| Answer Value | Participant's Response to above link of questions | text |  |

## TDI_SURVEY_CONDITIONS

Fields: 8.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| Question ID | ID associated with the Question | numeric |  |
| Response ID | ID associated with the Response | numeric |  |
| Answer ID | ID associated with the Answer | numeric |  |
| Date Submitted Date Days Since Sign Up |  | numeric |  |
| Survey Title | Overarching survey title | text |  |
| Question Title | Title of question, no subquestions present | text |  |
| Answer Value |  | text |  |

## TDI_SURVEY_FAMILYHX

Fields: 9.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| Question ID | ID associated with the Question | numeric |  |
| Response ID | ID associated with the Response | numeric |  |
| Answer ID | ID associated with the Answer | numeric |  |
| Date Submitted Date Days Since Sign Up |  | numeric |  |
| Survey Title | Overarching survey title | text |  |
| Question Title | Title of top-level question (e.g., Relation) | text |  |
| Response Route | Number that links questions and answers (e.g., All questions with response route "1" are linked to all answers with response route "1") | numeric |  |
| Answer Value |  | text |  |

## TDI_SURVEY_GENERAL

Fields: 9.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| Question ID | ID associated with the Question | numeric |  |
| Response ID | ID associated with the Response | numeric |  |
| Answer ID | ID associated with the Answer | numeric |  |
| Date Submitted Date Days Since Sign Up |  | numeric |  |
| Survey Title | Overarching survey title | text |  |
| Parent Question Title | Title of top-level question, if subquestions are present (e.g, What is your current height?) | text |  |
| Question Title | Title of top-level question if no subquestions are present or title of subquestion (e.g., Feet, Inches) | text |  |
| Answer Value | Participant's Response to above link of questions | text |  |

## TDI_SURVEY_GEOGRAPHY

Fields: 10.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| Question ID | ID associated with the Question | numeric |  |
| Response ID | ID associated with the Response | numeric |  |
| Answer ID | ID associated with the Answer | numeric |  |
| Date Submitted Date Days Since Sign Up |  | numeric |  |
| Survey Title | Overarching survey title | text |  |
| Parent Question Title | Title of top-level question, if subquestions are present (e.g, What residences have you lived in for 6 months or more?) | text |  |
| Question Title | Title of top-level question if no subquestions are preset or title of subquestion (e.g., What year did you move there?) | text |  |
| Response Route | Number that links questions and answers (e.g., All questions with response route "1" are linked to all answers with response route "1") | numeric |  |
| Answer Value | Participant's Response to above link of questions | text |  |

## TDI_SURVEY_HOSPITALIZATIONS

Fields: 8.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| Question ID | ID associated with the Question | numeric |  |
| Response ID | ID associated with the Response | numeric |  |
| Answer ID | ID associated with the Answer | numeric |  |
| Date Submitted Date Days Since Sign Up |  | numeric |  |
| Survey Title | Overarching survey title | text |  |
| Question Title | Title of question, no subquestions present | text |  |
| Answer Value |  | text |  |

## TDI_SURVEY_INJURIES

Fields: 8.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| Question ID | ID associated with the Question | numeric |  |
| Response ID | ID associated with the Response | numeric |  |
| Answer ID | ID associated with the Answer | numeric |  |
| Date Submitted Date Days Since Sign Up |  | numeric |  |
| Survey Title | Overarching survey title | text |  |
| Question Title | Title of question, no subquestions present | text |  |
| Answer Value |  | text |  |

## TDI_SURVEY_LIFESTYLE

Fields: 10.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| Question ID | ID associated with the Question | numeric |  |
| Response ID | ID associated with the Response | numeric |  |
| Answer ID | ID associated with the Answer | numeric |  |
| Date Submitted Date Days Since Sign Up |  | numeric |  |
| Survey Title | Overarching survey title | text |  |
| Parent Question Title | Title of top-level question, if subquestions are present (e.g, For each of the following age ranges please specify the estimated number of times per (week/month/year)?) | text |  |
| Question Title | Title of top-level question if no subquestions are preset or title of subquestion (e.g., Estimated number of times) | text |  |
| Response Route | Age range that is applicable to the subquestion (15-24 years) | text |  |
| Answer Value | Participant's Response to above link of questions | text |  |

## TDI_SURVEY_OCCUPATION

Fields: 10.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| Question ID | ID associated with the Question | numeric |  |
| Response ID | ID associated with the Response | numeric |  |
| Answer ID | ID associated with the Answer | numeric |  |
| Date Submitted Date Days Since Sign Up |  | numeric |  |
| Survey Title | Overarching survey title | text |  |
| Parent Question Title | Title of top-level question, if subquestions are present (e.g, What job titles and industries have you held in the past?) | text |  |
| Question Title | Title of top-level question if no subquestions are preset or title of subquestion (e.g., Job Title) | text |  |
| Response Route | Number that links questions and answers (e.g., All questions with response route "1" are linked to all answers with response route "1") | numeric |  |
| Answer Value | Participant's Response to above link of questions | text |  |

## TDI_VOICE_SCORE

Fields: 4.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant ID |  | numeric |  |
| Days Since Onset From Recording |  | numeric |  |
| Days Since Sign Up From Recording |  | numeric |  |
| Score | Predicted speech score generated using algorithm described in (web link in the dictionary file) | numeric |  |
