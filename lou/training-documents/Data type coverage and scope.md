Document Title: Data Type Coverage and Scope
Knowledge Base: KB 2: Data & Science Reference
Category: User-Facing Guide
Platform: Neuromine Data Portal (Answer ALS)
Support Contact: data@answerals.org
Last Updated: June 02, 2026
Version: 1.0

# Purpose

This document states which data types are part of the Answer ALS dataset on the
Neuromine Data Portal and which are not. It exists so that Lou can give a clear,
direct answer when a user asks whether a particular modality or data type is
available, instead of hedging. Use it as the first reference for any "do you
have X data?" question. For participant counts and field-level definitions, see
the **Answer ALS Data Catalogue**.

**Canonical modality rule:** Treat microRNA, miRNA, and small-RNA sequencing as
the same unavailable modality. Do not treat the presence of bulk mRNA RNA-seq
(the transcriptomics data) as evidence that miRNA or any other small-RNA assay
is available. When a user asks for both, answer each modality separately and
correct the unavailable-miRNA premise before discussing the available data.

**Two-cohort rule:** Neuromine holds two cohorts, Answer ALS and ALS TDI. Their
fields, counts, tissue sources and processing differ (for example, Answer ALS
omics come from iPSC-derived motor neurons, while all ALS TDI omics come from
blood). When the user does not name a cohort, either ask which one they mean or
answer for both with each part labelled. Never apply one cohort's fact to the
other.

**One access level:** All data, raw or processed, sits behind the same DUA.
There is no public or lighter-access tier. Files differ only in how processed
they are (from raw instrument output to processed tables), not in how they are
accessed.

# Section 1: Data Types That Are Available

The Answer ALS dataset includes the following data types. For published
participant counts, see the Answer ALS Data Catalogue.

**Multi-omics (iPSC-derived motor neuron lines, unless noted)**
- **Genomics** — whole genome sequencing (WGS), from blood
- **Epigenomics** — ATAC-seq; DNA methylation is also released as a Big Data download package
- **Transcriptomics** — RNA-seq
- **Proteomics** — mass-spectrometry proteomics

**Post-study biomarker assays (blood-derived)**
- **NfL** — neurofilament light chain, serum
- **SomaScan** — SomaScan proteomics, plasma

**Cell lines**
- **iPSC lines** — available to order through Cedars-Sinai or CIRM
- **diMN lines** — iPSC-derived motor neuron lines used to generate the omics data

**Clinical and metadata**
- Clinical measures, demographics, subject group, and assay/QC metadata as
  described in the Clinical Metadata and Measures and Answer ALS Data Catalogue
  documents.

# Section 2: Data Types That Are NOT Available

The following data types are **not part of the Answer ALS dataset on Neuromine**.
If a user asks about one of these, say plainly that it is not available, rather
than hedging or implying it might exist.

- Imaging of any kind (MRI, PET, CT, histopathology / digital pathology)
- Metabolomics
- Immunomics / immune-repertoire data
- Spatial omics / spatial transcriptomics
- Single-cell or single-nucleus sequencing (the omics are bulk)
- microRNA / small-RNA sequencing
- Long-read sequencing
- CRISPR / gene-editing screen data
- Radiomics

Q: Does Answer ALS include microRNA (miRNA) or small-RNA sequencing?

Context: Users may use "RNA-seq" or "transcriptomics" to mean any RNA assay,
or may request mRNA and miRNA together. Lou must distinguish the available
bulk mRNA transcriptomics data from the unavailable small-RNA modality.

A: No. MicroRNA (miRNA) and small-RNA sequencing are not part of the Answer ALS
dataset on the Neuromine Data Portal. Bulk mRNA RNA-seq is available as
transcriptomics, but it does not include miRNA or small-RNA sequencing. If a
user's request assumes that miRNA is included, correct that assumption plainly;
do not imply that it can be downloaded or inferred from the mRNA data.

Q: How should Lou answer when a user asks about a data type not listed in Section 1?

Context: Users frequently ask whether the portal includes modalities that it does not. Earlier behavior was to hedge ("absence of documentation does not prove absence"), which left users unsure.

A: For the data types listed in Section 2, state directly that they are not part
of the Answer ALS dataset on the Neuromine Data Portal. For a data type that is
not listed in either section and that you cannot confirm from the knowledge base,
say you cannot confirm it is available and direct the user to data@answerals.org
rather than guessing.

# General Support Reference

For questions about data availability not covered here, contact the Neuromine
Data Portal support team at data@answerals.org.
