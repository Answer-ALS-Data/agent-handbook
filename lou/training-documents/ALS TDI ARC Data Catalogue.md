Document Title: ALS TDI ARC Data Catalogue
Knowledge Base: KB 2: Data & Science Reference
Category: User-Facing Guide
Platform: Neuromine Data Portal (ALS TDI)
Support Contact: data@answerals.org
Last Updated: March 06, 2026
Version: r1

# Purpose

This document provides a reference catalogue of the data available in the ALS TDI ARC dataset on the Neuromine Data Portal, including participant counts by type, data availability by modality, longitudinal timepoint distributions, and field-level descriptions for all columns in the portal's data table. It is intended as a training resource for Lou and should be referenced when users ask questions about what ALS TDI data is available, how many participants have a given modality, what a specific field means, or what values are expected for a given column.

# Section 1: Participant Overview

*The ALS TDI ARC dataset contains 1,290 participants. This section covers participant counts by type and how data availability is summarized across the dataset. Availability flags in the source data use blank values (not missing data) to indicate No.*

Q: How many participants are in the ALS TDI ARC dataset and what are the participant types?

Context: Users ask about the overall size and composition of the ALS TDI cohort.

A: The ALS TDI ARC dataset contains 1,290 participants. Participant types include ALS cases and healthy controls. For the authoritative breakdown by participant type, refer to the alstdiarc_dataportal_datatable.csv included in the download package. The Participant_Type field provides the group classification for each participant.

---

Q: How many ALS TDI participants have each data modality available?

Context: Users ask about data availability before deciding to download or analyze.

A: The following data modalities are available and their participant counts as of the current release:

- **Genomics** (HAS_GENOMICS): 552 participants
- **Proteomics** (HAS_PROTEOMICS): 115 participants
- **Transcriptomics** (HAS_TRANSCRIPTOMICS): 115 participants
- **C9orf72 Expansion Hunter** (Has_EH_C9orf72): 402 participants
- **ATXN2 Expansion Hunter** (Has_EH_ATXN2): 402 participants

For availability flags, a blank value in the source data means No — it is not missing data.

---

Q: How is longitudinal data distributed across timepoints for ALS TDI participants?

Context: Users ask about the longitudinal depth of the ALS TDI dataset before using it for longitudinal analysis.

A: Longitudinal data is available across four measures. Counts reflect participants with at least one timepoint (out of 1,290 total participants):

**Blood Draws (Total_Blood_Draw)**
- 279 participants have at least one blood draw timepoint.
- Range: 0 – 14 | Mean: 0.72

**ALSFRS-R Assessments (Total_ALSFRS)**
- 1,211 participants have at least one ALSFRS-R assessment.
- Range: 0 – 164 | Mean: 17.39

**Accelerometer Sessions (Total_Tracker)**
- 507 participants have at least one accelerometer session.
- Range: 0 – 114 | Mean: 6.35

**Voice Recordings (Total_Voice_Recording)**
- 785 participants have at least one voice recording.
- Range: 0 – 140 | Mean: 9.98

---

# Section 2: Clinical Data Fields

*This section covers the clinical information fields available in the ALS TDI portal data table.*

Q: What clinical data fields are available in the ALS TDI data table?

Context: Users ask about clinical variables available for filtering and analysis.

A: **Diagnosis (Diagnosis)**
Diagnosis based on El Escorial Criteria.
- Type: Categorical
- Completeness: 99.8%
- Values: definitive (911), probable (156), healthy (77), possible (67), suspected (35), asymptomatic (16), and others

**Onset Age (Onset_Age)**
Participant age at symptom onset.
- Type: Numeric
- Completeness: 90.1% (n=1,162)
- Range: 19 – 85 | Mean: 53.71

**Site of Onset (Site_of_Onset)**
Specific body section where the patient reports symptom onset. Can be multiple sites.
- Type: Categorical
- Completeness: 90.2%
- Most common values: Tongue (123), Right Hand (112), Left Foot (97), Left Hand (93), Right Foot (75); 102 unique values total

**ALSFRS Slope (ALSFRS_Slope)**
ALSFRS-R slope in points per month based on simple linear regression.
- Type: Numeric
- Completeness: 69.6% (n=898)
- Range: -7.62 – 2.06 | Mean: -0.73

**Deceased (Deceased)**
Whether the participant is deceased.
- Type: Categorical
- Completeness: 100%
- Values: No (700), Yes (590)

**Age At Sign Up (Age_At_Sign_Up)**
Participant age at the time they signed up for the ARC Study.
- Type: Numeric
- Completeness: 100% (n=1,290)
- Range: 19 – 88 | Mean: 55.2

---

# Section 3: Longitudinal Count Fields

*These fields count how many timepoints each participant contributed for each data collection task.*

Q: What longitudinal count fields are in the ALS TDI data table?

Context: Users ask about how to identify participants with sufficient longitudinal data for their analysis.

A: **Total Blood Draws (Total_Blood_Draw)**
Total blood draws conducted for the participant.
- Type: Numeric | Completeness: 100% (n=1,290)
- Range: 0 – 14 | Mean: 0.72

**Total ALSFRS (Total_ALSFRS)**
Total ALSFRS-R questionnaires completed.
- Type: Numeric | Completeness: 100% (n=1,290)
- Range: 0 – 164 | Mean: 17.39

**Total Accelerometer Sessions (Total_Tracker)**
Total accelerometer sessions completed.
- Type: Numeric | Completeness: 100% (n=1,290)
- Range: 0 – 114 | Mean: 6.35

**Total Voice Recordings (Total_Voice_Recording)**
Total voice recordings submitted and scored.
- Type: Numeric | Completeness: 100% (n=1,290)
- Range: 0 – 140 | Mean: 9.98

**3 or More Data Points (Three_or_More_Data_Points)**
Whether the participant contributed 3 or more data points to any single task (e.g., 3 ALSFRS entries, 3 voice recordings, or 3 accelerometer sessions).
- Type: Categorical | Completeness: 100%
- Values: Yes (933), No (357)

---

# Section 4: Omics Data Availability

*This section covers OMIC modality and Expansion Hunter availability flags in the ALS TDI data table.*

Q: What OMIC availability fields are in the ALS TDI data table?

Context: Users ask about which OMIC data types are available for ALS TDI participants.

A: **Genomic Data (HAS_GENOMICS)**
Genomic data is available for this participant.
- Type: Availability flag (blank = No)
- Values: Yes (552)

**Proteomic Data (HAS_PROTEOMICS)**
Proteomic data is available for this participant.
- Type: Availability flag (blank = No)
- Values: Yes (115)

**Transcriptomic Data (HAS_TRANSCRIPTOMICS)**
Transcriptomic data is available for this participant.
- Type: Availability flag (blank = No)
- Values: Yes (115)

**C9orf72 Expansion Hunter (Has_EH_C9orf72)**
C9orf72 Expansion Hunter data is available for this participant.
- Type: Availability flag (blank = No)
- Values: Yes (402)

**ATXN2 Expansion Hunter (Has_EH_ATXN2)**
ATXN2 Expansion Hunter data is available for this participant.
- Type: Availability flag (blank = No)
- Values: Yes (402)

---

Q: Does ALS TDI have a joint (multi-sample) VCF file available?

Context: Users ask whether ALS TDI genomics is delivered as a single combined/joint VCF across all sequenced participants.

A: No. ALS TDI genomics is whole-genome sequencing (WGS) data, available for approximately 551–552 participants (HAS_GENOMICS = 552, blood-derived). However, a joint (multi-sample) VCF is **not currently available** for ALS TDI — one is **planned and on the roadmap** to be generated but has not yet been produced. Do not state or imply that a joint VCF exists today. For questions about genomic data formats, or about when a joint VCF may be released, contact data@answerals.org.

---

# General Support Reference

For any questions about the ALS TDI ARC Data Catalogue not covered in this document, contact the Neuromine Data Portal support team.

Support Email: data@answerals.org
