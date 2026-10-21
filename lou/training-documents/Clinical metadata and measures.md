Document Title: Clinical Metadata and Measures
Knowledge Base: KB 2: Data & Science Reference
Category: User-Facing Guide
Platform: Neuromine Data Portal (Answer ALS)
Support Contact: data@answerals.org
Last Updated: March 30, 2026
Version: 1.0

---

## Purpose

This document provides answers to frequently asked questions about the clinical data available on the Neuromine Data Portal — what fields exist, what they mean clinically, how key measures are collected and calculated, and where to find reference documentation. It covers both the Answer ALS and ALS TDI datasets, with clear distinctions between them where their data, methods, or fields differ. This guide is intended for use as a training resource for an LLM-based conversational assistant and should be referenced when users ask questions about clinical variables, assessment scales, subject group definitions, study design, diagnostic criteria, or the clinical data dictionary.

This document covers clinical interpretation and methodology. For field inventories, completeness percentages, participant counts, and value distributions, see the Data Catalog Overview. For omics-specific methodology, see the Omics Processing and File Formats guide.

---

## Overview

The Neuromine Data Portal hosts two distinct clinical datasets: **Answer ALS** and **ALS TDI** (ALS Therapy Development Institute / ARC Study). These datasets were collected using different study designs, at different types of sites, with different instruments, and they contain different clinical fields. Answer ALS data was collected in clinic by physicians at academic ALS centers. ALS TDI data was primarily self-reported by participants via online surveys from home. When answering questions about clinical data, it is important to specify which dataset is being described, as the answer frequently differs between the two.

---

## Section 1: Clinical Data Dictionary

*Users frequently ask where to find documentation for the clinical variables in the portal. The clinical data dictionary is the primary reference for understanding field names, values, and meanings. The bot previously gave vague answers about the dictionary's location or provided links that may be outdated. This section provides the current, accurate path to finding the dictionary for each dataset.*

---

Q: Where can I find the clinical data dictionary?

Context: *Users need to know where the data dictionary is and how to access it. The bot previously gave general descriptions or pointed to links that may not be current. The dictionary is included in the metadata download package, not available as a standalone page.*

A: The clinical data dictionary is included in the metadata package for each dataset. To access it:

1. Go to the **Datasets** tab on the Neuromine Data Portal.
2. Select the dataset you are interested in (**Answer ALS** or **ALS TDI**).
3. Click **Next**.
4. Click **Download Data**.
5. Find the **"Metadata and Clinical Data"** card, which has download buttons.

The dictionary is included in that package. Each dataset has its own clinical data dictionary.

Note: *Do not provide direct download links to the clinical data dictionary. The file name and location may change between releases. Always direct users to the Datasets tab path described above.*

---

Q: What is the clinical data dictionary and what does it contain?

Context: *Users want to understand what they will find in the dictionary before downloading it. Some expect a glossary; others expect a full codebook. The dictionary is a structured CSV file.*

A: The clinical data dictionary is a CSV file that lists every variable in the clinical dataset. For each variable, it provides:

- **Form Name**: which survey or assessment form the variable belongs to
- **Field Name**: the variable name as it appears in the data files
- **Field Label**: a human-readable description of what the variable captures
- **Values**: the possible coded values and their meanings (for categorical fields)
- **Field Type**: whether the field is numeric, text, or another type

The Answer ALS dictionary covers over 30 clinical forms, including diagnosis, history, functional assessments, cognitive screens, medications, vitals, and biospecimen collection records. The ALS TDI dictionary covers survey-based forms including ALSFRS-R, activity tracking, medications, supplements, and participant surveys.

For a full list of what clinical data files are included in each dataset, refer to the data dictionary and the readme included in the download package.

---

Q: Is there a separate clinical data dictionary for ALS TDI?

Context: *Users sometimes assume there is only one dictionary covering both datasets, or that the Answer ALS dictionary applies to ALS TDI. Each dataset has its own dictionary with its own variables and structure.*

A: Yes. Answer ALS and ALS TDI each have their own clinical data dictionary. The dictionaries are located in the same place on the portal — Datasets tab > select the dataset > Next > Download Data > "Metadata and Clinical Data" card — but you must select the correct dataset (Answer ALS or ALS TDI) to get the corresponding dictionary. The two dictionaries contain different variables reflecting the different data collection methods used in each study.

---

## Section 2: Study Design and Data Collection

*Users ask about how the clinical data was collected, whether it comes from observational studies or clinical trials, and what the difference is between the two datasets. The bot previously conflated Answer ALS with the ARC study, describing ARC's home-based data collection methods when users asked about Answer ALS. This section provides accurate, dataset-specific answers.*

---

Q: How was the Answer ALS clinical data collected?

Context: *This is a common question. The bot previously described home-based surveys and wearable accelerometers, which are characteristics of the ALS TDI/ARC study, not Answer ALS. Answer ALS data was collected in clinic by physicians. Getting this distinction right is critical.*

A: Answer ALS is a prospective, multi-center, longitudinal observational study. Clinical data was collected **in clinic by physicians** at approximately six Northeast ALS Consortium (NEALS) centers in the United States. The study was coordinated by Johns Hopkins University School of Medicine and Massachusetts General Hospital.

Participants underwent a screening visit followed by in-clinic follow-up visits every three months for one year, with optional continued follow-up every three months thereafter. At each visit, physicians performed standardized clinical assessments including functional ratings, cognitive screens, respiratory testing, strength measurements, and diagnostic evaluations. Data was entered into a secure electronic data capture system (NeuroBANK) and linked to each participant by a unique identifier.

The study protocol is Answer ALS-001, version 4.0 (October 24, 2016). The protocol and annotated electronic case report forms (eCRF) are included in the methodology folder of the Answer ALS download package.

Note: *Do not describe Answer ALS data collection using terms like "home surveys," "online surveys," "wearable accelerometers," or "voice recordings." These are characteristics of the ALS TDI/ARC study. Answer ALS data was collected in person at clinical sites. The bot has previously made this error — it must not be repeated.*

---

Q: Is Answer ALS an observational study?

Context: *Users have asked whether Answer ALS is an observational study, a phase 0 cohort, or a clinical trial. The bot previously could not answer this question. The protocol clearly describes it as an observational study with no experimental intervention.*

A: Yes. Answer ALS is a prospective observational cohort study. It is not a clinical trial and involves no experimental intervention. The study was designed to collect comprehensive clinical, genetic, molecular, and cellular data from a large population of ALS and motor neuron disease participants to support research and discovery. The study was conducted under IRB oversight in compliance with Good Clinical Practice (GCP) and ICH guidelines.

---

Q: How was the ALS TDI clinical data collected?

Context: *Users need to understand the data collection methods for the ALS TDI dataset, which are fundamentally different from Answer ALS. ALS TDI data is primarily self-reported from home.*

A: ALS TDI clinical data comes from the ALS Research Collaborative (ARC) study, run by the ALS Therapy Development Institute. Data was primarily **self-reported by participants via online surveys from home**. The dataset includes ALSFRS-R self-assessments, accelerometer sessions, voice recordings, blood draws, and extensive surveys covering medical history, lifestyle, family history, hospitalizations, injuries, medications, supplements, clinical trials, and geography.

Timepoints in the ALS TDI data are recorded as days since sign-up and days since symptom onset, rather than numbered clinic visits.

---

Q: What is the difference between Answer ALS and ALS TDI clinical data?

Context: *Users sometimes assume the two datasets were collected the same way or contain the same fields. The bot has previously mixed them up. This question requires a clear side-by-side distinction.*

A: The two datasets differ in study design, data collection method, and available clinical fields:

- **Answer ALS**: In-clinic data collected by physicians at academic ALS centers. Includes physician-administered functional assessments (ALSFRS-R, ALS-CBS, SVC, HHD, Ashworth, CNS-LS, Reflexes), diagnostic evaluations (El Escorial criteria with EMG findings), vital signs, labs, and biospecimen records. Visit schedule was every three months.
- **ALS TDI**: Home-based data collected via self-reported online surveys. Includes self-reported ALSFRS-R, accelerometer activity sessions, voice recordings, blood draws, CBC/CMP labs, and extensive patient surveys. Data is timestamped by days since sign-up.

The clinical data dictionaries for each dataset list the specific fields available. Do not assume that a field present in one dataset exists in the other.

---

## Section 3: Subject Groups and Phenotype Definitions

*Users ask about how participants are categorized and what the subject group labels mean. The bot previously gave vague or incorrect answers about phenotype information, often referencing iPSC lines instead of clinical classification fields. This section explains the clinical meaning of each subject group and where to find the classification in the data.*

---

Q: What are the Answer ALS subject groups and how are they defined?

Context: *Users encounter subject group labels in the data and need to understand the clinical criteria behind them. The bot previously could not explain these categories with specifics. The authoritative source is the `subject_group_id` field in `subjects.csv`, which was reviewed by clinicians involved in the study.*

A: Answer ALS participants are classified into four subject groups. The authoritative field is **`subject_group_id`** in the **`subjects.csv`** file included in the clinical data package. This classification was reviewed by clinicians involved in study administration and reflects the current best clinical understanding of each participant's status.

- **ALS**: Participants diagnosed with familial or sporadic ALS as possible, laboratory-supported probable, probable, or definite according to the Revised El Escorial Criteria. The study criteria were later expanded to also include suspected diagnoses.
- **Non-ALS MND**: Participants with clinically diagnosed motor neuron disorders other than ALS, including Primary Lateral Sclerosis (PLS), flail arm ALS, Progressive Muscular Atrophy (PMA), monomelic amyotrophy, and other clinical variants of neurodegenerative motor neuron disease.
- **Asymptomatic ALS Gene Carrier**: Participants with documented presence of a gene known to cause ALS who had no symptoms at the time of enrollment.
- **Healthy Control**: Participants with no known history or diagnosis of ALS or motor neuron disease, no positive family history of ALS or MND, and no unstable psychiatric disease, cognitive impairment, or dementia.

When assigning participants to disease cohorts for analysis, use the `subject_group_id` as the primary reference. Any apparent inconsistencies between this field and other data fields (such as El Escorial data or diagnosis entries) were reviewed by clinicians, and the `subject_group_id` reflects the corrected classification.

Note: *If a user asks about specific inconsistencies in the data (e.g., a healthy control with an ALS diagnosis entry, or a Non-ALS MND participant with ALS-specific forms completed), explain that these were reviewed by clinicians and the `subject_group_id` takes precedence. ALS-specific forms were sometimes used to record data for Non-ALS MND participants and should be interpreted accordingly. For detailed questions about individual participant classifications, direct users to data@answerals.org.*

---

Q: What does "Non-ALS MND" mean?

Context: *Users encounter this label and are unsure what diagnoses it includes. The term "motor neuron disease" is broad and can cause confusion.*

A: In the Answer ALS dataset, "Non-ALS MND" (Non-ALS Motor Neuron Disease) includes participants with motor neuron disorders that are clinically distinct from ALS. This group includes diagnoses such as:

- **Primary Lateral Sclerosis (PLS)**: a purely upper motor neuron disorder
- **Progressive Muscular Atrophy (PMA)**: a purely lower motor neuron disorder
- **Flail arm ALS**: a regional variant affecting primarily the upper limbs
- **Monomelic amyotrophy**: a focal motor neuron condition
- **Other clinical variants** of neurodegenerative motor neuron disease

The `SUBJECT_SUBGROUP` field in the portal index provides additional subclassification where available (e.g., "Primary Lateral Sclerosis").

---

Q: What does "Asymptomatic ALS Gene Carrier" mean?

Context: *Users have asked this specific question. The bot previously gave a generic genetics explanation rather than the portal's specific definition. The criteria are straightforward.*

A: An Asymptomatic ALS Gene Carrier is a participant who has documented genetic testing confirming the presence of a gene known to cause ALS but who had **no symptoms of ALS or motor neuron disease at the time of enrollment**. These participants are included in the study to support research into pre-symptomatic disease and potential biomarkers of disease onset.

---

Q: What are the ALS TDI participant types?

Context: *Users working with ALS TDI data encounter the `participant_type` field and want to understand the categories. The ALS TDI study provides less detailed clinical classification than Answer ALS.*

A: ALS TDI participants are classified into four types in the **`participant_type`** field of **`TDI_OVERVIEW`**:

- **ALS Patient**
- **Healthy Volunteer**
- **Asymptomatic Carrier**
- **ALS Reversal**: patients who received an ALS diagnosis and are included in Dr. Richard Bedlack's ALS Reversals program

For detailed definitions of ALS TDI participant types, refer to the ALS TDI data dictionary and documentation included in the ALS TDI download package.

---

Q: Where is phenotype information stored in the clinical data?

Context: *Users sometimes cannot find phenotype or classification information on the portal. The bot previously gave vague answers about iPSC lines rather than directing users to the correct clinical fields.*

A: Phenotype and disease classification information is stored in the following locations:

- **Answer ALS**: The **`subject_group_id`** field in **`subjects.csv`** provides the primary disease classification (ALS, Non-ALS MND, Asymptomatic ALS Gene Carrier, Healthy Control). The **`SUBJECT_SUBGROUP`** field provides additional subclassification. Diagnostic detail including El Escorial criteria classification is in the **`AALSDXFX`** (ALS Diagnosis) form. Site of onset is in the **`AALSHXFX`** (ALS History) form.
- **ALS TDI**: The **`participant_type`** field in **`TDI_OVERVIEW`** provides the primary classification. Diagnosis and onset information are also in `TDI_OVERVIEW`.

For field-level detail, refer to the clinical data dictionary for the relevant dataset.

Note: *Do not direct users to iPSC line information when they ask about phenotype. Phenotype in this context refers to clinical disease classification, not cell line characteristics.*

---

## Section 4: ALSFRS-R Score, Change, and Slope

*The ALSFRS-R is the most frequently asked-about clinical measure on the portal. Users ask how it is collected, what the scores mean, how change and slope are calculated, and which timepoints are used. The bot previously gave textbook definitions and generic formulas instead of portal-specific answers. It also conflated Answer ALS and ALS TDI collection methods. This section provides accurate, dataset-specific answers.*

---

Q: What is the ALSFRS-R?

Context: *Users sometimes need a basic orientation to the scale before asking more specific questions. A brief description is appropriate, but the answer must stay focused on how the scale is used on this portal, not a neurology textbook explanation.*

A: The ALS Functional Rating Scale-Revised (ALSFRS-R) is a questionnaire-based scale that measures and tracks changes in a person's physical function over time. It consists of 12 items covering speech, salivation, swallowing, handwriting, cutting food, dressing/hygiene, turning in bed, walking, climbing stairs, and three respiratory items (dyspnea, orthopnea, respiratory insufficiency). Each item is scored from 0 (unable to perform) to 4 (normal function), for a total possible score of 48. Lower scores indicate greater functional impairment.

Both the Answer ALS and ALS TDI datasets include longitudinal ALSFRS-R assessments. For item-level definitions and scoring values, refer to the clinical data dictionary for the relevant dataset.

---

Q: How is ALSFRS-R collected in the Answer ALS dataset?

Context: *The bot previously described home-based monthly surveys, which is the ALS TDI collection method, not Answer ALS. Answer ALS ALSFRS-R was administered in clinic. This distinction is critical.*

A: In the Answer ALS dataset, the ALSFRS-R was **administered in clinic at each study visit** — at the screening visit and at follow-up visits every three months. The mode of administration is recorded for each assessment (in person, telephone, self-administered, or other). The ALSFRS-R could also be administered via telephone if the in-person visit was missed.

Each assessment is linked to a visit number and a visit date (recorded as days elapsed since the screening visit). The **`ALSFRS_R.csv`** file in the full clinical data package contains the longitudinal item-level scores and total scores for each participant.

Note: *Do not describe Answer ALS ALSFRS-R collection as "monthly surveys" or "online self-report." It was physician-administered in clinic. The bot has previously given incorrect information on this point.*

---

Q: How is ALSFRS-R collected in the ALS TDI dataset?

Context: *Users working with ALS TDI data need to understand that ALSFRS-R in this dataset is self-reported, not clinician-administered.*

A: In the ALS TDI dataset, the ALSFRS-R is **self-reported by participants via online surveys from home**. Participants can complete assessments frequently — some participants have over 100 ALSFRS-R entries. Each assessment is timestamped with days since sign-up and days since symptom onset. The **`TDI_ALSFRS-R`** table contains the item-level scores and total score for each assessment.

---

Q: How is the ALSFRS-R progression slope calculated in Answer ALS?

Context: *This is one of the most commonly asked clinical questions in the conversation log. The bot previously gave a generic "points lost per month" formula without referencing the portal's actual calculation. Users need the specific method.*

A: The Answer ALS dataset includes a pre-calculated field: **`ALSFRS_R_PROGRESSION_SLOPE`**, described as "The revised ALS functional rating scale progression score represented as points/month. Calculated by NeuroBANK."

The slope is calculated using **simple linear regression** — specifically, the same method as the Excel SLOPE function, which fits a least-squares regression line through the available ALSFRS-R scores over time and returns the slope in points per month.

This field is available in the release index file and in the portal's data search interface. Negative values indicate functional decline (the typical pattern in ALS). For example, a value of -0.625 means the participant's ALSFRS-R score declined by approximately 0.625 points per month on average.

The dataset also provides **`ALSFRS_R_Baseline_Value`** (score at the first visit) and **`ALSFRS_R_Latest_Value`** (score at the most recent visit). Change can be derived from these two values.

Note: *Do not provide a generic formula for slope calculation. Always reference the pre-calculated field and the simple linear regression method. If a user asks about calculating slope themselves from raw data, point them to the longitudinal ALSFRS-R scores in the clinical data package and note that the portal's pre-calculated slope uses simple linear regression via NeuroBANK.*

---

Q: How is the ALSFRS-R slope calculated in ALS TDI?

Context: *Users working with ALS TDI data ask the same question. The method is documented in the Data Catalog.*

A: The ALS TDI dataset includes a pre-calculated field: **`ALSFRS_Slope`**, defined as "ALSFRS-R slope in points per month based on simple linear regression." This field is available in the portal's data search interface. The method is the same approach as Answer ALS — simple linear regression applied to the longitudinal ALSFRS-R scores.

---

## Section 5: Other Clinical Assessments and Scales

*Users ask about what clinical measures exist beyond ALSFRS-R. This section covers the other assessments available in the Answer ALS dataset and corrects a specific prior bot error about the CNS Lability Scale.*

---

Q: What clinical assessments are available in the Answer ALS dataset?

Context: *Users want to know the full scope of clinical data collected. The Answer ALS protocol included a comprehensive battery of clinical assessments administered at each visit.*

A: The Answer ALS dataset includes the following clinical assessments, collected at the screening visit and at follow-up visits every three months:

**Functional and Cognitive:**
- **ALSFRS-R** (ALS Functional Rating Scale-Revised): functional ability across 12 daily activity domains
- **ALS-CBS** (ALS Cognitive Behavioral Screen): short measure of cognition (8 tasks, max score 20) and behavior (caregiver questionnaire)

**Motor and Physical:**
- **HHD** (Hand Held Dynamometry): quantitative muscle strength measurement across multiple muscle groups
- **Grip Strength Testing**: bilateral handgrip force
- **Ashworth Spasticity Scale**: muscle tone and spasticity, scored 1–5 per limb
- **Reflexes**: deep tendon, pathologic, and cranial reflex scores by body region

**Respiratory:**
- **SVC** (Slow Vital Capacity): upright respiratory function testing via spirometry
- **Vital Capacity**: includes FVC (forced vital capacity) measurements

**Upper Motor Neuron Assessment:**
- **CNS-LS** (Center for Neurologic Study-Lability Scale): 7-item self-report scale measuring pseudobulbar affect
- The CNS-LS, Ashworth, and Reflexes are collectively part of the **Penn Upper Motor Neuron-Burden (UMN-B)** assessment

**Diagnostic:**
- **El Escorial Criteria** evaluation with EMG findings by body region
- ALS history including site of onset, date of symptom onset, and date of diagnosis

**Demographics and History:**
- Demographics, medical history, family history, environmental questionnaire, medications log, vital signs

**Biospecimen Records:**
- Collection records for PBMC, DNA, plasma, serum, and CSF samples

For item-level detail on any of these assessments, refer to the clinical data dictionary. The annotated eCRF (electronic case report forms) document in the methodology folder shows the exact forms used for data collection.

Note: *Not all of these assessments were administered to healthy controls. See the question about healthy control data in this section for details.*

---

Q: What scale measures CNS lability or pseudobulbar affect?

Context: *A user previously asked this question and the bot incorrectly stated that CNS lability is measured by the ALSFRS-R. This is wrong — pseudobulbar affect is not assessed by the ALSFRS-R. The correct scale is the CNS-LS. This error must be explicitly corrected.*

A: CNS lability (pseudobulbar affect) is measured by the **Center for Neurologic Study-Lability Scale (CNS-LS)**, not the ALSFRS-R. The CNS-LS is a 7-item self-report scale that assesses the perceived frequency of involuntary laughing or crying episodes. Each item is scored from 1 ("Does not apply") to 5 ("Applies most of the time"), producing a total score.

In the Answer ALS dataset, CNS-LS data is in the **`CNS_Lability_Scale.csv`** file in the full clinical data package. The CNS-LS is part of the Penn Upper Motor Neuron-Burden (UMN-B) assessment battery.

The ALSFRS-R does not measure pseudobulbar affect. It assesses functional abilities such as speech, swallowing, and mobility.

Note: *The bot previously gave an incorrect answer on this topic, stating that the ALSFRS-R measures CNS lability. This is factually wrong and was corrected by the user in the conversation. Always use the answer above. If a user asks about pseudobulbar affect, emotional lability, or involuntary laughing/crying, point to the CNS-LS, not the ALSFRS-R.*

---

Q: What is the ALS-CBS?

Context: *Users encounter CBS fields in the data and want to understand what this assessment measures.*

A: The ALS Cognitive Behavioral Screen (ALS-CBS) is a short measure of cognition and behavior in ALS patients. It has two parts:

- **Cognitive section**: consists of 8 tasks testing attention, concentration, tracking, and initiation/retrieval, with a possible total score of 20. Administered by a physician or clinical staff in approximately 5 minutes.
- **Behavioral section** (ALS Caregiver Questionnaire): completed by a caregiver or family member. Captures observed changes in personality and behavior since ALS onset, plus yes/no questions about mood, pseudobulbar affect, and fatigue.

The portal provides pre-calculated summary fields: **`CBS_Baseline_Value`**, **`CBS_Latest_Value`**, and **`COGNITIVE_PROGRESSION_SLOPE`** (CBS progression score in points/month, calculated by NeuroBANK). Item-level data is in the **`ALS_CBS.csv`** file in the full clinical data package.

---

Q: Is there respiratory function data?

Context: *Users ask about respiratory data, which is clinically important for tracking ALS progression.*

A: Yes. The Answer ALS dataset includes **Slow Vital Capacity (SVC)** measurements, collected via upright spirometry at each study visit. SVC is a standard measure of respiratory function used to monitor diaphragmatic weakness and disease progression in ALS. The **`Vital_Capacity.csv`** file in the full clinical data package contains the respiratory measurements. The ALSFRS-R also includes three respiratory items (dyspnea, orthopnea, respiratory insufficiency).

---

Q: What clinical data is available for healthy controls compared to ALS participants?

Context: *Users ask whether healthy controls have the same clinical data as ALS participants. They do not — controls received a subset of assessments.*

A: Healthy controls in the Answer ALS dataset received a subset of the clinical assessments. Specifically:

**Collected for healthy controls:**
- Demographics
- Medical history
- Environmental questionnaire
- Vital signs (height, weight, blood pressure, heart rate, temperature)
- Concomitant medication review
- Hand Held Dynamometry (optional)
- Biospecimen collection (PBMC, DNA, plasma, serum, CSF optional)
- Adverse event review

**Not collected for healthy controls:**
- ALSFRS-R
- ALS-CBS (Cognitive Behavioral Screen)
- Slow Vital Capacity (SVC)
- UMN-B assessment (CNS-LS, Ashworth Spasticity Scale, Reflexes)
- El Escorial diagnostic evaluation
- ALS history, gene mutations, or family history of ALS

Additionally, some external controls used for omics analyses have only sex and age available as demographic data.

Note: *If a user asks about control data availability for a specific modality (e.g., "do controls have proteomics data?"), refer them to the Data Catalog Overview for availability counts by subject group and modality.*

---

## Section 6: Diagnosis and Onset Fields

*Users ask about how to interpret diagnostic criteria and onset fields in the data. This section covers the El Escorial criteria used for ALS diagnosis and the site of onset fields.*

---

Q: What diagnostic criteria are used for ALS diagnosis in the portal data?

Context: *Users encounter the El Escorial criteria classification in the data and want to understand what the categories mean. Both datasets use this system.*

A: Both the Answer ALS and ALS TDI datasets classify ALS diagnosis using the **Revised El Escorial Criteria**, a standard system developed by the World Federation of Neurology. The categories, from lowest to highest certainty, are:

- **Suspected**: clinical signs of LMN dysfunction only in one or more regions
- **Possible**: clinical signs of UMN and LMN dysfunction in one region, or UMN signs in two or more regions
- **Probable Laboratory Supported**: clinical signs of UMN and LMN dysfunction in one region, with EMG evidence of LMN involvement in at least two regions
- **Probable**: clinical signs of UMN and LMN dysfunction in at least two regions, with some UMN signs above LMN signs
- **Definite**: clinical signs of UMN and LMN dysfunction in three or more regions

In the Answer ALS dataset, the El Escorial classification is in the **`elescrlr`** field of the **`AALSDXFX`** (ALS Diagnosis) form, and as the **`REVISED_EL_ESCORIAL_CRITERIA`** field in the release index. In the ALS TDI dataset, the classification is in the **`diagnosis`** field of **`TDI_OVERVIEW`**.

For questions about the clinical interpretation of a specific participant's diagnosis, contact data@answerals.org.

Note: *Lou should provide the category definitions above when asked, but should not attempt to interpret individual participant diagnoses or provide clinical guidance on what a specific El Escorial category means for a patient's prognosis. Direct those questions to data@answerals.org.*

---

Q: What does the "Site of Onset" field represent?

Context: *Users encounter site of onset fields and want to understand the categories and structure.*

A: The site of onset field records where the participant first experienced ALS symptoms. The two datasets capture this information differently:

**Answer ALS**: Onset is recorded in the **`AALSHXFX`** (ALS History) form using multiple binary fields for each body region and sub-region:
- **Bulbar**: Speech, Swallowing
- **Limb**: Upper (arm, hand) and Lower (leg, foot), with left/right laterality
- **Axial**: Neck, Trunk, Respiratory
- **Generalized**
- **Other** (with free text)

Multiple onset sites can be recorded simultaneously. The release index also includes summary fields: `Site_of_Onset`, `Bulbar_Onset`, `Axial_Onset`, `Limb_Onset`, and `Other_Onset`.

**ALS TDI**: Onset is recorded in the **`onset_site_unnested`** field of **`TDI_OVERVIEW`** as a text description of the specific body part (e.g., "Tongue," "Right Hand," "Left Foot").

---

Q: Is EMG data available on the portal?

Context: *A user asked this question and the bot gave a textbook definition of EMG rather than answering whether it exists on the portal. EMG data exists but only as part of the diagnostic evaluation, not as raw electrophysiology data.*

A: EMG findings are recorded in the Answer ALS dataset as part of the **El Escorial diagnostic evaluation** in the **`AALSDXFX`** (ALS Diagnosis) form. This includes EMG results by body region — Bulbar, Left/Right Upper Extremity, Left/Right Lower Extremity, and Trunk — recorded as Yes, No, or Not Done. These are diagnostic classification findings used to support the El Escorial criteria categorization.

This is **not** raw EMG waveform or electrophysiology study data. If you need detailed EMG study data, it is not available on the portal. Contact data@answerals.org for guidance.

EMG data is not available in the ALS TDI dataset.

---

## General Support Reference

For any clinical metadata or measures questions not covered in this document, or for issues that cannot be resolved through the information described above, users should contact the Neuromine Data Portal support team.

Support Email: data@answerals.org
