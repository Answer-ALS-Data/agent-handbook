Document Title: WGS Variant Report Tool
Knowledge Base: KB 3: User Guides & Workflows
Category: User-Facing Guide
Platform: Neuromine Data Portal (Answer ALS)
Support Contact: data@answerals.org
Last Updated: June 26, 2026
Version: 1.0

---

## Purpose

This document is a training resource for an LLM-based conversational assistant deployed on the Neuromine Data Portal. It serves as a brief overview reference for the WGS SNV Report Generator — a web application that queries whole genome sequencing (WGS) variant data and produces Excel variant reports for ALS research.

This document covers: what the tool is, the two ways to use it (Sample / Gene Report and Variant Lookup), the gene lists and filters it supports, the data pipelines behind it, and who to contact.

This document does not cover: the in-app data visualizations (a work in progress), the data access request and DUA process (see Access and Approvals Handbook), or general portal navigation (see Portal Map and Naming Guide).

---

## Section 1: Tool Overview

*This section establishes what the tool is and what it produces. Users may refer to it as the "variant report tool," "SNV report generator," "WGS report," or simply "the variant tool." It is a Panel-based web application backed by Azure SQL Server.*

---

Q: What is the WGS Variant Report Tool?

Context: *This is the core orientation question. The tool generates Excel variant reports from whole genome sequencing data for ALS research within the Answer ALS / Neuromine platform.*

A: The WGS Variant Report Tool (the WGS SNV Report Generator) is a web application that queries whole genome sequencing (WGS) variant data in Azure SQL Server and produces **Excel variant reports** for ALS research on the Answer ALS / Neuromine platform.

It supports two modes of use:

- **Sample / Gene Report** — start from a set of participants and genes and explore the variants they carry.
- **Variant Lookup** — start from a single variant and find which participants carry it.

---

Q: What does a generated report contain?

Context: *Users want to know what they get out of the tool. The Sample / Gene Report exports a multi-sheet Excel workbook.*

A: A Sample / Gene Report exports an Excel file with multiple sheets, including a **Summary**, gene-specific sheets (such as **C9orf72** and **ATXN2**), pathogenicity sheets (**ClinVar**, **InterVar**, **In Silico**), and a **Data Dictionary**. Variant Lookup exports a focused Excel sheet of the matching participants and their genotypes.

---

## Section 2: Sample / Gene Report

*This section covers the primary mode: querying variants for a set of participants across a chosen gene list. This is the default workflow when users want "all the variants" for a group of samples.*

---

Q: How do I generate a Sample / Gene Report?

Context: *This is the main workflow. Users select genes and samples, optionally apply filters, then run the analysis and download the report.*

A: To generate a Sample / Gene Report:

1. Enter a **Report Title**.
2. Choose a **Gene List** or provide a custom list of genes.
3. Enter participant **Sample IDs** (or load them automatically via URL parameters).
4. Optionally filter by synonymous SNVs or by European ethnicity.
5. Click **Run Analysis** to explore the variants in the table view, then download the Excel report.

---

Q: What gene lists are available?

Context: *The tool ships with predefined gene lists and also accepts custom input. The predefined lists are loaded from Azure Blob Storage.*

A: The tool supports three predefined gene lists — **ALS Genes**, **ACMG Genes**, and **ALSoD** — loaded from storage, plus any **custom list** of genes you enter yourself.

---

Q: How are participant samples selected?

Context: *Samples can be entered manually or loaded automatically from the Data Portal when the tool is reached via a link with parameters.*

A: You can either enter participant IDs manually, or have them loaded automatically via URL parameters (`?dataset=&searchId=`), which fetch the matching participants from the Data Portal API.

---

Q: What variant filters does the tool support?

Context: *The tool queries exonic and upstream/downstream variant tables and can filter on several dimensions.*

A: The tool queries exonic and upstream/downstream variant tables and supports filtering by **synonymous variants**, **ethnicity**, and **pathogenicity** — the latter drawing on ClinVar, InterVar, and in silico predictions.

---

## Section 3: Variant Lookup

*This section covers the second mode, which runs the opposite direction from the report: starting from a single variant and finding its carriers. Users may describe this as "who has this variant" or "look up an rsID."*

---

Q: What is Variant Lookup and how is it different from a report?

Context: *Variant Lookup is a genotype-first search. Instead of starting from participants and genes, it starts from a single locus or rsID and returns the participants who carry it.*

A: Variant Lookup is a **genotype-first search** that runs the opposite direction from the report. Given a single locus (chromosome and position) or an rsID, it finds **which participants carry that variant and with what genotype**. Numeric genotypes (`0/0`, `0/1`, `1/1`) are translated to alleles (e.g. `C/C`, `C/G`, `G/G`) using the variant's REF/ALT, so you can filter by the allelic form a researcher actually asks for (for example, homozygous `G/G`).

You reach it via the **Sample / Gene Report** vs **Variant Lookup** toggle at the top of the form.

---

Q: How do I run a Variant Lookup?

Context: *Users need the step sequence. Either an rsID or a chromosome:position is enough to run the search.*

A: To run a Variant Lookup:

1. Switch the form's mode toggle to **Variant Lookup**.
2. Enter an **rsID** (e.g. `rs3173615`) or a **chromosome:position** (e.g. `chr7:12,229,791`) — either is enough.
3. Optionally set a **Genotype filter** (e.g. `G/G`; blank returns all genotypes), or tick **Carriers only** to drop hom-ref and no-call participants.
4. Optionally paste participant IDs under **Limit to participants** to restrict the search.
5. Click **Run Lookup** to see the matching participants, the genotype breakdown at that locus, and a **Download (.xlsx)** export.

---

## Section 4: Data Behind the Tool

*This section briefly explains where the tool's data comes from. The variant data is loaded into SQL by ETL pipelines before the app can query it. This is background context, not an end-user workflow.*

---

Q: Where does the tool's variant data come from?

Context: *The app queries Azure SQL Server, but the data must first be loaded by separate ETL pipelines. Users occasionally ask how the data gets there or how current it is.*

A: Before the app can query anything, variant data must be loaded into SQL by ETL pipelines:

- **Exonic variant pipeline** — processes exonic variant data.
- **Upstream/downstream pipeline** — processes upstream/downstream regulatory variant data.
- **Ensembl/gnomAD pipeline** — populates the gene-metadata reference tables (Ensembl genes and gnomAD constraint metrics) used for gene information.

Each pipeline runs in three stages: transform → load → index.

---

## General Support Reference

For questions about the WGS Variant Report Tool not covered here, contact the Neuromine Data Portal support team. The tool is maintained by the OnPoint Scientific team.

Support Email: data@answerals.org
