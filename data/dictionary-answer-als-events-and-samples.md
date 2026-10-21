# Answer ALS clinical dictionary: events, logs, labs and samples

Part of dictionary-answer-als.md, which lists every form and the page that holds it.

Columns: Field name is the column header in the form CSV. Label is the dictionary's New Field Label. Type is numeric or text. Coded values are the codes and labels for a coded field, as "code, label" pairs separated by a pipe, as the dictionary gives them. Coded fields are stored as the code. Text is written in ASCII (curly quotes and dashes become plain ones) and a # before a number is written as the word number, and a web link is replaced by the words (web link in the dictionary file).

Source: __Clinical_Dictionary_Sep_2026.csv. Written from the dictionary rows only, never from a data file.

## ANSASFD

Form label: ANSWER-ALS Subject Final Disposition. Fields: 9.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Form_Name | The name of this form | numeric |  |
| lnadt | Date last known alive, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| moptrb | Reason for exiting study | numeric | 1, Subject was a Screen Failure \| 2, Subject died \| 3, Discontinued Participation \| 99, Other (specify) |
| otsp | Other reason for exiting study (specify) | text |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| sfdt | Date of Screen Failure, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| sfsp | Reason for screen failure | text |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## ANSWER_ALS_Medications_Log

Form label: Medication Log. Fields: 15.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Form_Name | The name of this form | numeric |  |
| invdrg | Was this medication an investigational drug | numeric | 1, Yes \| 2, No |
| med | Medication | text |  |
| meddose | Medication Dose | text |  |
| medenddt | Medication Stop Date, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| medfreq | Medication Frequency | numeric | 1, QD \| 2, BID \| 3, TID \| 4, QID \| 5, QHS \| 6, continuous IV \| 7, PRN \| 99, other (please specify) |
| medfrqsp | Medication Frequency other specify | text |  |
| medind | Medication Indication | text |  |
| medrte | Medication Route | numeric | 1, oral \| 2, intravenous \| 3, subcutaneous \| 4, topical \| 5, inhalation \| 6, transdermal \| 7, rectal \| 8, intramuscular \| 9, sublingual \| 10, PEG \| 99, other (please specify) |
| medrtesp | Medication Route other specify | text |  |
| medstdt | Medication Start Date, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| medu | Medication Unit | numeric | 1, micrograms (ucg) \| 2, milligrams (mg) \| 3, grams (g) \| 4, tablet(s) \| 5, capsule(s) \| 6, gtt \| 7, milliequivalent (meq) \| 8, international units (U) \| 9, units (U) \| 99, other (please specify) |
| meduotsp | Medication Unit other specify | text |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |

## ANSWER_ALS_MobileApp

Form label: Mobile App Form. Fields: 6.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Form_Name | The name of this form | numeric |  |
| madate | If 'Yes', please enter Date of Enrollment in the trial: | numeric |  |
| mobileap | Mobile App consent | numeric | 1, Yes \| 2, No |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Auxiliary_Chemistry

Form label: Auxiliary Chemistry 2. Fields: 31.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| acckrslt | Creatine Kinase (CK) Result | text |  |
| acckunit | Creatine Kinase (CK) Units | text |  |
| accreuni | Creatinine Units | text |  |
| accrrslt | Creatinine Result | text |  |
| acphouni | Phosphorus Units | text |  |
| acphrslt | Phosphorus result interpretation | text |  |
| acuarslt | Uric Acid Results | text |  |
| acuaunit | Uric Acid Units | text |  |
| cknorm | Creatine kinase result interpretation | numeric | 1, Normal \| 2, Abnormal, NOT Clinically Significant \| 3, Abnormal, Clinically Significant |
| crenorm | Creatinine result interpretation | numeric | 1, Normal \| 2, Abnormal, NOT Clinically Significant \| 3, Abnormal, Clinically Significant |
| Form_Name | The name of this form | numeric |  |
| labdn | Auxiliary Chemistry laboratory data collection status | numeric | 1, Collected \| 2, Not collected |
| labdt | Date Blood Drawn, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| ot1norm | Interpretation of additional laboratory test (Other 1) | numeric | 1, Normal \| 2, Abnormal, NOT Clinically Significant \| 3, Abnormal, Clinically Significant |
| ot2norm | Interpretation of additional laboratory test (Other 2) | numeric | 1, Normal \| 2, Abnormal, NOT Clinically Significant \| 3, Abnormal, Clinically Significant |
| ot3norm | Interpretation of additional laboratory test (Other 3) | numeric | 1, Normal \| 2, Abnormal, NOT Clinically Significant \| 3, Abnormal, Clinically Significant |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| phonorm | Phosphorus result interpretation | numeric | 1, Normal \| 2, Abnormal, NOT Clinically Significant \| 3, Abnormal, Clinically Significant |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| uanorm | Uric acid result interpretation | numeric | 1, Normal \| 2, Abnormal, NOT Clinically Significant \| 3, Abnormal, Clinically Significant |
| uot1rslt | Result value for additional laboratory test (Other 1) | text |  |
| uot1test | Name of additional laboratory test (Other 1) | text |  |
| uot1unit | Units of measure for additional laboratory test (Other 1) | text |  |
| uot2rslt | Result value for additional laboratory test (Other 2) | text |  |
| uot2test | Name of additional laboratory test (Other 2) | text |  |
| uot2unit | Units of measure for additional laboratory test (Other 2) | text |  |
| uot3rslt | Result value for additional laboratory test (Other 3) | text |  |
| uot3test | Name of additional laboratory test (Other 3) | text |  |
| uot3unit | Units of measure for additional laboratory test (Other 3) | text |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Auxiliary_Chemistry_Labs

Form label: Auxiliary Chemistry 1. Fields: 31.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| acckrslt | Creatine Kinase (CK) Result | text |  |
| acckunit | Creatine Kinase (CK) Units | text |  |
| accreuni | Creatinine Units | text |  |
| accrrslt | Creatinine Result | text |  |
| acphouni | Phosphorus Units | text |  |
| acphrslt | Phosphorus result interpretation | text |  |
| acuarslt | Uric Acid Results | text |  |
| acuaunit | Uric Acid Units | text |  |
| cknorm | Creatine kinase result interpretation | numeric | 1, Normal \| 2, Abnormal, NOT Clinically Significant \| 3, Abnormal, Clinically Significant |
| crenorm | Creatinine result interpretation | numeric | 1, Normal \| 2, Abnormal, NOT Clinically Significant \| 3, Abnormal, Clinically Significant |
| Form_Name | The name of this form | numeric |  |
| labdn | Auxiliary Chemistry laboratory data collection status | numeric | 1, Collected \| 2, Not collected |
| labdt | Date Blood Drawn, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| ot1norm | Interpretation of additional laboratory test (Other 1) | numeric | 1, Normal \| 2, Abnormal, NOT Clinically Significant \| 3, Abnormal, Clinically Significant |
| ot2norm | Interpretation of additional laboratory test (Other 2) | numeric | 1, Normal \| 2, Abnormal, NOT Clinically Significant \| 3, Abnormal, Clinically Significant |
| ot3norm | Interpretation of additional laboratory test (Other 3) | numeric | 1, Normal \| 2, Abnormal, NOT Clinically Significant \| 3, Abnormal, Clinically Significant |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| phonorm | Phosphorus result interpretation | numeric | 1, Normal \| 2, Abnormal, NOT Clinically Significant \| 3, Abnormal, Clinically Significant |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| uanorm | Uric acid result interpretation | numeric | 1, Normal \| 2, Abnormal, NOT Clinically Significant \| 3, Abnormal, Clinically Significant |
| uot1rslt | Result value for additional laboratory test (Other 1) | text |  |
| uot1test | Name of additional laboratory test (Other 1) | text |  |
| uot1unit | Units of measure for additional laboratory test (Other 1) | text |  |
| uot2rslt | Result value for additional laboratory test (Other 2) | text |  |
| uot2test | Name of additional laboratory test (Other 2) | text |  |
| uot2unit | Units of measure for additional laboratory test (Other 2) | text |  |
| uot3rslt | Result value for additional laboratory test (Other 3) | text |  |
| uot3test | Name of additional laboratory test (Other 3) | text |  |
| uot3unit | Units of measure for additional laboratory test (Other 3) | text |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Cerebrospinal_Fluid

Form label: Cerebrospinal Fluid Collection Log. Fields: 30.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| aliqcnt | Number of full CSF aliquots created | numeric |  |
| aliqfzth | Time CSF aliquots put in freezer HRS (aliqfzth : aliqfztm) (24hr clock) | numeric |  |
| aliqfztm | Time CSF aliquots put in freezer MINS (aliqfzth : aliqfztm) (24hr clock) | numeric |  |
| aliqicth | Time CSF aliquots put on dry ice HRS (aliqicth : aliqictm) (24hr clock) | numeric |  |
| aliqictm | Time CSF aliquots put on dry ice MINS (aliqicth : aliqictm) (24hr clock) | numeric |  |
| aliqth | Time CSF aliquoted HRS (aliqth : aliqtm) (24hr clock) | numeric |  |
| aliqtm | Time CSF aliquoted MINS (aliqth : aliqtm) (24hr clock) | numeric |  |
| aliqvol | Volume per full CSF aliquot | numeric |  |
| aliqvolu | CSF aliquot volume units | numeric | 1, mL \| 2, uL (microliter) |
| alqicena | CSF aliquots not placed on dry ice | numeric | 0, 0 \| 1, 1 |
| alqvolot | Volume of last CSF aliquot (if less than volume specified) | numeric |  |
| csfcntth | Time CSF centrifugation started HRS (csfcntth : csfcnttm) (24hr clock) | numeric |  |
| csfcnttm | Time CSF centrifugation started MINS (csfcntth : csfcnttm) (24hr clock) | numeric |  |
| csfcol | CSF sample collection number | numeric |  |
| csfcolth | Time CSF collected HRS (csfcolth : csfcoltm) (24hr clock) | numeric |  |
| csfcoltm | Time CSF collected MINS (csfcolth : csfcoltm) (24hr clock) | numeric |  |
| csfdn | CSF sample collection status | numeric | 1, Collected \| 2, Not collected |
| csfdnsp | Reason CSF sample not collected | text |  |
| csfdt | Date CSF sample collected, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| csfdur | Duration of CSF centrifugation (minutes) | numeric |  |
| csfspeed | CSF centrifugation speed (relative centrifugal force, x g) | numeric |  |
| Form_Name | The name of this form | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| possmp | Post-centrifugation CSF sample appearance | numeric | 1, Clear \| 2, Pink \| 3, Cloudy \| 99, other |
| possmpsp | Specify post-centrifugation CSF sample appearance | text |  |
| presmp | Pre-centrifugation CSF sample appearance | numeric | 1, Clear \| 2, Pink \| 3, Cloudy \| 99, other |
| presmpsp | Specify pre-centrifugation CSF sample appearance | text |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Diaphragm_Pacing_System_Device

Form label: Diaphragm Pacing System Device Log. Fields: 7.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| dpsadmin | Admission date for diaphragm pacing system placement, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| dpsdate | Date of Placement for diaphragm pacing system, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| dpsdsch | Discharge Date, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| dpsrec | Date diaphragm pacing system (DPS) recommended, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Form_Name | The name of this form | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |

## DNA_Sample_Collection

Form label: DNA Sample Collection Log. Fields: 16.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| aliqcnt | Number of full DNA aliquots | numeric |  |
| aliqvol | Volume per full DNA aliquot | numeric |  |
| aliqvolu | DNA aliquot volume units | numeric | 1, mL \| 2, uL (microliter) |
| alqvolot | Volume of last DNA aliquot (if less than volume specified) | numeric |  |
| dnacnt | Number of DNA tubes collected | numeric |  |
| dnacol | DNA sample collection number | numeric |  |
| dnadn | DNA sample collection status | numeric | 1, Collected \| 2, Not collected |
| dnadnsp | Reason DNA sample not collected | text |  |
| dnadt | Date DNA sample collected, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Form_Name | The name of this form | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| resource | RESOURCE ID | numeric |  |
| smplnygc | DNA sample sent to New York Genome Center (NYGC) | numeric | 1, Yes \| 2, No |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Feeding_Tube_Placement

Form label: Feeding Tube Placement. Fields: 25.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Form_Name | The name of this form | numeric |  |
| ftpaccdt | Date feeding tube accepted, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| ftpadmdt | Feeding Tube Admission Date, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| ftpdchdt | Feeding Tube Discharge Date, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| ftpelctv | Feeding tube placement urgency | numeric | 1, Prophylactic/elective \| 2, Emergent |
| ftpmeth | Feeding tube placement method | numeric | 1, General surgery \| 2, Interventional radiology \| 3, Microscopic Laparotomy \| 4, Percutaneous Endoscopic Gastrostomy \| 99, Other, specify |
| ftpmthsp | Specify other placement method | text |  |
| ftprecdt | Date feeding tube recommended, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| ftptyp | Type of feeding tube | numeric | 1, Nasogastric \| 2, Gastrostomy |
| morabort | Procedure aborted secondary to anatomy (due to feeding tube) | numeric | 0, Unchecked \| 1, Checked |
| morasp | Aspiration (due to feeding tube) | numeric | 0, Unchecked \| 1, Checked |
| mordth | Death (due to feeding tube) | numeric | 0, Unchecked \| 1, Checked |
| morhem | Hemorrhage (due to feeding tube) | numeric | 0, Unchecked \| 1, Checked |
| morinf | Local infection (due to feeding tube) | numeric | 0, Unchecked \| 1, Checked |
| mornaus | Nausea/vomiting (due to feeding tube) | numeric | 0, Unchecked \| 1, Checked |
| morot | Other, specify: (due to feeding tube) | numeric | 0, Unchecked \| 1, Checked |
| morotsp | Other feeding tube morbidity specify | text |  |
| moroxygn | Oxygen desaturation/inadequate ventilation during procedure (due to feeding tube) | numeric | 0, Unchecked \| 1, Checked |
| morpain | Excessive pain (due to feeding tube) | numeric | 0, Unchecked \| 1, Checked |
| morper | Peritonitis (due to feeding tube) | numeric | 0, Unchecked \| 1, Checked |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| source | Source of data for Feeding Tube Placement | numeric | 1, medical records \| 2, original collection \| 3, patient reported \| 90, unknown \| 99, other |
| sourcesp | Specify other data source for Feeding Tube Placement | text |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Mortality

Form label: Mortality. Fields: 14.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| aut | Was an autopsy performed? | numeric | 1, Yes \| 2, No \| 90, Unknown |
| autdt | Date of Autopsy, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| autobt | Has a copy of the autopsy report been obtained? | numeric | 1, Yes \| 2, No |
| autpmi | Postmortem Interval (hours) | numeric |  |
| auttyp | Type of autopsy performed (Limited or complete) | numeric | 1, Complete autopsy \| 2, Limited autopsy (brain and spinal cord only) |
| diedcaus | Cause of death | text |  |
| dieddt | Date of death, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Form_Name | The name of this form | numeric |  |
| icd10cm | ICD-10 CM Code for cause of death | text |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| source | Source of data for Mortality | numeric | 1, Medical records \| 2, original collection \| 3, patient reported \| 90, unknown \| 99, other |
| sourcesp | Specify other data source | text |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## NIV_Log

Form label: Non-invasive Ventilation Log. Fields: 11.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Form_Name | The name of this form | numeric |  |
| nivcont | NIV use ongoing at end of study | numeric | 0, Unchecked \| 1, Checked |
| nivstpdt | NIV use stop date, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| nivstrdt | NIV use start date, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| nivusdur | NIV daily use (hours/day), single value | numeric |  |
| nivusg | NIV usage reporting method | numeric | 1, Range \| 2, Single Number |
| nivusg1 | No NIV use during study period | numeric | 0, Unchecked \| 1, Checked |
| nivusrg1 | NIV daily use (hours/day), range lower bound | numeric |  |
| nivusrg2 | NIV daily use (hours/day), range upper bound | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |

## PBMC_Sample_Collection

Form label: PBMC Sample Collection Log. Fields: 11.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Form_Name | The name of this form | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| smplcol | PBMC sample collection number | numeric |  |
| smpldn | PBMC sample collection status | numeric | 1, Collected \| 2, Not collected |
| smpldnsp | Reason PBMC sample not collected | text |  |
| smpldt | Date PBMC sample collected, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| tbscol | Number of PBMC tubes collected | numeric |  |
| tubshdt | Date PBMC tubes shipped, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Permanent_Assisted_Ventilation

Form label: Permanent Assisted Ventilation Log. Fields: 6.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Form_Name | The name of this form | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| pavdt | Permanent assisted ventilation date started, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| pavyn | Permanent assisted ventilation reached | numeric | 0, No \| 1, Yes |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Plasma_Sample

Form label: Plasma Collection Log. Fields: 27.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| aliqcnt | Number of full plasma aliquots | numeric |  |
| aliqvol | Volume per full plasma aliquot | numeric |  |
| aliqvolu | Plasma aliquot volume units | numeric | 1, mL \| 2, uL (microliter) |
| alqfrzna | Plasma aliquots not placed on dry ice | numeric | 0, Unchecked \| 1, Checked |
| alqfrzth | Time plasma aliquots put in freezer HRS (alqfrzth : alqfrztm) (24hr clock) | numeric |  |
| alqfrztm | Time plasma aliquots put in freezer MINS (alqfrzth : alqfrztm) (24hr clock) | numeric |  |
| alqiceth | Time plasma aliquots put on dry ice HRS (alqiceth : alqicetm) (24hr clock) | numeric |  |
| alqicetm | Time plasma aliquots put on dry ice MINS (alqiceth : alqicetm) (24hr clock) | numeric |  |
| alqth | Time plasma aliquoted HRS (alqth : alqtm) (24hr clock) | numeric |  |
| alqtm | Time plasma aliquoted MINS (alqth : alqtm) (24hr clock) | numeric |  |
| alqvolot | Volume of last plasma aliquot (if less than volume specified) | numeric |  |
| cntdur | Duration of plasma centrifugation (minutes) | numeric |  |
| Form_Name | The name of this form | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| plspnk | Plasma sample appearance after centrifugation | numeric | 1, Yes \| 2, No |
| smplclth | Time plasma collected HRS (smplclth : smplcltm) (24hr clock) | numeric |  |
| smplcltm | Time plasma collected MINS (smplclth : smplcltm) (24hr clock) | numeric |  |
| smplctth | Time plasma centrifugation started HRS (smplctth : smplcttm) (24hr clock) | numeric |  |
| smplcttm | Time plasma centrifugation started MINS (smplctth : smplcttm) (24hr clock) | numeric |  |
| smplspd | Plasma centrifugation speed (relative centrifugal force, x g) | numeric |  |
| srplcol | Plasma sample collection number | numeric |  |
| srpldn | Plasma sample collection status | numeric | 1, Collected \| 2, Not collected |
| srpldnsp | Reason plasma sample not collected | text |  |
| srpldt | Date plasma sample collected, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Serum_Sample

Form label: Serum Collection Log. Fields: 27.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| aliqcnt | Number of full serum aliquots | numeric |  |
| aliqvol | Volume per full serum aliquot | numeric |  |
| aliqvolu | Serum aliquot volume units | numeric | 1, mL \| 2, uL (microliter) |
| alqfrzna | Serum aliquots not placed on dry ice | numeric | 0, Unchecked \| 1, Checked |
| alqfrzth | Time serum aliquots put in freezer HRS (alqfrzth : alqfrztm) (24hr clock) | numeric |  |
| alqfrztm | Time serum aliquots put in freezer MINS (alqfrzth : alqfrztm) (24hr clock) | numeric |  |
| alqiceth | Time serum aliquots put on dry ice HRS (alqiceth : alqicetm) (24hr clock) | numeric |  |
| alqicetm | Time serum aliquots put on dry ice MINS (alqiceth : alqicetm) (24hr clock) | numeric |  |
| alqth | Time serum aliquoted HRS (alqth : alqtm) (24hr clock) | numeric |  |
| alqtm | Time serum aliquoted MINS (alqth : alqtm) (24hr clock) | numeric |  |
| alqvolot | Volume of last serum aliquot (if less than volume specified) | numeric |  |
| cntdur | Duration of serum centrifugation (minutes) | numeric |  |
| Form_Name | The name of this form | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| serpnk | Serum sample appearance after centrifugation | numeric | 1, Yes \| 2, No |
| smplclth | Time serum collected HRS (smplclth : smplcltm) (24hr clock) | numeric |  |
| smplcltm | Time serum collected MINS (smplclth : smplcltm) (24hr clock) | numeric |  |
| smplctth | Time serum centrifugation started HRS (smplctth : smplcttm) (24hr clock) | numeric |  |
| smplcttm | Time serum centrifugation started MINS (smplctth : smplcttm) (24hr clock) | numeric |  |
| smplspd | Serum centrifugation speed (relative centrifugal force, x g) | numeric |  |
| srplcol | Serum sample collection number | numeric |  |
| srpldn | Serum sample collection status | numeric | 1, Collected \| 2, Not collected |
| srpldnsp | Reason serum sample not collected | text |  |
| srpldt | Date serum sample collected, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Tracheostomy

Form label: Tracheostomy. Fields: 10.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| admsndt | Admission Date, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| dschgdt | Discharge Date, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Form_Name | The name of this form | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| rsnothsp | Specify other reason for tracheostomy | text |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| trachrsn | Reason for tracheostomy | numeric | 1, Respiratory failure \| 2, Secretion control \| 99, Other (specify) |
| trchdt | Date of Tracheostomy, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| trchrcdt | Date tracheostomy recommended | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |
