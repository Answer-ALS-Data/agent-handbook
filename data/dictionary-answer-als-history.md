# Answer ALS clinical dictionary: diagnosis, history and demographics

Part of dictionary-answer-als.md, which lists every form and the page that holds it.

Columns: Field name is the column header in the form CSV. Label is the dictionary's New Field Label. Type is numeric or text. Coded values are the codes and labels for a coded field, as "code, label" pairs separated by a pipe, as the dictionary gives them. Coded fields are stored as the code. Text is written in ASCII (curly quotes and dashes become plain ones) and a # before a number is written as the word number, and a web link is replaced by the words (web link in the dictionary file).

Source: __Clinical_Dictionary_Sep_2026.csv. Written from the dictionary rows only, never from a data file.

## AALSDXFX

Form label: ALS Diagnosis. Fields: 28.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| alsdx1 | Topographical location and pattern of progression of UMN and LMN signs, including signs of spread within a region or to other regions, consistent with ALS? | numeric | 1, Yes \| 2, No |
| alsdx2 | Exclusion by electrophysiological testing of all other processes including conduction block that might explain the underlying signs and symptoms? | numeric | 1, Yes \| 2, No \| 90, Not Done |
| alsdx3 | Exclusion by neuroimaging of other disease processes such as myelopathy or radiculopathy that might explain observed clinical and electrophysiological signs? | numeric | 1, Yes \| 2, No \| 90, Not Done |
| alsdxdt | Date of examination, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| blbclmn | LMN Signs Present - Bulbar Region | numeric | 1, Yes \| 2, No \| 90, Not Done |
| blbcumn | UMN Signs Present - Bulbar Region | numeric | 1, Yes \| 2, No \| 90, Not Done |
| blbelmn | EMG Evidence of Denervation - Bulbar Region | numeric | 1, Denervation \| 2, No Denervation \| 90, Not Done |
| elescrlr | El Escorial Criteria Revised Conclusion | numeric | 1, Suspected \| 2, Possible \| 3, Probable Laboratory Supported \| 4, Probable \| 5, Definite |
| Form_Name | The name of this form | numeric |  |
| lleclmn | LMN Signs Present - Left Lower Extremity | numeric | 1, Yes \| 2, No \| 90, Not Done |
| llecumn | UMN Signs Present - Left Lower Extremity | numeric | 1, Yes \| 2, No \| 90, Not Done |
| lleelmn | EMG Evidence of Denervation - Left Lower Extremity | numeric | 1, Denervation \| 2, No Denervation \| 90, Not Done |
| lueclmn | LMN Signs Present - Left Upper Extremity | numeric | 1, Yes \| 2, No \| 90, Not Done |
| luecumn | UMN Signs Present - Left Upper Extremity | numeric | 1, Yes \| 2, No \| 90, Not Done |
| lueelmn | EMG Evidence of Denervation - Left Upper Extremity | numeric | 1, Denervation \| 2, No Denervation \| 90, Not Done |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| rleclmn | LMN Signs Present - Right Lower Extremity | numeric | 1, Yes \| 2, No \| 90, Not Done |
| rlecumn | UMN Signs Present - Right Lower Extremity | numeric | 1, Yes \| 2, No \| 90, Not Done |
| rleelmn | EMG Evidence of Denervation - Right Lower Extremity | numeric | 1, Denervation \| 2, No Denervation \| 90, Not Done |
| rueclmn | LMN Signs Present - Right Upper Extremity | numeric | 1, Yes \| 2, No \| 90, Not Done |
| ruecumn | UMN Signs Present - Right Upper Extremity | numeric | 1, Yes \| 2, No \| 90, Not Done |
| rueelmn | EMG Evidence of Denervation - Right Upper Extremity | numeric | 1, Denervation \| 2, No Denervation \| 90, Not Done |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| trnkclmn | LMN Signs Present - Trunk Region | numeric | 1, Yes \| 2, No \| 90, Not Done |
| trnkcumn | UMN Signs Present - Trunk Region | numeric | 1, Yes \| 2, No \| 90, Not Done |
| trnkelmn | EMG Evidence of Denervation - Trunk Region | numeric | 1, Denervation \| 2, No Denervation \| 90, Not Done |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## AALSHXFX

Form label: ALS History. Fields: 29.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| alsdxloc | Where was diagnosis made | numeric | 1, Outside center \| 2, ALS center |
| diagdt | Date of diagnosis, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Form_Name | The name of this form | numeric |  |
| hxax | Axial site of onset | numeric | 0, No \| 1, Yes |
| hxaxnk | Neck site of onset | numeric | 0, No \| 1, Yes |
| hxaxtr | Trunk site of onset | numeric | 0, No \| 1, Yes |
| hxaxtrrp | Respiratory site of onset | numeric | 0, No \| 1, Yes |
| hxblb | Bulbar site of onset | numeric | 0, No \| 1, Yes |
| hxblbsch | Speech site of onset | numeric | 0, No \| 1, Yes |
| hxblbsw | Swallowing site of onset | numeric | 0, No \| 1, Yes |
| hxgen | Generalized site of onset | numeric | 0, No \| 1, Yes |
| hxli | Limb site of onset | numeric | 0, No \| 1, Yes |
| hxlil | Lower Limb site of onset | numeric | 0, No \| 1, Yes |
| hxlilft | Foot site of onset | numeric | 0, No \| 1, Yes |
| hxlill | Lower Left Limb site of onset | numeric | 0, No \| 1, Yes |
| hxlilleg | Leg site of onset | numeric | 0, No \| 1, Yes |
| hxlilr | Lower Right Limb site of onset | numeric | 0, No \| 1, Yes |
| hxliu | Upper Limb site of onset | numeric | 0, No \| 1, Yes |
| hxliuarm | Arm site of onset | numeric | 0, No \| 1, Yes |
| hxliuhnd | Hand site of onset | numeric | 0, No \| 1, Yes |
| hxliul | Upper Left Limb site of onset | numeric | 0, No \| 1, Yes |
| hxliur | Upper Right Limb site of onset | numeric | 0, No \| 1, Yes |
| hxot | Other site of onset | numeric | 0, No \| 1, Yes |
| hxotsp | Other Text site of onset | text |  |
| onsetdt | Date of symptom onset, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## ALS_Gene_Mutations

Form label: Self-reported ALS Gene Mutations. Fields: 28.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| ang | Self-reported ANG mutation | numeric | 1, positive \| 2, negative |
| angnd | ANG Not Tested | numeric | 0, Tested \| 1, Not Tested |
| c9orf72 | Self-reported C9ORF72 mutation | numeric | 1, positive \| 2, negative |
| c9orfnd | C9ORF72 Not Tested | numeric | 0, Tested \| 1, Not Tested |
| Form_Name | The name of this form | numeric |  |
| fus | Self-reported FUS mutation | numeric | 1, positive \| 2, negative |
| fusnd | FUS Not Tested | numeric | 0, Tested \| 1, Not Tested |
| mutot | Other Mutation result | numeric | 1, positive \| 2, negative |
| mutotsp | Other mutation 1 | text |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| prgrnnd | Progranulin Not Tested | numeric | 0, Tested \| 1, Not Tested |
| progran | Self-reported Progranulin mutation | numeric | 1, positive \| 2, negative |
| setx | Self-reported SETX mutation | numeric | 1, positive \| 2, negative |
| setxnd | SETX Not Tested | numeric | 0, Tested \| 1, Not Tested |
| sod1 | Self-reported SOD1 mutation | numeric | 1, positive \| 2, negative |
| sod1muta | Specified SOD1 Gene Mutation | text |  |
| sod1nd | SOD1 Not Tested | numeric | 0, Tested \| 1, Not Tested |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| tau | Self-reported TAU mutation | numeric | 1, positive \| 2, negative |
| taund | Tau Not Tested | numeric | 0, Tested \| 1, Not Tested |
| tdp43 | Self-reported TDP-43 mutation | numeric | 1, positive \| 2, negative |
| tdp43nd | TDP43 Not Tested | numeric | 0, Tested \| 1, Not Tested |
| vapb | Self-reported VAPB mutation | numeric | 1, positive \| 2, negative |
| vapbnd | VAPB Not Tested | numeric | 0, Tested \| 1, Not Tested |
| vcp | Self-reported VCP mutation | numeric | 1, positive \| 2, negative |
| vcpnd | VCP Not Tested | numeric | 0, Tested \| 1, Not Tested |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Demographics

Form label: Demographics. Fields: 14.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| age | Age at time of assessment | numeric |  |
| dob | Date of Birth, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| ethnic | Ethnic category | numeric | 1, Hispanic or Latino \| 2, Not Hispanic or Latino |
| Form_Name | The name of this form | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| raceamin | Race: American Indian/Alaska Native | numeric | 0, No \| 1, Yes |
| raceasn | Race: Asian | numeric | 0, No \| 1, Yes |
| raceblk | Race: Black/African American | numeric | 0, No \| 1, Yes |
| racenh | Race: Native Hawaiian/Pacific Islander | numeric | 0, No \| 1, Yes |
| racewt | Race: White | numeric | 0, No \| 1, Yes |
| sex | Sex | numeric | 1, Male \| 2, Female |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Environmental_Questionnaire

Form label: Environmental Questionnaire. Fields: 58.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| exerdd | How many days per week do you exercise at least moderately (break a sweat)? | numeric |  |
| maratb | How many marathons have you run? | text |  |
| city1 | Current city of residence | text |  |
| city2 | City of residence immediately prior to ALS diagnosis | text |  |
| ottbx1 | Other current geography | text |  |
| ottbx2 | Other geography prior to diagnosis | text |  |
| state1 | Current state of residence | text |  |
| state2 | State of residence immediately prior to ALS diagnosis | text |  |
| asmkerb | Are you an active smoker? | numeric | 1, Yes \| 2, No |
| driavgtb | In the 10 years prior to your diagnosis, approximately how much alcohol did you drink (on average)? (drinks per week) | numeric |  |
| drinktb | How much alcohol do you drink? (drinks per week) | numeric |  |
| smkavgtb | How many packs per day (on average)? | numeric |  |
| smokerb | Have you ever been a smoker? | numeric | 1, Yes \| 2, No |
| yrssmktb | If so, for how many years? (years smoked) | numeric |  |
| concussrb | Have you had any concussions? (more than one year prior to symptom onset) | numeric | 1, Yes \| 2, No |
| concusstb | If so, how many? (how many concussions more than one year prior to symptom onset) | numeric |  |
| edrb | Have you ever been seen in the ED for a head injury? (more than one year prior to symptom onset) | numeric | 1, Yes \| 2, No |
| headrb | Have you ever been admitted to the hospital for a head injury? (more than one year prior to symptom onset) | numeric | 1, Yes \| 2, No |
| milirb | Were you in the military? | numeric | 1, Yes \| 2, No |
| outusrb | Were you deployed outside the US? | numeric | 1, Yes \| 2, No |
| where | To where? (Locations of deployment outside the United States) | text |  |
| yrsout | If so, what years? (Years deployed outside the United States) | text |  |
| yrstb | How many years? (Total years of military service) | numeric |  |
| leveldd | Sport Level | numeric | 1, High School \| 2, College \| 3, Amateur \| 4, Recreational \| 5, Professional |
| noytb | Number of years participated in sport | numeric |  |
| otsptb | Other Sport | text |  |
| sportdd | Sport Participated In | numeric | 1, Soccer \| 2, Football \| 3, Baseball \| 4, Hockey (ice/field) Lacrosse \| 5, Track & Field/Distance Running \| 6, Swimming \| 7, Tennis \| 9, Golf \| 99, Other |
| teck1 | Insecticide sprays inside home used >2 times per month for >=6 months | numeric | 0, Unchecked \| 1, Checked |
| teck2 | Insecticide sprays outside home used >2 times per month for >=6 months | numeric | 0, Unchecked \| 1, Checked |
| teck3 | Herbicide use >2 times per month for >=6 months | numeric | 0, Unchecked \| 1, Checked |
| adesmock | Arts, Design, Entertainment, Sports, and Media Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| aeock | Architecture and Engineering Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| bfopo | Business and Financial Operations Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| bgclmock | Building and Grounds Cleaning and Maintenance Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| ceock | Construction and Extraction Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| cmock | Computer and Mathematical Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| cssock | Community and Social Service Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| etlock | Education, Training, and Library Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| fffock | Farming, Fishing, and Forestry Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| fpsrock | Food Preparation and Serving Related Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| hptock | Healthcare Practitioners and Technical Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| hsock | Healthcare Support Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| imrock | Installation, Maintenance, and Repair Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| lock | Legal Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| lpssock | Life, Physical, and Social Science Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| mock | Management Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| msock | Military Specific Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| oasock | Office and Administrative Support Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| pcsock | Personal Care and Service Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| pock | Production Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| psock | Protective Service Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| srock | Sales and Related Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| tmmock | Transportation and Material Moving Occupations (held for at least 1 year) | numeric | 0, Unchecked \| 1, Checked |
| Form_Name | The name of this form | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Family_History_Log

Form label: Family History Log. Fields: 44.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| famgen | Family Member Gender | numeric | 1, Male \| 2, Female |
| famguid | GUID of selected relative | text |  |
| famher | Family Member Heredity | numeric | 1, Paternal \| 2, Maternal |
| famhx1 | A detailed family history was obtained: | numeric | 1, Yes \| 2, No |
| famrel | Family Member Relation | numeric | 1, Mother \| 2, Father \| 3, Sister \| 4, Brother \| 5, Half-sister \| 6, Half-brother \| 7, Daughter \| 8, Son \| 9, Grandmother \| 10, Grandfather \| 11, Aunt \| 12, Uncle \| 13, Cousin \| 99, other relative |
| famrelsp | Other relative | text |  |
| fhals | Family member affected by Amyotrophic Lateral Sclerosis | numeric | 0, Unchecked \| 1, Checked |
| fhalz | Family member affected by Alzheimer's Disease | numeric | 0, Unchecked \| 1, Checked |
| fharth | Family member affected by Arthritis | numeric | 0, Unchecked \| 1, Checked |
| fhasth | Family member affected by Asthma | numeric | 0, Unchecked \| 1, Checked |
| fhcanc | Family member affected by Cancer | numeric | 0, Unchecked \| 1, Checked |
| fhcirc | Family member affected by Circulation Problems | numeric | 0, Unchecked \| 1, Checked |
| fhdem | Family member affected by Dementia | numeric | 0, Unchecked \| 1, Checked |
| fhdiab | Family member affected by Diabetes | numeric | 0, Unchecked \| 1, Checked |
| fhdown | Family member affected by Down's Syndrome | numeric | 0, Unchecked \| 1, Checked |
| fhftd | Family member affected by Frontotemporal Dementia | numeric | 0, Unchecked \| 1, Checked |
| fhgen | Was genetic testing for ALS/Dementia/FTD performed | numeric | 1, Yes \| 2, No |
| fhgnang | Family member has ANG mutation | numeric | 0, Unchecked \| 1, Checked |
| fhgnc9 | Family member has C9ORF72 mutation | numeric | 0, Unchecked \| 1, Checked |
| fhgnfus | Family member has FUS mutation | numeric | 0, Unchecked \| 1, Checked |
| fhgnot | Family Member Has Other Gene Mutation | numeric | 0, Unchecked \| 1, Checked |
| fhgnotsp | Specify other ALS mutation identified in family member | text |  |
| fhgnprg | Family member has Progranulin mutation | numeric | 0, Unchecked \| 1, Checked |
| fhgnsetx | Family member has SETX mutation | numeric | 0, Unchecked \| 1, Checked |
| fhgnsod1 | Family member has SOD1 mutation | numeric | 0, Unchecked \| 1, Checked |
| fhgntau | Family member has TAU mutation | numeric | 0, Unchecked \| 1, Checked |
| fhgntdp | Family member has TDP-43 mutation | numeric | 0, Unchecked \| 1, Checked |
| fhgnvapb | Family member has VAPB mutation | numeric | 0, Unchecked \| 1, Checked |
| fhgnvcp | Family member has VCP mutation | numeric | 0, Unchecked \| 1, Checked |
| fhhbp | Family member affected by High Blood Pressure | numeric | 0, Unchecked \| 1, Checked |
| fhhd | Family member affected by Huntington's Disease | numeric | 0, Unchecked \| 1, Checked |
| fhhrt | Family member affected by Heart Disease | numeric | 0, Unchecked \| 1, Checked |
| fhlung | Family member affected by Lung Disease | numeric | 0, Unchecked \| 1, Checked |
| fhot | Family member affected by Other Disease | numeric | 0, Unchecked \| 1, Checked |
| fhotsp | Specify Other Disease family member affected by | text |  |
| fhpd | Family member affected by Parkinson's Disease | numeric | 0, Unchecked \| 1, Checked |
| fhpsy | Family member affected by Psychiatric Disorder | numeric | 0, Unchecked \| 1, Checked |
| fhpsysp | Specify psychiatric disorder family member affected by | text |  |
| fhstk | Family member affected by Stroke | numeric | 0, Unchecked \| 1, Checked |
| Form_Name | The name of this form | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## Medical_History

Form label: Medical History. Fields: 9.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Form_Name | The name of this form | numeric |  |
| medhx1 | A detailed medical history was obtained | numeric | 1, Yes \| 2, No |
| medhxdsc | Medical condition description | text |  |
| medhxprs | Medical condition still present | numeric | 1, Yes \| 2, No |
| medhxyr | Date medical condition was diagnosed, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
| Visit_Date | Date form filled, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| Visit_Name | The number of visits up to and including this visit for this participant | numeric |  |

## NEUROLOG

Form label: Neurological Disease Log. Fields: 22.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| d1ag0 | Diagnosis (Neuroinflammatory Disorders) | numeric | 63, Acute Disseminated Encephalomyelitis (ADEM) \| 64, Multiple Sclerosis (MS) \| 65, Neuromyelitis Optica (NMO) \| 66, Other Neuroinflammatory Disorder (Type) |
| d1ag1 | Diagnosis (Neuro-oncological Disorders) | numeric | 67, Acoustic Neuroma \| 68, CNS Lymphoma \| 69, Glioblastoma \| 70, Meningioma \| 71, Other Neuro-oncological Disorder (Type) |
| d1ag2 | Diagnosis (Neuro-ophthalmology Disorders) | numeric | 72, Ischemic Optic Neuropathy \| 73, Norrie Disease \| 74, Other Neuro-ophthalmology Disorder (Type) |
| d1ag3 | Diagnosis (Neurovascular Disorders) | numeric | 75, CNS Vasculitis \| 76, Hemorrhagic Stroke \| 77, Ischemic Stroke \| 78, Subarachnoid Hemorrhage (SAH) \| 79, Subdural Hemorrhage (SDH) \| 80, Other Neurovascular Disease (Type) |
| d1ag4 | Diagnosis (Seizure Disorder) | numeric | 81, Benign Rolandic Epilepsy \| 82, Juvenile Myoclonic Epilepsy \| 83, Temporal Lobe Epilepsy \| 84, Other Seizure Disorder (Type) |
| date1 | Diagnosis Date, given in relative number of days elapsed (+/-) since this participant's screening visit | numeric |  |
| diag1 | Diagnosis (Behavioral Neurology) | numeric | 1, Attention Deficit Disorder \| 2, Autism \| 3, Tourette Syndrome \| 4, Other Behavioral Neurology Disorder |
| diag2 | Diagnosis (Dementia) | numeric | 5, Alzheimer's Dementia \| 6, FTD; Amnestic \| 7, FTD; Behavioral Variant \| 8, FTD; Primary Progressive Aphasia (PPA) \| 9, Lewy Body Dementia \| 10, Prion Disease (Type) \| 11, Other Dementia (Type) |
| diag3 | Diagnosis (Headache Disorder) | numeric | 12, Hemiplegic Migraine \| 13, Migraine; Complicated \| 14, Migraine; Uncomplicated \| 15, Tension Headaches \| 16, Other Headache Disorder (Type) |
| diag4 | Diagnosis (Leukodystrophy) | numeric | 17, Adrenoleukodystrophy (ALD) \| 18, Canavan \| 19, Late Onset Tay-Sachs (LOTS) \| 20, Other Leukodystrophy Disease (Type) |
| diag5 | Diagnosis (Motor Neuron Diseases) | numeric | 21, Amyotrophic Lateral Sclerosis (ALS) \| 22, Distal Spinal Muscular Atrophy (dSMA) \| 23, Hereditary Spastic Paraplegia (HSP) \| 24, Hirayama Disease \| 25, Kennedy's Disease (SBMA) \| 26, Post-Polio Syndrome \| 27, Spinomuscular Atrophy (SMA) \| 28, Primary Lateral Sclerosis \| 29, Progressive spinal muscular atrophy \| 30, Other Motor Neuron Disease (Type) |
| diag6 | Diagnosis (Movement Disorders) | numeric | 31, Ataxia Telangiectasia \| 32, Cerebral Palsy (CP) \| 33, Cortical Basilar Degeneration (CBD) \| 34, DYT3 Dystonia \| 35, Friedrich's Ataxia \| 36, Huntington's Disease (HD) \| 37, Multisystem Atrophy (MSA) \| 38, Parkinson's Disease (PD) \| 39, Progressive Supranuclear Palsy (PSP) \| 40, Spinocerebellar Ataxia (Type) \| 41, Other Movement Disorder (Type) |
| diag7 | Diagnosis (Muscle Diseases) | numeric | 42, Muscular Dystrophy (Type) \| 43, Myopathy (Type) \| 44, Myositis (Type) \| 45, Myotonic Disorder (Type) \| 46, Periodic Paralysis \| 47, Other Muscle Disease (Type) |
| diag8 | Diagnosis (Nerve/Nerve Root Diseases) | numeric | 48, Brachial Plexopathy \| 49, Charcot-Marie-Tooth Disease (CMT) \| 50, Chronic Inflammatory Demyelinating Polyneuropathy (CIDP) \| 51, Guillain-Barre Syndrome (GBS) \| 52, Lumbosacral Plexopathy \| 53, Multifactor Motor Neuropathy (MMN) \| 54, Polyneuropathy (Type) \| 55, Radiculopathy (Level) \| 56, Vasculitic Neuropathy \| 57, Other Neuropathy/Radiculopathy (Type) |
| diag9 | Diagnosis (Neuroinfectious Disorders) | numeric | 58, Infectious Encephalopathy (Specify) \| 59, Neuro Lyme \| 60, Neuro Syphilis \| 61, West Nile Virus (Specify Involvement) \| 62, Other Neuroinfectious Disease (Type) |
| Form_Name | The name of this form | numeric |  |
| hidden1 | Diagnosis Category | numeric |  |
| hidden2 | Disease Name | numeric |  |
| neuro | Neurological Disease Diagnosis | numeric | 1, Behavioral Neurology \| 2, Dementia \| 3, Headache Disorder \| 4, Leukodystrophy \| 5, Motor Neuron Diseases \| 6, Movement Disorders \| 7, Muscle Diseases \| 8, Nerve/Nerve Root Diseases \| 9, Neuroinfectious Disorders \| 10, Neuroinflammatory Disorders \| 11, Neuro-oncological Disorders \| 12, Neuro-ophthalmology Disorders \| 13, Neurovascular Disorders \| 14, Seizure Disorder |
| other | Diagnosis (Other/Type/Specify) | text |  |
| Participant_ID | Answer ALS Participant ID | numeric |  |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |

## subjects

Form label: Study Disease Group Assignment. Fields: 3.

| Field name | Label | Type | Coded values |
|---|---|---|---|
| Participant_ID | Answer ALS Participant ID | numeric |  |
| subject_group_id | Subject Study Disease Group | numeric | 1, ALS \| 5, Healthy Control \| 11, Asymptomatic ALS Gene carrier \| 17, Non-ALS MND |
| SubjectUID | Subject Global Unique Identifier (GUID) | numeric |  |
