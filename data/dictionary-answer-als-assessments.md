# Answer ALS clinical dictionary: clinical assessments

Part of dictionary-answer-als.md, which lists every form and the page that holds it.

Columns: Field name is the column header in the form CSV. Label is the dictionary's New Field Label. Type is numeric or text. Coded values are the codes and labels for a coded field, as "code, label" pairs separated by a pipe, as the dictionary gives them. Coded fields are stored as the code. Text is written in ASCII (curly quotes and dashes become plain ones) and a # before a number is written as the word number, and a web link is replaced by the words (web link in the dictionary file).

Source: __Clinical_Dictionary_Sep_2026.csv. Written from the dictionary rows only, never from a data file.

## ALS_CBS

Form label: ALS Cognitive Behavioral Screen. Fields: 81.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| atta | Number of errors when participant followed two multi-step verbal commands (e.g., "point to the ceiling then to your left"; "touch your shoulder, point to the floor, then make a fist") | numeric | 0, 0 \| 1, 1+ |
| attb1 | Number of syllables stated by participant for the phrase "The weather is nice" (correct answer = 5 syllables) | numeric |  |
| attb1tim | Participant required more than 20 seconds to respond to the syllable counting task for "The weather is nice" | numeric | 0, Unchecked \| 1, Subject took >20 seconds |
| attb2 | Number of syllables stated by the participant for the phrase "Tomorrow will be sunny" (correct answer = 7 syllables) | numeric |  |
| attb2tim | Participant required more than 20 seconds to respond to the syllable counting task for "Tomorrow will be sunny" | numeric | 0, Unchecked \| 1, Subject took >20 seconds |
| attc1 | Number of correct visually guided saccades performed by the participant out of 8 trials | numeric | 0, 0 \| 1, 1 \| 2, 2 \| 3, 3 \| 4, 4 \| 5, 5 \| 6, 6 \| 7, 7 \| 8, 8 |
| attc2 | Number of correct antisaccades (looking in the opposite direction of a stimulus) performed by the participant out of 8 trials | numeric | 0, 0 \| 1, 1 \| 2, 2 \| 3, 3 \| 4, 4 \| 5, 5 \| 6, 6 \| 7, 7 \| 8, 8 |
| attscr | Attention section subtotal score derived from commands, syllable counting, and eye movement tasks (maximum score = 5) | numeric |  |
| carbeh | Total caregiver-reported behavioral change score (sum of 15 items; maximum score = 45) | numeric |  |
| carbeh01 | Reduced interest in activities or topics that were previously important to the participant before ALS symptom onset | numeric | 1, No Change \| 2, Small Change \| 3, Medium Change \| 4, Large Change |
| carbeh02 | Reduced emotional expression or responsiveness compared to the participant's behavior before ALS symptom onset | numeric | 1, No Change \| 2, Small Change \| 3, Medium Change \| 4, Large Change |
| carbeh03 | More agreeable or pleasant demeanor with fewer worries compared to before ALS symptom onset | numeric | 1, No Change \| 2, Small Change \| 3, Medium Change \| 4, Large Change |
| carbeh04 | Acts without thinking or fails to consider consequences before acting compared to before ALS symptom onset | numeric | 1, No Change \| 2, Small Change \| 3, Medium Change \| 4, Large Change |
| carbeh05 | Increased social withdrawal not attributable to sadness compared to before ALS symptom onset | numeric | 1, No Change \| 2, Small Change \| 3, Medium Change \| 4, Large Change |
| carbeh06 | More easily confused or distracted compared to before ALS symptom onset | numeric | 1, No Change \| 2, Small Change \| 3, Medium Change \| 4, Large Change |
| carbeh07 | Reduced ability to tolerate frustration or stress compared to before ALS symptom onset | numeric | 1, No Change \| 2, Small Change \| 3, Medium Change \| 4, Large Change |
| carbeh08 | Reduced concern for others' feelings or decreased empathy compared to before ALS symptom onset | numeric | 1, No Change \| 2, Small Change \| 3, Medium Change \| 4, Large Change |
| carbeh09 | Increased anger or irritability compared to before ALS symptom onset | numeric | 1, No Change \| 2, Small Change \| 3, Medium Change \| 4, Large Change |
| carbeh10 | More sarcastic or childlike behavior compared to before ALS symptom onset | numeric | 1, No Change \| 2, Small Change \| 3, Medium Change \| 4, Large Change |
| carbeh11 | Increased appetite or new preference for particular foods (e.g., sweets) compared to before ALS symptom onset | numeric | 1, No Change \| 2, Small Change \| 3, Medium Change \| 4, Large Change |
| carbeh12 | Greater difficulty adapting to change or modifying opinions compared to before ALS symptom onset | numeric | 1, No Change \| 2, Small Change \| 3, Medium Change \| 4, Large Change |
| carbeh13 | Reduced judgment or impaired decision-making (e.g., safety, financial decisions) compared to before ALS symptom onset | numeric | 1, No Change \| 2, Small Change \| 3, Medium Change \| 4, Large Change |
| carbeh14 | Reduced awareness of obvious problems or denial of changes compared to before ALS symptom onset | numeric | 1, No Change \| 2, Small Change \| 3, Medium Change \| 4, Large Change |
| carbeh15 | New language difficulties such as word-finding problems, incorrect word substitutions, newly created words, or decline in spelling ability compared to before ALS symptom onset | numeric | 1, No Change \| 2, Small Change \| 3, Medium Change \| 4, Large Change |
| cbsdn | ALS CBS Assessment Status (Collected / Not Collected) | numeric | 1, Collected \| 2, Not collected |
| cbsdnsp | Reason ALS CBS Assessment Not Collected | text |  |
| cbsdt | Date ALS Cognitive Behavioral Screen performed, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| cbstot | Total score for ALS Cognitive Behavioral Screen (sum of Attention, Concentration, Tracking/Monitoring, and Initiation & Retrieval section scores; maximum score = 20) | numeric |  |
| cbswrite | Mark if participant responses were written | numeric |  |
| cgcuranx | Caregiver reports that the participant appears anxious on most days at the present time | numeric | 1, Yes \| 2, No |
| cgcurcry | Caregiver reports that the participant experiences episodes of unexpected crying or laughing at the present time | numeric | 1, Yes \| 2, No |
| cgcurdep | Caregiver reports that the participant appears depressed on most days at the present time | numeric | 1, Yes \| 2, No |
| cgcurftg | Caregiver reports that the participant appears extremely fatigued on most days at the present time | numeric | 1, Yes \| 2, No |
| cgqcnst | Caregiver consent obtained? | numeric | 1, Yes \| 2, No \| 95, N/A |
| cgqdn | ALS Caregiver Questionnaire Status (Collected / Not Collected) | numeric | 1, Collected \| 2, Not collected |
| cgqdnsp | Reason Caregiver Questionnaire Not Collected | text |  |
| cgqdt | Date caregiver questionnaire performed, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| cgqrel | Relation to participant | numeric | 1, Child \| 2, Friend \| 3, Home aide \| 4, In-home nurse \| 5, Long-term care/Nursing facility staff \| 6, Neighbor \| 7, Other relative \| 8, Parent or legal guardian \| 9, Roomate or housemate \| 10, Sibling \| 11, Spouse or partner |
| Child_Name | The name of the administered form | numeric |  |
| con1 | Correctly repeated the 2-digit sequence "2-9" in reverse order (expected response: 9-2) | numeric | 1, Correct \| 2, Incorrect |
| con2 | Correctly repeated the 2-digit sequence "6-4" in reverse order (expected response: 4-6) | numeric | 1, Correct \| 2, Incorrect |
| con3 | Correctly repeated the 3-digit sequence "3-7-2" in reverse order (expected response: 2-7-3) | numeric | 1, Correct \| 2, Incorrect |
| con4 | Correctly repeated the 3-digit sequence "5-8-1" in reverse order (expected response: 1-8-5) | numeric | 1, Correct \| 2, Incorrect |
| con5 | Correctly repeated the 4-digit sequence "7-8-6-4" in reverse order (expected response: 4-6-8-7) | numeric | 1, Correct \| 2, Incorrect |
| con6 | Correctly repeated the 4-digit sequence "5-4-1-9" in reverse order (expected response: 9-1-4-5) | numeric | 1, Correct \| 2, Incorrect |
| con7 | Correctly repeated the 5-digit sequence "8-2-5-9-3" in reverse order (expected response: 3-9-5-2-8) | numeric | 1, Correct \| 2, Incorrect |
| con8 | Correctly repeated the 5-digit sequence "5-7-6-3-9" in reverse order (expected response: 9-3-6-7-5) | numeric | 1, Correct \| 2, Incorrect |
| conscr | Concentration section subtotal score derived from backward digit span performance (maximum score = 5) | numeric |  |
| ini01 | 1st word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini02 | 2nd word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini03 | 3rd word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini04 | 4th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini05 | 5th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini06 | 6th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini07 | 7th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini08 | 8th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini09 | 9th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini10 | 10th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini11 | 11th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini12 | 12th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini13 | 13th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini14 | 14th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini15 | 15th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini16 | 16th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini17 | 17th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini18 | 18th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini19 | 19th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| ini20 | 20th word generated by the participant beginning with the letter F during the 1-minute verbal fluency task | text |  |
| iniscr | Initiation and Retrieval section subtotal score derived from verbal fluency performance (maximum score = 5) | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| source | Source of data for this ALS CBS record | numeric | 1, medical records \| 2, original collection \| 3, patient reported \| 90, unknown \| 99, other |
| sourcesp | Specify other data source | text |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| trka | Number of sequencing errors while the participant recited the months of the year in reverse order, starting with December | numeric | 0, 0 \| 1, 1 \| 2, 2+ |
| trkb | Number of errors while the participant recited or wrote the alphabet in correct sequential order (A-Z) | numeric | 0,0 \| 1, 1+ |
| trkc | Number of sequencing errors while the participant alternated between ascending numbers and letters in order (e.g., 1-A, 2-B, 3-C, continuing sequentially) | numeric | 0, 0 \| 1, 1 \| 2, 2 |
| trkcor | Total number of correct admissible words generated by the participant during the 1-minute letter F verbal fluency task | numeric | 1, <=4 \| 2, <8 \| 3, 8-12 \| 4, >12 |
| trkerr | Number of rule violations or repeated words produced by the participant during the 1-minute letter F verbal fluency task | numeric | 0, 0 \| 1, 1 \| 2, 2+ |
| trkscr | Tracking/Monitoring section subtotal score derived from months backward, alphabet recitation, and alternation tasks (maximum score = 5) | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## ALSFRS_R

Form label: ALS Functional Rating Scale (Revised). Fields: 28.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| alsfdn | ALSFRS-R Assessment Status | numeric | 1, Collected \| 2, Not Collected |
| alsfdnsp | Reason ALSFRS-R Not Collected | text |  |
| alsfrs1 | ALSFRS-R 1.Speech score | numeric | 0, Loss of useful speech \| 1, Speech combined with nonvocal communication \| 2, Intelligible with repeating \| 3, Detectable speech disturbances \| 4, Normal speech processes |
| alsfrs2 | ALSFRS-R 2.Salivation score | numeric | 0, Marked drooling requires constant tissue or handkerchief \| 1, Marked excess of saliva with some drooling \| 2, Moderately excessive saliva may have minimal drooling \| 3, Slight but definite excess of saliva in mouth may have nighttime drooling \| 4, Normal |
| alsfrs3 | ALSFRS-R 3.Swallowing score | numeric | 0, NPO (exclusively parenteral or enteral feeding) \| 1, Needs supplemental tube feeding \| 2, Dietary consistency changes \| 3, Early eating problems - occasional choking \| 4, Normal eating habits |
| alsfrs4 | ALSFRS-R 4.Handwriting score | numeric | 0, Unable to grip pen \| 1, Able to grip pen but unable to write \| 2, Not all words are legible \| 3, Slow or sloppy all words are legible \| 4, Normal |
| alsfrs5 | Presence of gastrostomy tube at time of assessment | numeric | 1, Yes \| 2, No |
| alsfrs5a | ALSFRS-R 5.a Cutting Without Gastrostomy score | numeric | 0, Needs to be fed \| 1, Food must be cut by someone, but can still feed slowly \| 2, Can cut most foods, although clumsy and slow some help needed \| 3, Somewhat slow and clumsy, but no help needed \| 4, Normal |
| alsfrs5b | ALSFRS-R 5.b Cutting With Gastrostomy score | numeric | 0, Unable to perform any aspect of task \| 1, Provides minimal assistance to caregivers \| 2, Some help needed with closures and fasteners \| 3, Clumsy but able to perform all manipulations independently \| 4, Normal |
| alsfrs6 | ALSFRS-R 6.Dressing and Hygiene score | numeric | 0, Total dependence \| 1, Needs attendant for self-care \| 2, Intermittent assistance or substitute methods \| 3, Independent and complete self-care with effort or decreased efficiency \| 4, Normal function |
| alsfrs7 | ALSFRS-R 7.Turning in Bed score | numeric | 0, Helpless \| 1, Can initiate, but not turn or adjust sheets alone \| 2, Can turn alone or adjust sheets, but with great difficulty \| 3, Somewhat slow and clumsy, but no help needed \| 4, Normal |
| alsfrs8 | ALSFRS-R 8.Walking score | numeric | 0, No purposeful leg movement \| 1, Nonambulatory functional movement only \| 2, Walks with assistance \| 3, Early ambulation difficulties \| 4, Normal |
| alsfrs9 | ALSFRS-R 9.Climbing Stairs score | numeric | 0, Cannot do \| 1, Needs assistance \| 2, Mild unsteadiness or fatigue \| 3, Slow \| 4, Normal |
| alsfrsdt | ALSFRS-R Date Performed, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| alsfrsmd | ALSFRS-R Mode of administration | numeric | 1, In person \| 2, Telephone \| 3, Self-administered \| 99, Other |
| alsfrsr1 | ALSFRS-R R-1.Dyspnea score | numeric | 0, Significant difficulty, considering using mechanical respiratory support \| 1, Occurs at rest, difficulty breathing when either sitting or lying \| 2, Occurs with one or more of the following: eating, bathing, dressing \| 3, Occurs when walking \| 4, None |
| alsfrsr2 | ALSFRS-R R-2 Orthopnea score | numeric | 0, Unable to sleep without mechanical assistance \| 1, Can only sleep sitting up \| 2, Needs extra pillow in order to sleep (more than two) \| 3, Some difficulty sleeping at night due to shortness of breath, does not routinely use more than two pillows \| 4, None |
| alsfrsr3 | ALSFRS-R R-3.Respiratory Insufficiency score | numeric | 0, Invasive mechanical ventilation by intubation or tracheostomy \| 1, Continuous use of NIPPV during the night and day \| 2, Continuous use of NIPPV during the night \| 3, Intermittent use of NIPPV \| 4, None |
| alsfrsrp | ALSFRS-R Responder | numeric | 1, Patient \| 2, Patient via Caregiver |
| alsfrssp | Specify Other Mode | text |  |
| alsfrst | ALSFRS Total Score | numeric |  |
| Form_Name | The name of this form | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| source | Source of data for ALSFRS-R assessment | numeric | 1, Medical records \| 2, original collection \| 3, patient reported \| 90, unknown \| 99, other |
| sourcesp | Specify other data source | text |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | text |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Ashworth_Spasticity_Scale

Form label: Ashworth Spasticity Scale. Fields: 14.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| asharml | Ashworth spasticity scale Score Left Arm | numeric | 1, No increase in muscle tone \| 2, Slight increase in tone giving a 'catch' when affected part is moved in flexion or extension \| 3, More marked increase in tone, but affected part is easily flexed \| 4, Considerable increase in tone; passive movement difficult \| 5, Affected part is rigid in flexion or extension \| 6, Not tested \| 7, Not tested (subject unable to perform task) |
| asharmr | Ashworth spasticity scale Score Right Arm | numeric | 1, No increase in muscle tone \| 2, Slight increase in tone giving a 'catch' when affected part is moved in flexion or extension \| 3, More marked increase in tone, but affected part is easily flexed \| 4, Considerable increase in tone; passive movement difficult \| 5, Affected part is rigid in flexion or extension \| 6, Not tested \| 7, Not tested (subject unable to perform task) |
| ashdn | Ashworth Spasticity Scale Assessment Status | numeric | 1, Collected \| 2, Not Collected |
| ashdnsp | Reason Ashworth Spasticity Scale Not Collected | text |  |
| ashdt | Ashworth spasticity scale date performed, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| ashlegl | Ashworth spasticity scale Score Left Leg | numeric | 1, No increase in muscle tone \| 2, Slight increase in tone giving a 'catch' when affected part is moved in flexion or extension \| 3, More marked increase in tone, but affected part is easily flexed \| 4, Considerable increase in tone; passive movement difficult \| 5, Affected part is rigid in flexion or extension \| 6, Not tested \| 7, Not tested (subject unable to perform task) |
| ashlegr | Ashworth spasticity scale Score Right Leg | numeric | 1, No increase in muscle tone \| 2, Slight increase in tone giving a 'catch' when affected part is moved in flexion or extension \| 3, More marked increase in tone, but affected part is easily flexed \| 4, Considerable increase in tone; passive movement difficult \| 5, Affected part is rigid in flexion or extension \| 6, Not tested \| 7, Not tested (subject unable to perform task) |
| Form_Name | The name of this form | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| source | Source of data for Ashworth Spasticity Scale | numeric | 1, medical records \| 2, original collection \| 3, patient reported \| 90, unknown \| 99, other |
| sourcesp | Specify other data source | text |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## CNS_Lability_Scale

Form label: Central Nervous System Lability Scale. Fields: 19.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| cnslcb | Completed by | numeric | 1, Patient \| 2, Person other than patient |
| cnsldn | Status | numeric | 1, Collected \| 2, Not collected |
| cnsldnsp | Reason not collected | text |  |
| cnsldt | Date assessment performed, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| cnslsq1 | CNS Lability Scale Q1: There are times when I feel fine 1 minute, and then I'll become tearful the next over something small or for no reason at all. | numeric | 1, Does not apply \| 2, Rarely Applies \| 3, Occasionally Applies \| 4, Frequently Applies \| 5, Applies Most of the Time |
| cnslsq2 | CNS Lability Scale Q2: Others have told me that I seem to become amused very easily or that I seem to become amused about things that aren't funny. | numeric | 1, Does not apply \| 2, Rarely Applies \| 3, Occasionally Applies \| 4, Frequently Applies \| 5, Applies Most of the Time |
| cnslsq3 | CNS Lability Scale Q3: I find myself crying very easily. | numeric | 1, Does not apply \| 2, Rarely Applies \| 3, Occasionally Applies \| 4, Frequently Applies \| 5, Applies Most of the Time |
| cnslsq4 | CNS Lability Scale Q4: I find that even when I try to control my laughter, I am often unable to do so. | numeric | 1, Does not apply \| 2, Rarely Applies \| 3, Occasionally Applies \| 4, Frequently Applies \| 5, Applies Most of the Time |
| cnslsq5 | CNS Lability Scale Q5: There are times when I won't be thinking of anything happy or funny at all, but then I'll suddenly be overcome by funny or happy thoughts. | numeric | 1, Does not apply \| 2, Rarely Applies \| 3, Occasionally Applies \| 4, Frequently Applies \| 5, Applies Most of the Time |
| cnslsq6 | CNS Lability Scale Q6: I find that even when I try to control my crying, I am often unable to do so. | numeric | 1, Does not apply \| 2, Rarely Applies \| 3, Occasionally Applies \| 4, Frequently Applies \| 5, Applies Most of the Time |
| cnslsq7 | CNS Lability Scale Q7: I find that I am easily overcome by laughter. | numeric | 1, Does not apply \| 2, Rarely Applies \| 3, Occasionally Applies \| 4, Frequently Applies \| 5, Applies Most of the Time |
| cnslstot | Total score for CNS Lability Scale (sum of 7 items; score range 7-35) | numeric |  |
| Form_Name | The name of this form | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| source | Source of data for CNS Lability Scale | numeric | 1, medical records \| 2, original collections \| 3, patient reported \| 90, unknown \| 99, other |
| sourcesp | Specify other data source | text |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Grip_Strength_Testing

Form label: Grip Strength Testing. Fields: 19.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Form_Name | The name of this form | numeric |  |
| grpdtper | Date Assessment Performed, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| grpstat | Grip strength testing status | numeric | 1, Done \| 2, Not done |
| lgrpntck | Left Grip Strength Not Tested Checkbox | numeric | 0, Unchecked \| 1, Checked |
| lgrpset | Left Grip Strength Setting | text |  |
| lgrpsp | Reason left-hand grip strength test was not performed | numeric | 1, Subject unable to perform task due to weakness \| 99, Other (Specify) |
| lgrpspo | Left Grip Not Tested Specify Other | text |  |
| lgrpt1 | Left Grip Strength Trial 1 (Pounds) | numeric |  |
| lgrpt2 | Left Grip Strength Trial 2 (Pounds) | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| rgrpntck | Right Grip Strength Not Tested Checkbox | numeric | 0, Unchecked \| 1, Checked |
| rgrpset | Right Grip Strength Setting | text |  |
| rgrpsp | Reason right-hand grip strength test was not performed | numeric | 1, Subject unable to perform task due to weakness \| 99, Other (Specify) |
| rgrpspo | Right Grip Not Tested Specify Other | text |  |
| rgrpt1 | Right Grip Strength Trial 1 (Pounds) | numeric |  |
| rgrpt2 | Right Grip Strength Trial 2 (Pounds) | numeric |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Hand_Held_Dynamometry

Form label: Hand Held Dynamometry. Fields: 134.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Form_Name | The name of this form | numeric |  |
| hhddn | Hand-held dynamometry status | numeric | 1, Collected \| 2, Not collected |
| hhddnsp | Hand-held dynamometry reason not collected | text |  |
| hhdldt | Date collected, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| ladab | Hand-held dynamometry, left ankle dorsiflexion: examiner able to break | numeric | 1, Yes \| 2, No |
| ladnt | Hand-held dynamometry, left ankle dorsiflexion not performed | numeric | 0, Unchecked \| 1, Checked |
| ladntsp | Reason hand-held dynamometry was not performed for left ankle dorsiflexion | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| ladspo | Specify other reason hand-held dynamometry was not performed for left ankle dorsiflexion | text |  |
| ladt1 | Hand-held dynamometry strength, left ankle dorsiflexion, trial 1 (lb) | numeric |  |
| ladt2 | Hand-held dynamometry strength, left ankle dorsiflexion, trial 2 (lb) | numeric |  |
| ladt3 | Hand-held dynamometry strength, left ankle dorsiflexion, trial 3 (lb) | numeric |  |
| leeab | Hand-held dynamometry, left elbow extension: examiner able to break | numeric | 1, Yes \| 2, No |
| leent | Hand-held dynamometry, left elbow extension not performed | numeric | 0, Unchecked \| 1, Checked |
| leentsp | Reason hand-held dynamometry was not performed for left elbow extension | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| leespo | Specify other reason hand-held dynamometry was not performed for left elbow extension | text |  |
| leet1 | Hand-held dynamometry strength, left elbow extension, trial 1 (lb) | numeric |  |
| leet2 | Hand-held dynamometry strength, left elbow extension, trial 2 (lb) | numeric |  |
| leet3 | Hand-held dynamometry strength, left elbow extension, trial 3 (lb) | numeric |  |
| lefab | Hand-held dynamometry, left elbow flexion: examiner able to break | numeric | 1, Yes \| 2, No |
| lefnt | Hand-held dynamometry, left elbow flexion not performed | numeric | 0, Unchecked \| 1, Checked |
| lefntsp | Reason hand-held dynamometry was not performed for left elbow flexion | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| lefspo | Specify other reason hand-held dynamometry was not performed for left elbow flexion | text |  |
| left1 | Hand-held dynamometry strength, left elbow flexion, trial 1 (lb) | numeric |  |
| left2 | Hand-held dynamometry strength, left elbow flexion, trial 2 (lb) | numeric |  |
| left3 | Hand-held dynamometry strength, left elbow flexion, trial 3 (lb) | numeric |  |
| lfdicab | Hand-held dynamometry, left first dorsal interosseous contraction: examiner able to break | numeric | 1, Yes \| 2, No |
| lfdicnt | Hand-held dynamometry, left first dorsal interosseous contraction not performed | numeric | 0, Unchecked \| 1, Checked |
| lfdicnts | Reason hand-held dynamometry was not performed for left first dorsal interosseous contraction | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| lfdicspo | Specify other reason hand-held dynamometry was not performed for left first dorsal interosseous contraction | text |  |
| lfdict1 | Hand-held dynamometry strength, left first dorsal interosseous contraction, trial 1 (lb) | numeric |  |
| lfdict2 | Hand-held dynamometry strength, left first dorsal interosseous contraction, trial 2 (lb) | numeric |  |
| lfdict3 | Hand-held dynamometry strength, left first dorsal interosseous contraction, trial 3 (lb) | numeric |  |
| lhfab | Hand-held dynamometry, left hip flexion: examiner able to break | numeric | 1, Yes \| 2, No |
| lhfnt | Hand-held dynamometry, left hip flexion not performed | numeric | 0, Unchecked \| 1, Checked |
| lhfntsp | Reason hand-held dynamometry was not performed for left hip flexion | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| lhfspo | Specify other reason hand-held dynamometry was not performed for left hip flexion | text |  |
| lhft1 | Hand-held dynamometry strength, left hip flexion, trial 1 (lb) | numeric |  |
| lhft2 | Hand-held dynamometry strength, left hip flexion, trial 2 (lb) | numeric |  |
| lhft3 | Hand-held dynamometry strength, left hip flexion, trial 3 (lb) | numeric |  |
| lkeab | Hand-held dynamometry, left knee extension: examiner able to break | numeric | 1, Yes \| 2, No |
| lkent | Hand-held dynamometry, left knee extension not performed | numeric | 0, Unchecked \| 1, Checked |
| lkentsp | Reason hand-held dynamometry was not performed for left knee extension | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| lkespo | Specify other reason hand-held dynamometry was not performed for left knee extension | text |  |
| lket1 | Hand-held dynamometry strength, left knee extension, trial 1 (lb) | numeric |  |
| lket2 | Hand-held dynamometry strength, left knee extension, trial 2 (lb) | numeric |  |
| lket3 | Hand-held dynamometry strength, left knee extension, trial 3 (lb) | numeric |  |
| lkfab | Hand-held dynamometry, left knee flexion: examiner able to break | numeric | 1, Yes \| 2, No |
| lkfnt | Hand-held dynamometry, left knee flexion not performed | numeric | 0, Unchecked \| 1, Checked |
| lkfntsp | Reason hand-held dynamometry was not performed for left knee flexion | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| lkfspo | Specify other reason hand-held dynamometry was not performed for left knee flexion | text |  |
| lkft1 | Hand-held dynamometry strength, left knee flexion, trial 1 (lb) | numeric |  |
| lkft2 | Hand-held dynamometry strength, left knee flexion, trial 2 (lb) | numeric |  |
| lkft3 | Hand-held dynamometry strength, left knee flexion, trial 3 (lb) | numeric |  |
| lsfab | Hand-held dynamometry, left shoulder flexion: examiner able to break | numeric | 1, Yes \| 2, No |
| lsfnt | Hand-held dynamometry, left shoulder flexion not performed | numeric | 0, Unchecked \| 1, Checked |
| lsfntsp | Reason hand-held dynamometry was not performed for left shoulder flexion | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| lsfspo | Specify other reason hand-held dynamometry was not performed for left shoulder flexion | text |  |
| lsft1 | Hand-held dynamometry strength, left shoulder flexion, trial 1 (lb) | numeric |  |
| lsft2 | Hand-held dynamometry strength, left shoulder flexion, trial 2 (lb) | numeric |  |
| lsft3 | Hand-held dynamometry strength, left shoulder flexion, trial 3 (lb) | numeric |  |
| lweab | Hand-held dynamometry, left wrist extension: examiner able to break | numeric | 1, Yes \| 2, No |
| lwent | Hand-held dynamometry, left wrist extension not performed | numeric | 0, Unchecked \| 1, Checked |
| lwentsp | Reason hand-held dynamometry was not performed for left wrist extension | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| lwespo | Specify other reason hand-held dynamometry was not performed for left wrist extension | text |  |
| lwet1 | Hand-held dynamometry strength, left wrist extension, trial 1 (lb) | numeric |  |
| lwet2 | Hand-held dynamometry strength, left wrist extension, trial 2 (lb) | numeric |  |
| lwet3 | Hand-held dynamometry strength, left wrist extension, trial 3 (lb) | numeric |  |
| Participant_ID | ALS participant identifier | numeric |  |
| radab | Hand-held dynamometry, right ankle dorsiflexion: examiner able to break | numeric | 1, Yes \| 2, No |
| radnt | Hand-held dynamometry, right ankle dorsiflexion not performed | numeric | 0, Unchecked \| 1, Checked |
| radntsp | Reason hand-held dynamometry was not performed for right ankle dorsiflexion | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| radspo | Specify other reason hand-held dynamometry was not performed for right ankle dorsiflexion | text |  |
| radt1 | Hand-held dynamometry strength, right ankle dorsiflexion, trial 1 (lb) | numeric |  |
| radt2 | Hand-held dynamometry strength, right ankle dorsiflexion, trial 2 (lb) | numeric |  |
| radt3 | Hand-held dynamometry strength, right ankle dorsiflexion, trial 3 (lb) | numeric |  |
| reeab | Hand-held dynamometry, right elbow extension: examiner able to break | numeric | 1, Yes \| 2, No |
| reent | Hand-held dynamometry, right elbow extension not performed | numeric | 0, Unchecked \| 1, Checked |
| reentsp | Reason hand-held dynamometry was not performed for right elbow extension | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| reespo | Specify other reason hand-held dynamometry was not performed for right elbow extension | text |  |
| reet1 | Hand-held dynamometry strength, right elbow extension, trial 1 (lb) | numeric |  |
| reet2 | Hand-held dynamometry strength, right elbow extension, trial 2 (lb) | numeric |  |
| reet3 | Hand-held dynamometry strength, right elbow extension, trial 3 (lb) | numeric |  |
| refab | Hand-held dynamometry, right elbow flexion: examiner able to break | numeric | 1, Yes \| 2, No |
| refnt | Hand-held dynamometry, right elbow flexion not performed | numeric | 0, Unchecked \| 1, Checked |
| refntsp | Reason hand-held dynamometry was not performed for right elbow flexion | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| refspo | Specify other reason hand-held dynamometry was not performed for right elbow flexion | text |  |
| reft1 | Hand-held dynamometry strength, right elbow flexion, trial 1 (lb) | numeric |  |
| reft2 | Hand-held dynamometry strength, right elbow flexion, trial 2 (lb) | numeric |  |
| reft3 | Hand-held dynamometry strength, right elbow flexion, trial 3 (lb) | numeric |  |
| rfdicab | Hand-held dynamometry, right first dorsal interosseous contraction: examiner able to break | numeric | 1, Yes \| 2, No |
| rfdicnt | Hand-held dynamometry, right first dorsal interosseous contraction not performed | numeric | 0, Unchecked \| 1, Checked |
| rfdicnts | Reason hand-held dynamometry was not performed for right first dorsal interosseous contraction | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| rfdicspo | Specify other reason hand-held dynamometry was not performed for right first dorsal interosseous contraction | text |  |
| rfdict1 | Hand-held dynamometry strength, right first dorsal interosseous contraction, trial 1 (lb) | numeric |  |
| rfdict2 | Hand-held dynamometry strength, right first dorsal interosseous contraction, trial 2 (lb) | numeric |  |
| rfdict3 | Hand-held dynamometry strength, right first dorsal interosseous contraction, trial 3 (lb) | numeric |  |
| rhfab | Hand-held dynamometry, right hip flexion: examiner able to break | numeric | 1, Yes \| 2, No |
| rhfnt | Hand-held dynamometry, right hip flexion not performed | numeric | 0, Unchecked \| 1, Checked |
| rhfntsp | Reason hand-held dynamometry was not performed for right hip flexion | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| rhfspo | Specify other reason hand-held dynamometry was not performed for right hip flexion | numeric |  |
| rhft1 | Hand-held dynamometry strength, right hip flexion, trial 1 (lb) | numeric |  |
| rhft2 | Hand-held dynamometry strength, right hip flexion, trial 2 (lb) | numeric |  |
| rhft3 | Hand-held dynamometry strength, right hip flexion, trial 3 (lb) | numeric |  |
| rkeab | Hand-held dynamometry, right knee extension: examiner able to break | numeric | 1, Yes \| 2, No |
| rkent | Hand-held dynamometry, right knee extension not performed | numeric | 0, Unchecked \| 1, Checked |
| rkentsp | Reason hand-held dynamometry was not performed for right knee extension | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| rkespo | Specify other reason hand-held dynamometry was not performed for right knee extension | text |  |
| rket1 | Hand-held dynamometry strength, right knee extension, trial 1 (lb) | numeric |  |
| rket2 | Hand-held dynamometry strength, right knee extension, trial 2 (lb) | numeric |  |
| rket3 | Hand-held dynamometry strength, right knee extension, trial 3 (lb) | numeric |  |
| rkfab | Hand-held dynamometry, right knee flexion: examiner able to break | numeric | 1, Yes \| 2, No |
| rkfnt | Hand-held dynamometry, right knee flexion not performed | numeric | 0, Unchecked \| 1, Checked |
| rkfntsp | Reason hand-held dynamometry was not performed for right knee flexion | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| rkfspo | Specify other reason hand-held dynamometry was not performed for right knee flexion | text |  |
| rkft1 | Hand-held dynamometry strength, right knee flexion, trial 1 (lb) | numeric |  |
| rkft2 | Hand-held dynamometry strength, right knee flexion, trial 2 (lb) | numeric |  |
| rkft3 | Hand-held dynamometry strength, right knee flexion, trial 3 (lb) | numeric |  |
| rsfab | Hand-held dynamometry, right shoulder flexion: examiner able to break | numeric | 1, Yes \| 2, No |
| rsfnt | Hand-held dynamometry, right shoulder flexion not performed | numeric | 0, Unchecked \| 1, Checked |
| rsfntsp | Reason hand-held dynamometry was not performed for right shoulder flexion | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| rsfspo | Specify other reason hand-held dynamometry was not performed for right shoulder flexion | text |  |
| rsft1 | Hand-held dynamometry strength, right shoulder flexion, trial 1 (lb) | numeric |  |
| rsft2 | Hand-held dynamometry strength, right shoulder flexion, trial 2 (lb) | numeric |  |
| rsft3 | Hand-held dynamometry strength, right shoulder flexion, trial 3 (lb) | numeric |  |
| rweab | Hand-held dynamometry, right wrist extension: examiner able to break | numeric | 1, Yes \| 2, No |
| rwent | Hand-held dynamometry, right wrist extension not performed | numeric | 0, Unchecked \| 1, Checked |
| rwentsp | Reason hand-held dynamometry was not performed for right wrist extension | numeric | 1, Subject unable to perform task due to weakness \| 2, Other (Specify) |
| rwespo | Specify other reason hand-held dynamometry was not performed for right wrist extension | text |  |
| rwet1 | Hand-held dynamometry strength, right wrist extension, trial 1 (lb) | numeric |  |
| rwet2 | Hand-held dynamometry strength, right wrist extension, trial 2 (lb) | numeric |  |
| rwet3 | Hand-held dynamometry strength, right wrist extension, trial 3 (lb) | numeric |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Reflexes

Form label: Reflexes. Fields: 67.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| cfrnd | Cranial Facial Reflex not assessed | numeric | 0, Unchecked \| 1, Checked |
| cjjnd | Cranial Jaw Jerk not assessed | numeric | 0, Unchecked \| 1, Checked |
| cjjscr | Cranial Jaw Jerk reflex score | numeric | 1, Absent \| 2, Present |
| cpsnd | Cranial Palmomental Sign not assessed | numeric | 0, Unchecked \| 1, Checked |
| cpsscr | Cranial Palmomental Sign reflex score | numeric | 1, Absent \| 2, Present |
| crcfrscr | Cranial Facial Reflex score | numeric | 1, Absent \| 2, Present |
| lbcpnd | Left Biceps reflex not assessed | numeric | 0, Unchecked \| 1, Checked |
| lbcpscr | Left Biceps reflex score | numeric | 0, 0 \| 1, 1 \| 2, 2 \| 3, 3 \| 4, 4 |
| lbcpwk | Left Biceps reflex retained in weak or wasted limb | numeric | 1, Yes \| 2, No \| 95, N/A |
| lbrchnd | Left Brachioradialis reflex not assessed | numeric | 0, Unchecked \| 1, Checked |
| lbrchscr | Left Brachioradialis reflex score | numeric | 0, 0 \| 1, 1 \| 2, 2 \| 3, 3 \| 4, 4 |
| lbrchwk | Left Brachioradialis reflex retained in weak or wasted limb | numeric | 1, Yes \| 2, No \| 95, N/A |
| lcclnnd | Left Cervical Clonus not assessed | numeric | 0, Unchecked \| 1, Checked |
| lcclnscr | Left Cervical Clonus reflex score | numeric | 1, Absent \| 2, Present |
| lffnd | Left Finger Flexors reflex not assessed | numeric | 0, Unchecked \| 1, Checked |
| lffscr | Left Finger Flexors reflex score | numeric | 1, Absent \| 2, Present |
| lhsnd | Left Hoffman Sign not assessed | numeric | 0, Unchecked \| 1, Checked |
| lhsscr | Left Hoffman Sign reflex score | numeric | 1, Absent \| 2, Present |
| ltrcpnd | Left Triceps reflex not assessed | numeric | 0, Unchecked \| 1, Checked |
| ltrcpscr | Left Triceps reflex score | numeric | 0, 0 \| 1, 1 \| 2, 2 \| 3, 3 \| 4, 4 |
| ltrcpwk | Left Triceps reflex retained in weak or wasted limb | numeric | 1, Yes \| 2, No \| 95, N/A |
| lanklnd | Left Ankle reflex not assessed | numeric | 0, Unchecked \| 1, Checked |
| lanklscr | Left Ankle reflex score | numeric | 0, 0 \| 1, 1 \| 2, 2 \| 3, 3 \| 4, 4 |
| lanklwk | Left Ankle reflex retained in weak or wasted limb | numeric | 1, Yes \| 2, No \| 95, N/A |
| lbsnd | Left Babinski Sign not assessed | numeric | 0, Unchecked \| 1, Checked |
| lbsscr | Left Babinski Sign reflex score | numeric | 1, Absent \| 2, Present |
| lcadnd | Left Crossed Adduction not assessed | numeric | 0, Unchecked \| 1, Checked |
| lcadscr | Left Crossed Adduction reflex score | numeric | 1, Absent \| 2, Present |
| llclnnd | Left Lumbosacral Clonus not assessed | numeric | 0, Unchecked \| 1, Checked |
| llclnscr | Left Lumbosacral Clonus reflex score | numeric | 1, Absent \| 2, Present |
| lptlrnd1 | Left Patellar reflex not assessed | numeric | 0, Unchecked \| 1, Checked |
| lptlrscr | Left Patellar reflex score | numeric | 0, 0 \| 1, 1 \| 2, 2 \| 3, 3 \| 4, 4 |
| lptlrwk | Left Patellar reflex retained in weak or wasted limb | numeric | 1, Yes \| 2, No \| 95, N/A |
| rbcpnd | Right Biceps reflex not assessed | numeric | 0, Unchecked \| 1, Checked |
| rbcpscr | Right Biceps reflex score | numeric | 0, 0 \| 1, 1 \| 2, 2 \| 3, 3 \| 4, 4 |
| rbcpwk | Right Biceps reflex retained in weak or wasted limb | numeric | 1, Yes \| 2, No \| 95, N/A |
| rbrchnd | Right Brachioradialis reflex not assessed | numeric | 0, Unchecked \| 1, Checked |
| rbrchscr | Right Brachioradialis reflex score | numeric | 0, 0 \| 1, 1 \| 2, 2 \| 3, 3 \| 4, 4 |
| rbrchwk | Right Brachioradialis reflex retained in weak or wasted limb | numeric | 1, Yes \| 2, No \| 95, N/A |
| rcclnnd | Right Cervical Clonus not assessed | numeric | 0, Unchecked \| 1, Checked |
| rcclnscr | Right Cervical Clonus reflex score | numeric | 1, Absent \| 2, Present |
| rffnd | Right Finger Flexors reflex not assessed | numeric | 0, Unchecked \| 1, Checked |
| rffscr | Right Finger Flexors reflex score | numeric | 1, Absent \| 2, Present |
| rhsnd | Right Hoffman Sign not assessed | numeric | 0, Unchecked \| 1, Checked |
| rhsscr | Right Hoffman Sign reflex score | numeric | 1, Absent \| 2, Present |
| rtrcpnd | Right Triceps reflex not assessed | numeric | 0, Unchecked \| 1, Checked |
| rtrcpscr | Right Triceps reflex score | numeric | 0, 0 \| 1, 1 \| 2, 2 \| 3, 3 \| 4, 4 |
| rtrcpwk | Right Triceps reflex retained in weak or wasted limb | numeric | 1, Yes \| 2, No \| 95, N/A |
| ranklnd | Right Ankle reflex not assessed | numeric | 0, Unchecked \| 1, Checked |
| ranklscr | Right Ankle reflex score | numeric | 0, 0 \| 1, 1 \| 2, 2 \| 3, 3 \| 4, 4 |
| ranklwk | Right Ankle reflex retained in weak or wasted limb | numeric | 1, Yes \| 2, No \| 95, N/A |
| rbsnd | Right Babinski Sign not assessed | numeric | 0, Unchecked \| 1, Checked |
| rbsscr | Right Babinski Sign reflex score | numeric | 1, Absent \| 2, Present |
| rcadnd | Right Crossed Adduction not assessed | numeric | 0, Unchecked \| 1, Checked |
| rcadscr | Right Crossed Adduction reflex score | numeric | 1, Absent \| 2, Present |
| rlclnnd | Right Lumbosacral Clonus not assessed | numeric | 0, Unchecked \| 1, Checked |
| rlclnscr | Right Lumbosacral Clonus reflex score | numeric | 1, Absent \| 2, Present |
| rptlrnd | Right Patellar reflex not assessed | numeric | 0, Unchecked \| 1, Checked |
| rptlrscr | Right Patellar reflex score | numeric |  |
| rptlrwk | Right Patellar reflex retained in weak or wasted limb | numeric | 1, Yes \| 2, No \| 95, N/A |
| Form_Name | The name of this form | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| rflxdt | Date reflex examination performed, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| rflxst | Reflex examination status | numeric | 1, Done \| 2, Not done |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Vital_Capacity

Form label: Vital Capacity. Fields: 38.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Form_Name | The name of this form | numeric |  |
| fvcl1 | FVC Trial 1 Result (L) | numeric |  |
| fvcl2 | FVC Trial 2 Result (L) | numeric |  |
| fvcl3 | FVC Trial 3 Result (L) | numeric |  |
| fvcnd2 | FVC Trial 2 Not Done | numeric | 0, Unchecked \| 1, Checked |
| fvcnd3 | FVC Trial 3 Not Done | numeric | 0, Unchecked \| 1, Checked |
| fvcndrs2 | Reason FVC Trial 2 Not Done | numeric | 1, Subject unable to perform task due to weakness \| 99, Other (Specify) |
| fvcndrs3 | Reason FVC Trial 3 Not Done | numeric | 1, Subject unable to perform task due to weakness \| 99, Other (Specify) |
| fvcndsp2 | Specify other reason FVC trial number 2 was not done | text |  |
| fvcndsp3 | Specify other reason FVC trial number 3 was not done | text |  |
| fvcp1 | FVC % Predicted Trial 1 | numeric |  |
| fvcp2 | FVC % Predicted Trial 2 | numeric |  |
| fvcp3 | FVC % Predicted Trial 3 | numeric |  |
| fvcvar | FVC % Variability | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| source | Source of data for Vital Capacity | numeric | 1, Medical records \| 2, original collection \| 3, patient reported \| 90, unknown \| 99, other |
| sourcesp | Specify other data source | text |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| svcdn | Vital Capacity Assessment Status | numeric | 1, Done \| 2, Not Done |
| svcdnsp | Reason Vital Capacity assessment not performed | text |  |
| svcdt | Date Vital Capacity assessment performed, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| svcl1 | SVC Trial 1 Result (L) | numeric |  |
| svcl2 | SVC Trial 2 Result (L) | numeric |  |
| svcl3 | SVC Trial 3 Result (L) | numeric |  |
| svcnd2 | SVC Trial 2 Not Done | numeric | 0, Unchecked \| 1, Checked |
| svcnd3 | SVC Trial 3 Not Done | numeric | 0, Unchecked \| 1, Checked |
| svcndrs2 | Reason SVC Trial 2 Not Done | numeric | 1, Subject unable to perform task due to weakness \| 99, Other (Specify) |
| svcndrs3 | Reason SVC Trial 3 Not Done | numeric | 1, Subject unable to perform task due to weakness \| 99, Other (Specify) |
| svcndsp2 | Specify other reason SVC trial number 2 was not done | text |  |
| svcndsp3 | Specify other reason SVC trial number 3 was not done | text |  |
| svcp1 | SVC % Predicted Trial 1 | numeric |  |
| svcp2 | SVC % Predicted Trial 2 | numeric |  |
| svcp3 | SVC % Predicted Trial 3 | numeric |  |
| svcvar | SVC % Variability | numeric |  |
| vcpos | Participant Position During Vital Capacity Testing | numeric | 1, Supine \| 2, Upright \| 95, Unknown |
| vctyp | Type of Vital Capacity examination performed | numeric | 1, SVC \| 2, FVC |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Vital_Signs

Form label: Vital Signs. Fields: 25.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| bmi | Body Mass Index (BMI) | numeric |  |
| bparm | Arm Used for Blood Pressure Measurement | numeric | 1, Left \| 2, Right |
| bpdias | Blood Pressure Measurement Diastolic (mmHG) | numeric |  |
| bppos | Participant Position During Blood Pressure Measurement | numeric | 1, Standing \| 2, Sitting \| 3, Supine |
| bpsys | Blood Pressure Measurement Systolic (mmHG) | numeric |  |
| Form_Name | The name of this form | numeric |  |
| height | Body Height | numeric |  |
| heightu | Height Units | numeric | 1, in \| 2, cm |
| hr | Heart rate (Beats / min) | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| rr | Respiratory Rate Measurement (Breaths / min) | numeric |  |
| source | Source of data for Vital Signs | numeric | 1, Medical records \| 2, original collection \| 3, patient reported \| 90, unknown \| 99, other |
| sourcesp | Specify other data source | text |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| temp | Body Temperature Measurement | numeric |  |
| temprt | Temperature Measurement Method | numeric | 1, Axillary \| 2, Oral \| 3, Rectal \| 4, Tympanic \| 99, Other |
| temprtsp | Specify other temperature measurement method | text |  |
| tempu | Temperature Units | numeric | 1, F \| 2, C |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |
| vsdn | Vital Signs Collection Status | numeric | 1, Collected \| 2, Not collected |
| vsdnsp | Reason Vital Signs were not collected | text |  |
| vsdt | Date Vital Signs performed, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| weight | Body Weight | numeric |  |
| weightu | Weight units | numeric | 1, lb \| 2, kg |
