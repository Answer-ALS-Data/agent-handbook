# Answer ALS clinical package, Release 8: forms

The Answer ALS clinical package is one CSV per case report form, plus the clinical dictionary. Release 8 has 34 forms. The dictionary, __Clinical_Dictionary_Sep_2026.csv, ships inside the package and has one row per form column. It is the full field list; this page is a map of it, written from the dictionary only. It describes columns, never values.

## The dictionary

Columns of __Clinical_Dictionary_Sep_2026.csv:

| Column | Meaning |
|---|---|
| Form Name | The form, equal to the CSV file name without .csv, so the dictionary joins straight to the files. |
| Form Label | The readable form name. |
| Subsection Label | The section of the form the field sits in, when the form has sections. |
| Field Name | The column header in the form CSV. |
| New Field Label | What the field means. |
| Values | For coded fields, the codes and labels as "1, Yes / 2, No" (separated by a pipe in the file). Blank for free numbers and text. |
| Field Type | numeric or text. |
| Branching logic, if applicable | When the field is asked. |

## Rules that hold across forms

- Every form has Participant_ID and SubjectUID. Most also have Form_Name, Visit_Name and Visit_Date; some log and event forms leave out Visit_Date or both visit columns, and subjects has no Form_Name.
- Participant_ID has the same form as the index Participant_ID: CASE- or CTRL- plus the GUID. Join forms to the index on it. The prefix comes from subjects.subject_group_id (CTRL- for Healthy Control, CASE- otherwise).
- Dates are not calendar dates. Every date field is a count of days before (-) or after (+) the participant's screening visit. Day 0 is the screening visit.
- Coded fields are stored as the code, not the label. Read the label from the Values column.
- Identifier columns (Form_Name, Participant_ID, SubjectUID, Visit_Name) are typed numeric in the dictionary but hold text.
- Longitudinal forms have one row per participant per visit; log forms (medications, family history, medical history, NIV, neurological disease) have one row per entry.

## Forms

Fields counts the dictionary rows for the form, including the shared identifier and visit columns.

| Form Name | Form Label | What it collects | Fields | Key fields |
|---|---|---|---|---|
| AALSDXFX | ALS Diagnosis | El Escorial revised criteria: UMN and LMN signs and EMG denervation by body region | 28 | elescrlr (El Escorial conclusion), alsdxdt (exam day) |
| AALSHXFX | ALS History | Where and when ALS was diagnosed and the site of first symptoms | 29 | diagdt, onsetdt, hxblb, hxli, hxax (onset site flags) |
| ALS_CBS | ALS Cognitive Behavioral Screen | Cognitive screen sections and a caregiver behavior questionnaire | 81 | cbstot (total), attscr, conscr, iniscr, trkscr (section scores), carbeh (caregiver total), cbsdt |
| ALS_Gene_Mutations | Self-reported ALS Gene Mutations | Self-reported results for ALS genes, each with a not tested flag | 28 | c9orf72, sod1, fus, tdp43, mutot (other) |
| ALSFRS_R | ALS Functional Rating Scale (Revised) | The twelve ALSFRS-R items and total | 28 | alsfrst (total), alsfrs1 to alsfrs9, alsfrsr1 to alsfrsr3, alsfrsdt |
| ANSASFD | ANSWER-ALS Subject Final Disposition | Why and when the participant left the study | 9 | moptrb (exit reason), lnadt (last known alive) |
| ANSWER_ALS_Medications_Log | Medication Log | One row per medication with dose, route and dates | 15 | med, meddose, medu, medrte, medstdt, medenddt |
| ANSWER_ALS_MobileApp | Mobile App Form | Mobile app consent | 6 | mobileap |
| Ashworth_Spasticity_Scale | Ashworth Spasticity Scale | Spasticity score per limb | 14 | asharml, asharmr, ashlegl, ashlegr, ashdt |
| Auxiliary_Chemistry | Auxiliary Chemistry 2 | Creatine kinase, creatinine, phosphorus, uric acid and three other tests, with units and interpretation | 31 | acckrslt, accrrslt, acphrslt, acuarslt, labdt |
| Auxiliary_Chemistry_Labs | Auxiliary Chemistry 1 | Same fields as Auxiliary_Chemistry | 31 | acckrslt, accrrslt, acphrslt, acuarslt, labdt |
| Cerebrospinal_Fluid | Cerebrospinal Fluid Collection Log | CSF collection, processing times and aliquots | 30 | csfdn (status), csfdt, aliqcnt |
| CNS_Lability_Scale | Central Nervous System Lability Scale | Seven item pseudobulbar affect scale | 19 | cnslstot (total), cnslsq1 to cnslsq7, cnsldt |
| Demographics | Demographics | Age, relative birth date, sex, ethnicity and race flags | 14 | sex, ethnic, racewt, raceblk, raceasn, raceamin, racenh, age |
| Diaphragm_Pacing_System_Device | Diaphragm Pacing System Device Log | Diaphragm pacing recommendation and placement dates | 7 | dpsrec, dpsdate |
| DNA_Sample_Collection | DNA Sample Collection Log | DNA collection, aliquots and shipment to the New York Genome Center | 16 | dnadn (status), dnadt, smplnygc |
| Environmental_Questionnaire | Environmental Questionnaire | Exercise, geography, smoking and alcohol, head injury, military, sport, toxin and occupation history | 58 | smokerb, concussrb, milirb, sportdd, occupation flags ending in -ock |
| Family_History_Log | Family History Log | One row per relative with conditions and gene mutations | 44 | famrel, fhals, fhftd, fhdem, famguid (relative GUID) |
| Feeding_Tube_Placement | Feeding Tube Placement | Feeding tube dates, type, method and complications | 25 | ftprecdt, ftpadmdt, ftpdchdt, ftptyp, ftpmeth |
| Grip_Strength_Testing | Grip Strength Testing | Left and right grip strength, two trials each | 19 | lgrpt1, lgrpt2, rgrpt1, rgrpt2, grpdtper |
| Hand_Held_Dynamometry | Hand Held Dynamometry | Strength of 9 muscle actions, left and right, three trials each | 134 | trial fields ending t1 to t3 per muscle (for example lket1), hhdldt |
| Medical_History | Medical History | One row per medical condition | 9 | medhxdsc, medhxprs, medhxyr (diagnosis day, relative to screening) |
| Mortality | Mortality | Death, cause and autopsy | 14 | dieddt, diedcaus, icd10cm, aut |
| NEUROLOG | Neurological Disease Log | Other neurological diagnoses by category | 22 | neuro (category), diag1 to diag9, d1ag0 to d1ag4, date1 |
| NIV_Log | Non-invasive Ventilation Log | NIV start, stop and daily use | 11 | nivstrdt, nivstpdt, nivusdur |
| PBMC_Sample_Collection | PBMC Sample Collection Log | PBMC collection and shipment | 11 | smpldn (status), smpldt, tubshdt |
| Permanent_Assisted_Ventilation | Permanent Assisted Ventilation Log | Whether and when permanent ventilation started | 6 | pavyn, pavdt |
| Plasma_Sample | Plasma Collection Log | Plasma collection, processing times and aliquots | 27 | srpldn (status), srpldt, aliqcnt |
| Reflexes | Reflexes | Cranial, cervical and lumbosacral reflex scores, left and right | 67 | score fields ending scr (for example lbcpscr), rflxdt |
| Serum_Sample | Serum Collection Log | Serum collection, processing times and aliquots | 27 | srpldn (status), srpldt, aliqcnt |
| subjects | Study Disease Group Assignment | The participant's study group | 3 | subject_group_id |
| Tracheostomy | Tracheostomy | Tracheostomy reason and dates | 10 | trchdt, trachrsn |
| Vital_Capacity | Vital Capacity | Slow and forced vital capacity, three trials each, with percent predicted | 38 | svcl1 to svcl3, svcp1 to svcp3, fvcl1 to fvcl3, svcdt |
| Vital_Signs | Vital Signs | Height, weight, BMI, blood pressure, heart rate, respiratory rate, temperature | 25 | weight, height, bmi, bpsys, bpdias, vsdt |

## Codes worth knowing

- subjects.subject_group_id: 1 ALS, 5 Healthy Control, 11 Asymptomatic ALS Gene carrier, 17 Non-ALS MND.
- Collection status fields (names ending in dn, such as alsfdn, csfdn, vsdn): 1 Collected, 2 Not collected. The matching dnsp field gives the reason.
- source fields: where the record came from: 1 Medical records, 2 original collection, 3 patient reported, 90 unknown, 99 other.
- Checkbox fields: 0 Unchecked, 1 Checked.

## Source

__Clinical_Dictionary_Sep_2026.csv (Release 8 dictionary) and DICTIONARY_CHANGES.md from the Release 8 dictionary build.
