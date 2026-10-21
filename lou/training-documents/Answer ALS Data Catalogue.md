Document Title: Answer ALS Data Catalogue
Knowledge Base: KB 2: Data & Science Reference
Category: User-Facing Guide
Platform: Neuromine Data Portal (Answer ALS)
Support Contact: data@answerals.org
Last Updated: March 06, 2026
Version: r7.2.3

# Purpose

This document provides a reference catalogue of the data available in the Answer ALS dataset on the Neuromine Data Portal, including participant counts by group, data availability by modality, longitudinal timepoint distributions, and field-level descriptions for all columns in the portal's data table. It is intended as a training resource for Lou and should be referenced when users ask questions about what data is available, how many participants have a given modality, what a specific field means, or what values are expected for a given column.

# Section 1: Participant Overview

*The Answer ALS dataset contains data from participants organized into subject groups. This section covers participant counts and how data availability is summarized across the dataset. Availability flags in the source data use blank values (not missing data) to indicate No.*

Q: How many participants are in the Answer ALS dataset and what are the subject groups?

Context: Users ask about overall participant counts and how the cohort is broken down.

A: The Answer ALS dataset includes participants across four subject groups: ALS, Asymptomatic ALS Gene Carrier, Non-ALS MND, and Healthy Control. For the authoritative participant count by group, refer to the aals_dataportal_datatable.csv included in the download package. The subject_group_id field in subjects.csv is the most accurate and up-to-date classification of each participant's disease status.

---

Q: How many participants have each data modality available?

Context: Users ask about how broadly each data type is represented in the cohort before deciding to download.

A: The following data modalities are available and their participant counts as of the current release:

- **Epigenomics** (HAS_EPIGENOMICS): 1,039 participants
- **Transcriptomics** (HAS_TRANSCRIPTOMICS): 1,102 participants
- **Proteomics** (HAS_PROTEOMICS): 1,094 participants
- **Genomics / WGS** (HAS_GENOMICS): 939 participants
- **diMN lines** (HasDIMN): 1,062 participants
- **iPSC lines** (HasIPSC): 726 participants available through Cedars-Sinai or CIRM
- **NfL data** (HAS_NFL): 911 participants
- **SomaScan data** (HAS_SOMASCAN): 357 participants

For availability flags, a blank value in the source data means No — it is not missing data.

These counts reflect all participants across all subject groups. For group-specific counts (e.g., ALS only), filter by SUBJECT_GROUP before counting.

These are independent modality totals, not counts of the same participant set.
They describe how many participants have each flag, but do not establish that
participants counted under two different modalities are the same people.

---

Q: How many participants have data available across multiple modalities simultaneously?

Context: Users ask how many participants have both WGS and proteomics (or any other combination of modalities), often to understand the usable sample size for a multi-omic analysis.

A: The counts listed above are **independent per modality** — a participant counted under Genomics is not necessarily also counted under Proteomics. Do not assume that the smaller of two modality counts is a subset of the larger. To determine how many participants have two or more modalities simultaneously, the availability flags must be combined (i.e., both HAS_GENOMICS and HAS_PROTEOMICS must be Yes for the same participant). The intersection is always smaller than or equal to the smaller individual count, and must be computed directly — it cannot be inferred from the individual totals alone.

Example: If 774 ALS participants have HAS_GENOMICS=Yes and 716 have HAS_PROTEOMICS=Yes, the number with **both** is not 716 — it must be calculated separately (and may be lower).

---

Q: How is longitudinal biomarker data distributed across timepoints?

Context: Users ask how many participants have multiple timepoints for the longitudinal assays before deciding whether to use them for longitudinal analysis.

A: Longitudinal timepoint distribution for the two post-study biomarker assays:

**NfL (NFL_TIMEPOINTS_AVAILABLE)**
- 911 participants have at least one NfL timepoint.

**SomaScan (SOMASCAN_TIMEPOINTS_AVAILABLE)**
- 357 participants have at least one SomaScan timepoint.

Both assays were taken from multiple timepoints per participant. For the most common visit combinations, refer to the aals_dataportal_datatable.csv in the download package.

---

# Canonical overlap and modality corrections (P4-T12)

For WGS and RNA-seq questions, the modality totals above are independent
counts, not evidence that the same participants have both assays. Do not use
the smaller total, say that there is "some overlap," or say that the modalities
come from the same patients based only on those totals.

To determine the exact intersection, use participant-level rows and count the
same participant only when both `HAS_GENOMICS` and `HAS_TRANSCRIPTOMICS` are
Yes. If participant-level availability flags or identifiers are unavailable,
state that the exact intersection cannot be determined from the published
totals and escalate to data@answerals.org; do not estimate or infer it.

MicroRNA/miRNA/small-RNA sequencing is not part of the Answer ALS dataset.
Bulk mRNA RNA-seq is the available transcriptomics modality, and it must not be
used as evidence that miRNA is available.

Q: How should Lou correct a request that combines unavailable miRNA with WGS and RNA-seq overlap?

Context: Regression coverage for conversations where a user requests mRNA,
miRNA, and genomics data or asserts that all requested data comes from the same
patients. The conversation IDs below identify observed failure patterns; they
are not additional dataset counts.

A: Correct each premise independently. State that bulk mRNA RNA-seq and WGS are
available modalities, but microRNA/miRNA/small-RNA sequencing is not part of the
Answer ALS dataset. Then state that the WGS/RNA-seq participant intersection
cannot be inferred from the independent modality totals. Compute it only by
combining `HAS_GENOMICS` and `HAS_TRANSCRIPTOMICS` for the same participant; if
those participant-level flags or identifiers are unavailable, explicitly say so
and refer the user to data@answerals.org.

Regression examples:

- **8f6b99e9-8149-4803-873d-8bf5d42371ff** — For “Are the mRNA, miRNA, and genomics data all from the same patients?”, say that mRNA/RNA-seq and WGS are available, miRNA is unavailable, and same-patient overlap cannot be established from modality totals.
- **1ec015e9-fc8a-4057-beba-b14e341fb8b5** — When a user requests WGS, RNA-seq, miRNA, and clinical data while saying all data comes from the same patients, correct the miRNA premise and require participant-level flags (or an explicit escalation) before making an overlap claim.
- **037431f5-6e47-4b9d-bf97-b2a05576bf1c** — For “Are transcriptomics and genomics from the same patients?”, explain that the published counts are independent; calculate the intersection from same-row availability flags or say it is unavailable from the current evidence and escalate.

# Section 2: Genetic and Variant Data

*This section covers the genetic data fields available in the Answer ALS portal table, including self-reported mutations, WGS-derived variants, and repeat expansion data.*

Q: What genetic and variant data fields are available in the Answer ALS data table?

Context: Users ask about what genetic information is included in the portal table and what values to expect.

A: The following genetic and variant data fields are available:

**Self-reported Mutations (ClinReport_Mutations_Details)**
Mutations reported by participant, family, or physician during health history.
- Type: Categorical
- Completeness: 7.5%
- Values: C9orf72 (57), SOD1 (15), Other (9), Multiple (6), SETX (3), TARDBP/TDP43 (3), FUS (1), VCP (1)

**WGS Variants (HasVariant)**
A SNP was identified by sequence analysis in the indicated gene. It is not known if the SNP is correlated with disease.
- Type: Categorical
- Completeness: 3.7%
- Values: SOD1 (9), SQSTM1 (7), CHCHD1 (5), PFN1 (5), ANG (4), OPTN (4), SETX (3), UBQLN2 (2), ALS2 (2), TARDBP/TDP43 (2), FUS (1), FIG4 (1), Multiple (1), VCP (1)

**C9orf72 Repeat Length (C9orf72_repeat_length)**
Number of repeats found by Expansion Hunter software.
- Type: Numeric
- Completeness: 51.8% (n=660)
- Range: 2.0 – 1,198.0 | Mean: 38.67
- In the portal's Data Search this field is shown as **Repeat Length (C9)**. Portal display names come from the index facet settings and can differ from file column names.
- It is included in the Full Metadata download: that download contains a copy of the portal's index data table (`aals_dataportal_datatable.csv`), so anything visible in the portal table is in that file. There is no extra access restriction on this field.
- `Has_EH_C9orf72` (402 participants) is an **ALS TDI** field and does not apply to Answer ALS.

**ATXN2 Repeat Length (ATXN2_repeat_length)**
Number of repeats found by Expansion Hunter software.
- Type: Numeric
- Completeness: 51.8% (n=660)
- Range: 22.0 – 37.0 | Mean: 22.6

---

# Section 3: External Biomarker Data

*This section covers NfL and SomaScan data fields available in the portal table.*

Q: What external biomarker data fields are available and what do they mean?

Context: Users ask about the NfL and SomaScan availability flags and what source material was used.

A: **NfL Data (HAS_NFL)**
Whether the participant has neurofilament light chain (NfL) data. Source: Serum (Siemens Atellica Immunoassay).
- Type: Availability flag (blank = No)
- Values: Yes (911), No (361)

**SomaScan Data (HAS_SOMASCAN)**
Whether the participant has SomaScan Proteomics data. Source: Plasma.
- Type: Availability flag (blank = No)
- Values: Yes (357), No (915)

---

# Section 4: Cell Line Availability

*This section covers cell line availability flags in the portal table.*

Q: What cell line availability fields are in the Answer ALS data table?

Context: Users ask about which participants have cell lines available for ordering.

A: **diMN Lines (HasDIMN)**
A diMN line was used to generate the OMIC data for this participant.
- Type: Availability flag (blank = No)
- Values: Yes (1,062), No (211)

**iPSC Lines (HasIPSC)**
An iPSC line is available through Cedars-Sinai Biomanufacturing Center or CIRM (California Institute for Regenerative Medicine). Many control lines are also available through CIRM.
- Type: Availability flag (blank = No)
- Values: Yes (726), No (547)
- Ordering: To order iPSC lines, use the Resources tab on the Neuromine portal, which links to the Cedars-Sinai / CIRM distribution paths.
- Important: iPSC lines are **not** distributed through Coriell. Do not direct users to Coriell or any other distributor — Cedars-Sinai and CIRM are the correct channels.

---

# Section 5: Omics Data Availability

*This section covers the OMIC modality availability flags in the portal table.*

Q: What OMIC availability fields are in the Answer ALS data table?

Context: Users ask about which OMIC modalities are available for participants shown in search results.

A: **Epigenomics (HAS_EPIGENOMICS)**
Epigenomics data is available. Source: iPSC Derived Motor Neuron Lines.
- Type: Availability flag (blank = No)
- Values: Yes (1,039)

**Genomics (HAS_GENOMICS)**
Whole Genome Sequence data is available. Source: Blood.
- Type: Availability flag (blank = No)
- Values: Yes (939)

**Proteomics (HAS_PROTEOMICS)**
Proteomics data is available. Source: iPSC Derived Motor Neuron Lines.
- Type: Availability flag (blank = No)
- Values: Yes (1,094)

**Transcriptomics (HAS_TRANSCRIPTOMICS)**
Transcriptomics data is available. Source: iPSC Derived Motor Neuron Lines.
- Type: Availability flag (blank = No)
- Values: Yes (1,102)

---

# Section 6: Assay and Sequencing Metadata

*This section covers the assay and sequencing metadata fields available in the portal table, including quality metrics, library preparation methods, and batch information.*

Q: What assay and sequencing metadata fields are available in the Answer ALS data table?

Context: Users ask about QC fields, instrument information, and batch data to assess sample quality and plan batch correction.

A: **RIN Value (RIN_Value)**
RNA integrity number — a QC metric for RNA quality.
- Type: Numeric
- Completeness: 86.4% (n=1,100)
- Range: 5.5 – 10.0 | Mean: 9.57

**Genomic Sequencing DNA Source (Genomic_Sequencing_DNA_Source)**
Source of the genomic sequencing DNA.
- Type: Categorical
- Completeness: 73.8%
- Values: Blood (939)

**WGS Library Preparation (WGS_Sequencing_Protocol_Used)**
Indicates whether WGS used TruSeq PCR-Free or TruSeq Nano (PCR-dependent) library preparation.
- Type: Categorical
- Completeness: 73.8%
- Values: TruSeq PCR-Free (699), TruSeq Nano PCR amplification (240)

**Epigenomics Sequencing DNA Source (Epigenomic_Sequencing_DNA_Source)**
Source of the epigenomics sequencing DNA.
- Type: Categorical
- Completeness: 81.6%
- Values: iPSC Derived Motor Neuron Lines (1,039)

**Transcriptomic Sequencing DNA Source (Transcriptomic_Sequencing_DNA_Source)**
Source of the transcriptomic sequencing DNA.
- Type: Categorical
- Completeness: 86.6%
- Values: iPSC Derived Motor Neuron Lines (1,102)

**Proteomic Sequencing DNA Source (Proteomic_Sequencing_DNA_Source)**
Source of the proteomic sequencing DNA.
- Type: Categorical
- Completeness: 85.9%
- Values: iPSC Derived Motor Neuron Lines (1,094)

**Proteomics Instrument (Proteomic_Instrument)**
Instrument used for proteomics processing at the participant level.
- Type: Categorical
- Completeness: 81.9%
- Values: Thermo Fisher Scientific Orbitrap Exploris 480 (595), Sciex TripleTOF 6600 (446), both instruments (1)

**Proteomics Digestion Batch (Proteomic_Digestion_Batch)**
Proteomics digestion batch assignment.
- Type: Categorical
- Completeness: 81.9%
- Values: Thermo__10 (75), Thermo__16 (72), Thermo__12 (72), Thermo__13 (71), Thermo__14 (71), Thermo__11 (69), Thermo__15 (67), Sciex__Plate-6 (63), Sciex__Plate-9 (61), Sciex__Plate-7 (61), Sciex__Plate-4 (60), Sciex__Plate-8 (56), Thermo__17 (56), Sciex__Plate-3 (51), Sciex__Plate-2 (49), Sciex__Plate-5 (47), Thermo__18 (42)

---

# General Support Reference

For any questions about the Answer ALS Data Catalogue not covered in this document, contact the Neuromine Data Portal support team.

Support Email: data@answerals.org
