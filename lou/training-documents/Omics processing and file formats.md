Document Title: Omics Processing and File Formats
Knowledge Base: KB 3: User Guides & Workflows
Category: User-Facing Guide
Platform: Neuromine Data Portal (Answer ALS)
Support Contact: data@answerals.org
Last Updated: April 1, 2026
Version: 1.0

# Purpose

This document provides answers to frequently asked questions about how omics data is processed, structured, and formatted on the Neuromine Data Portal. It covers the data level system (levels 1–5) and what each level represents for each assay type, the file formats associated with each level, batch correction resources including the sample mapping file and known batch effect issues, SomaScan and NfL data specifics, differences between Answer ALS and ALS TDI sample sources, and platform and sample preparation details. This guide is intended for use as a training resource for an LLM-based conversational assistant and should be referenced when users ask questions about data levels, file formats, batch effects, proteomics processing, or omics platform details.

# Section 1: Data Levels

*Users frequently ask what the data levels mean, which level they should download, and why some levels are not available for certain assay types. The level system is consistent across assay types but the file formats and sizes vary. Proteomics is the notable exception — it has no Level 3.*

Q: What do the data levels mean?

Context: This is the foundational question for understanding the omics data structure. Users often download the wrong level for their use case because they do not understand the hierarchy.

A: The Neuromine Data Portal organizes omics data into a five-level hierarchy representing increasing degrees of processing:

- **Level 1** — Raw, immutable data coming directly off an instrument (e.g., a sequencer or mass spectrometer). This is the least processed form of the data.
- **Level 2** — Raw data mapped against an appropriate reference (e.g., the hg38 human genome reference for sequencing-based assays). Still individual-level data.
- **Level 3** — The most processed form of patient-specific, individual-level data. For sequencing assays this is variant calls or gene counts; for epigenomics it is peak calls.
- **Level 4** — Cohort-level data produced by joining Level 3 data across all participants into a single matrix. This is the most commonly used level for downstream analysis.
- **Level 5** — Comparative data between two specific cohorts. Typically differentially expressed genes (DESeq2), differentially accessible chromatin regions (DiffBind), or differentially expressed proteins.

**Important caveats — not all levels exist for all assays:**
- **Proteomics has no Level 3.** The proteomics pipeline goes directly from Level 2 (mzML) to Level 4 (protein/peptide intensity matrices) via openSWATH and mapDIA. Do not describe a Level 3 proteomics format or imply that L3 exists for proteomics.
- **Genomics Level 1 (FASTQ)** is only available by special request — it is not part of the standard download flow. Contact data@answerals.org to request it.
- **Level 5 is "coming soon"** in the portal. Pre-computed differential analyses are documented as the intended L5 product, but L5 datasets may not all be available for every assay at the time of any given visit. Always note this caveat when discussing what to download.

Always mention these caveats explicitly when a user asks "what are the levels?" or "which level should I download?" — never describe the hierarchy as if all five levels exist uniformly across every assay.

---

Q: What are the file formats and sizes for each assay type at each level?

Context: Users ask this when deciding what to download, planning storage, or writing analysis pipelines. The answer varies significantly by assay type.

A: The following table summarizes the file format and approximate size per individual (or per cohort for Level 4) for each assay type:

**Genomics (Whole Genome Sequencing)**
- Level 1: FASTQ — ~48 GB per individual (special request only)
- Level 2: BAM/CRAM — ~15 GB per individual
- Level 3: VCF — ~10 GB per individual
- Level 4: Annotated VCF — ~190 GB cohort file

**Epigenomics (ATAC-Seq)**
- Level 1: FASTQ — ~5 GB per individual
- Level 2: BAM — ~6.5 GB per individual
- Level 3: narrowPeak — ~26 MB per individual
- Level 4: CSV matrix of consensus peak counts — ~100 MB
- Level 5: Differentially accessible peaks (DiffBind)

**Transcriptomics (RNA-Seq)**
- Level 1: FASTQ — ~5 GB per individual
- Level 2: BAM/CRAM — ~5 GB per individual
- Level 3: TSV gene counts — ~35 MB per individual
- Level 4: CSV matrix of counts — ~45 MB
- Level 5: CSV of differentially expressed genes (DESeq2)

**Proteomics (SWATH-MS)**
- Level 1: WIFF — ~2.5 GB per individual
- Level 2: mzML — ~12 GB per individual
- Level 3: Does not exist — see note below
- Level 4: TXT protein and peptide intensity matrices — ~11 MB
- Level 5: Differentially expressed proteins

Note: Proteomics has no Level 3. The pipeline goes from Level 2 mzML directly to Level 4 protein/peptide intensity matrices via the openSWATH and mapDIA processing pipeline.

---

Q: How do I get Level 1 genomics data?

Context: Level 1 genomics (raw FASTQ) is not available for standard download. Users sometimes ask for it when they want to reprocess raw reads with their own pipeline.

A: Level 1 genomics data is only available upon special request. To request it, contact the Neuromine support team at data@answerals.org. All other omics Level 1 data is available through the standard download process.

---

Q: Which level should I download for my analysis?

Context: Users new to the portal often do not know which level fits their use case. The right answer depends on what they are trying to do.

A: The right level depends on your analysis:

- **Level 4** is the right starting point for most researchers. It contains the cohort-wide matrix of counts or intensities — one file with all participants — ready for statistical analysis.
- **Level 3** is appropriate if you want to work with individual participant files and run your own cohort aggregation, or if you need data for a specific subset of participants.
- **Level 2** is appropriate if you need aligned reads for custom variant calling, peak calling, or transcript quantification with your own tools.
- **Level 1** is appropriate only if you need to reprocess raw instrument data from scratch. Genomics Level 1 requires a special request.
- **Level 5** provides pre-computed differential analysis results (ALS vs. controls) if you want a starting point rather than running DE analysis yourself.

For most downstream analyses, Level 4 is the recommended starting point. For questions about which level fits a specific use case, contact data@answerals.org.

---

# Section 2: File Formats

*Users ask about specific file formats when they encounter unfamiliar types or are setting up analysis pipelines. This section describes each format in plain language and explains which assay and level it belongs to.*

Q: What is a FASTQ file?

Context: FASTQ is the raw output format from sequencing instruments. Users may encounter it at Level 1 for genomics, epigenomics, and transcriptomics.

A: A FASTQ file is a text-based format that stores raw sequence data and quality scores from a sequencing instrument. Each sequenced read is represented as four lines: a sequence identifier, the base calls (A, C, T, G, N), a separator (+), and Phred-encoded quality scores. FASTQ files are the raw, immutable output from the sequencer and are the starting point for all alignment-based pipelines. In the Neuromine data, FASTQ corresponds to Level 1 for genomics, epigenomics, and transcriptomics.

---

Q: What is a BAM or CRAM file?

Context: BAM and CRAM are the Level 2 aligned read formats. Users who want to run their own variant calling or quantification pipelines will work with these files.

A: BAM (Binary Alignment/Map) and CRAM are formats for storing sequencing reads aligned to a reference genome. BAM is a compressed binary version of the human-readable SAM format. CRAM is a more highly compressed alternative that achieves smaller file sizes while preserving all information. Both formats store one alignment per row, with fields for query name, flag, reference name, position, mapping quality, CIGAR string, and sequence data. In the Answer ALS data, BAM and CRAM correspond to Level 2 for genomics, epigenomics, and transcriptomics, and all Answer ALS alignments use hg38 as the reference genome. The ALS TDI reference genome is not documented here; if a user asks about ALS TDI, say so and refer them to data@answerals.org.

---

Q: What is a VCF file?

Context: VCF is the Level 3 format for genomics. Users doing variant analysis will work with these files.

A: A VCF (Variant Call Format) file is a text format for storing genetic variants identified in a sequenced sample. Each data line represents one variant position in the genome and includes the chromosome, position, reference base, alternate allele(s), quality score, filter status, and genotype information per sample. Level 3 VCFs on the portal contain individual-level variant calls. Level 4 contains an Annotated VCF — the same format with additional gene function and variant impact annotations added to the INFO column using the ANNOVAR tool. The annotated Level 4 cohort VCF is approximately 190 GB.

---

Q: What is a narrowPeak file?

Context: narrowPeak is the Level 3 format for epigenomics and is unfamiliar to users who have not worked with ATAC-Seq data before.

A: A narrowPeak file is a BED6+4 format used to report called peaks of signal enrichment from ATAC-Seq data. Each row represents one peak region and includes the chromosome, start and end positions, a name, a score, strand orientation, signal value, p-value, q-value, and the position of the peak summit. In the Neuromine data, narrowPeak files are the Level 3 output for epigenomics — one file per participant representing that individual's accessible chromatin regions. The Level 4 matrix is generated from these individual peak files using the DiffBind R package to create a consensus peakset across the cohort.

---

Q: What is a WIFF file?

Context: WIFF is the Level 1 raw format for proteomics. It is a proprietary Sciex format and unfamiliar to users outside of mass spectrometry.

A: A WIFF file is a proprietary format from Sciex mass spectrometers containing raw data-independent acquisition (DIA) mass spectrometry output. It is not human-readable and requires Sciex software or compatible tools to open. In the Neuromine proteomics pipeline, WIFF files are the Level 1 raw instrument output and are converted to the open-source mzML format to produce Level 2 data.

---

Q: What is an mzML file?

Context: mzML is the Level 2 format for proteomics — a standardized open format for mass spectrometry data.

A: An mzML file is the standard open-source XML-based format for mass spectrometry data. It is produced by converting raw vendor-specific files (WIFF) into a format that is compatible with open-source analysis tools. An mzML file contains the sample list, instrument configuration, data processing history, acquisition settings, spectra (MS1 and MS2), and chromatograms. In the Neuromine data, mzML corresponds to Level 2 proteomics. Each mzML file is approximately 12 GB per individual. The conversion from WIFF to mzML is performed using the Sciex converter tool.

---

Q: What do the Level 4 proteomics matrix files contain?

Context: The Level 4 proteomics files are tab-separated text files with a specific structure that users need to understand before loading them into analysis tools.

A: The Level 4 proteomics data consists of two tab-separated TXT files: a protein-level matrix and a peptide-level matrix.

The **protein-level matrix** contains:
1. Uniprot-derived ProteinID
2. Sample-wise intensities (one column per sample)
3. Number of fragments associated with the ProteinID
4. Number of peptides associated with the ProteinID

The **peptide-level matrix** contains:
1. Uniprot-derived ProteinID
2. Peptide sequence
3. Sample-wise intensities (one column per sample)
4. Number of fragments associated with the peptide sequence

These matrices are the output of the mapDIA software processing pipeline and represent normalized, quantified protein and peptide abundances across all participants. Each file is approximately 11 MB. For access questions, contact data@answerals.org.

---

# Section 3: Batch Effects and Correction

*Batch effects are a major concern in large-scale omics studies. The portal provides specific resources for handling batch effects correctly. This section covers the batch control design, the 52 proteomics samples with known issues, the sample mapping file, and the sex effect in transcriptomics PCA.*

Q: What batch controls are included in the Answer ALS data and why?

Context: Users running their own analyses need to understand how batch variation was controlled for during data generation. The portal uses two distinct types of batch controls.

A: The Answer ALS experimental design includes two types of batch controls using the CTRL-NEUEU392AE8 cell line:

1. **Batch Technical Control (BTC):** Produced in bulk in Oct–Dec 2018, this control is sent to each omics lab with every shipment of samples. Because all BTC pellets were produced simultaneously under a standard operating protocol, the same assay should return the same results for any BTC pellet. This controls for assay-specific variability between runs.

2. **Batch Differentiation Control (BDC):** The same cell line is also differentiated alongside every new batch of ALS/CTR lines. It is thawed, expanded, differentiated, and pelleted with each batch and sent to omics labs alongside the ALS and control samples. This controls for inter-batch variability in the differentiation process itself.

Both controls appear in the data as CTRL-NEUEU392AE8. The batch and shipment identifiers in the Sample Mapping File link each participant sample to its corresponding controls.

---

Q: What is the Sample Mapping File and how should I use it?

Context: The sample mapping file is a critical resource for batch correction but users often do not know it exists or how to apply it.

A: The Sample Mapping File is a CSV that links each participant sample to its batch number, shipment, site, and other processing metadata. It is essential for controlling batch effects in downstream analysis. The file contains columns including participant ID, sample ID, cell line, batch number, vial ID, site, and shipment.

To use it: include batch and shipment as covariates in your statistical model. For example, in a differential expression design formula, use `design ~ batch + condition` rather than `design ~ condition` alone. This removes known systematic variation introduced during sample processing before testing for disease-relevant signal.

The Sample Mapping File is available in the Level 3 folder for each omics type and also on the Resources tab of the portal. For questions about how to apply it to a specific analysis, contact data@answerals.org.

---

Q: Why do some samples appear multiple times in a Level 4 counts matrix, and does that mean repeat participant visits? (e.g. a sample that appears 147 times)

Context: Users inspecting a Level 4 matrix — most often the transcriptomics counts matrix — frequently notice that some sample IDs recur across many columns, sometimes a single ID appearing well over a hundred times. They tend to read these as repeat clinical visits from one participant, or as a special "reference sample." They are neither, and answering this correctly requires the batch-control design and the Sample Mapping File described above.

A: Duplicate or repeated sample IDs in a Level 4 counts matrix are **technical repeats and batch controls — not repeat participant visits.** The Answer ALS iPSC-derived omics (epigenomics, transcriptomics, proteomics) is generated from a single reprogramming per participant, so these counts matrices do not carry longitudinal, per-participant timepoints at all. When a participant's sample appears more than once, it means the same material was assayed more than once (a technical/replicate aliquot); when a control line appears many times, it is a batch control that was run alongside successive batches and shipments. (Repeat timepoints exist only in the separate post-study biomarker datasets — SomaScan and NfL — never in the iPSC-derived counts matrices.)

The clearest example is the **CTRL-NEUEU392AE8** cell line. As described above, it is a batch control (the BTC and BDC design), assayed alongside every batch and shipment — so it recurs once for each batch/shipment it accompanied. A sample ID that appears, for instance, 147 times in the transcriptomics data is this batch/design control appearing once per batch it was run with. It is **not** a reference sample in the sense of a gold-standard reference material, and it is **not** 147 biological repeat visits from one participant — its many copies are exactly the batch-effect controls that anchor the assay across runs.

**How to tell a technical repeat from a distinct sample using the sample ID.** Answer ALS sample IDs are composed as `<Participant_ID>-<VialID>-<assayLetter>` — for example `CTRL-NEUEU392AE8-<VialID>-T`. The trailing assay letter identifies the assay, not a timepoint: `-T` is transcriptomics (UCI), `-P` proteomics (Cedars-Sinai), `-E` epigenomics (Diagenode/MIT). Two rows that share the same `Participant_ID` but carry a **different VialID** are two distinct physical aliquots of that participant or control line — i.e., technical repeats, or for a control line separate batch-control pellets — rather than one biological sample and never a repeat clinical visit. To resolve which is which, look the sample ID up in the **Sample Mapping File**: its batch and shipment columns tell you that two rows sharing a participant ID are technical repeats/controls drawn from different runs, not repeat participant visits. If you need one value per participant for a downstream analysis, collapse technical repeats (and drop or model the batch controls) rather than treating each row as an independent biological observation.

---

Q: A sample (for example CTRL-NEUEU392AE8) appears many times — say 147 times — in the transcriptomics data. Is this a reference sample?

Context: This is the single most common misread of the counts matrix. Users see one sample ID recur far more often than any participant could and reach for "reference sample," "technical reference," or "repeat visits." The correct answer is that it is a batch control, verified against the Sample Mapping File — and it is worth answering the question in exactly these terms whenever a user points at a many-times-repeated ID.

A: No — a sample that appears many times, such as CTRL-NEUEU392AE8 appearing 147 times in the transcriptomics data, is **not a reference sample and not a repeat participant visit.** It is a **batch control**: the CTRL-NEUEU392AE8 cell line run as the BTC and BDC controls described above, assayed alongside every batch and shipment. The number of appearances tracks the number of batches and shipments it accompanied — roughly one appearance per batch — which is why it far exceeds the count of any real participant. To confirm what any repeated ID is, look it up in the **Sample Mapping File**: its batch and shipment columns show that the many copies are the same control cell line spread across processing runs, not a gold-standard reference material and not one participant sequenced 147 times. Treat these rows as batch controls — drop them or model them as controls — and never as biological replicates of a participant.

---

Q: I heard some proteomics samples have batch effects. Which ones and what should I do?

Context: 52 proteomics samples from Release One were identified as having strong batch effects. This is documented on the portal but users may not know about it or find the list easily.

A: Yes. 52 proteomics samples from Release One were found to have strong batch effects that differ substantially from all subsequent data. The Answer ALS team advises against using these 52 samples in any analysis.

These samples are **excluded from the Level 4 proteomics matrix** on the portal. However, their Level 1 and Level 2 data (WIFF and mzML) are still available for download if needed for specific purposes.

The full list of the 52 affected sample IDs is available at:
`(document on the portal)`

If you need access to the original Level 4 proteomics matrix that included these samples (from prior to release 6.1), contact terri@answerals.org.

Note: These samples correspond to dataset 1-1. Dataset 1-2, which is what the current Level 4 matrix is based on, excludes them.

---

Q: What is the sex effect in transcriptomics and how do I handle it?

Context: The sex effect is the dominant source of variation in PCA of transcriptomics data and users frequently encounter it without knowing what it is or how to correct for it.

A: The sex effect is the single largest contributor to gene expression variation observed in PCA analysis of the Answer ALS transcriptomics data. It is driven by both sex chromosome-linked genes (chrX and chrY) and autosomal genes that are differentially expressed between biological sexes. This effect has also been reported in post-mortem human brain tissue and iPSC-derived lines.

If you do not account for it, the sex effect will dominate your analysis and obscure disease-relevant signal.

To control for it, either:
1. Exclude chrX and chrY-linked genes from your analysis, and add a binary sex variable to your statistical design formula (e.g., `design ~ sex + condition`)
2. Or both of the above together

This is especially important for differential expression analysis comparing ALS cases to controls. The Answer ALS team recommends controlling for sex effect as a standard step in any downstream transcriptomics analysis.

---

Q: What are external controls in the dataset and how do I identify them?

Context: External controls were added to bolster the control cohort. Users may encounter them in the data and need to know what they are and how to handle them in analysis.

A: External controls are healthy control participants added to the Answer ALS dataset from an external source (CDI) to supplement the in-house control cohort. They were incorporated starting from batch 42. Because external controls come from a different source than the primary cohort, they can introduce confounding effects in transcriptomic and epigenomic analyses and may drive false-positive differentially expressed genes or differentially accessible regions.

To identify external controls, use the **External_Controls** column in the `aals_dataportal_datatable.csv` index file. This column flags which participants are external controls.

To handle them in analysis: include external control status as a covariate in your statistical design formula, or exclude them if your analysis requires a homogeneous control population. For guidance, contact data@answerals.org.

---

# Section 4: SomaScan and NfL

*SomaScan and NfL are post-study omics datasets that are separate from the primary iPSC-derived omics. Users frequently ask about them and what they measure. There is a known data quality issue with SomaScan NfL readings that users must be aware of.*

Q: What is SomaScan and is it available on the portal?

Context: Users ask about SomaScan when they are interested in plasma proteomics or biomarker discovery. It is a different type of proteomics than the SWATH-MS data.

A: SomaScan is an aptamer-based proteomics platform developed by SomaLogic that measures the relative abundance of 7,288 human proteins from a small plasma sample. It is a high-throughput approach well-suited for biomarker discovery across a large number of proteins simultaneously.

The Answer ALS SomaScan dataset contains 943 plasma samples from 358 participants — 282 ALS cases and 76 controls — across multiple timepoints. This data is available on the portal as a separate download package on the Datasets page. It is considered "external" or "post-study" data because it was collected outside the primary iPSC-derived omics framework.

For access or questions about the SomaScan dataset, contact data@answerals.org.

---

Q: What is the NfL dataset and is it available on the portal?

Context: NfL (neurofilament light chain) is a well-established biomarker for neuronal damage and users interested in ALS disease progression frequently ask about it.

A: The NfL dataset on the portal uses the Siemens Atellica immunoassay to measure neurofilament light chain concentration in serum samples. NfL is a protein released into the bloodstream when neurons are damaged and is a widely used biomarker for tracking ALS disease progression.

The Answer ALS NfL dataset contains measurements from 911 participants across multiple timepoints — 816 ALS cases and 95 controls. Like SomaScan, it is available as a separate post-study omics download package on the Datasets page.

---

Q: I noticed SomaScan includes an NfL measurement. Should I use that instead of the dedicated NfL dataset?

Context: This is a critical data quality issue. Users comparing NfL values across the portal may find conflicting results between the SomaScan NfL measurement and the Siemens Atellica NfL dataset. The bot has not had a reliable answer for this.

A: No. **Do not use the SomaScan NfL readings.** It has been found that NfL values from the SomaScan platform do not correlate with NfL values from the Siemens Atellica immunoassay on matched samples. The Answer ALS team is coordinating with SomaLogic to understand and resolve this discrepancy.

Until the discrepancy is resolved, exclude NfL from any SomaScan-based analyses. If you need NfL measurements, use the dedicated Siemens Atellica NfL dataset instead.

For the most current status on this issue, contact data@answerals.org.

Note: This known issue is documented in the Answer ALS SomaScan Data Readme, which is included in the SomaScan download package.

---

Q: Are there overlapping participants between the SomaScan dataset and the iPSC-derived omics datasets?

Context: Users planning multi-modal analyses want to know whether they can link SomaScan measurements to transcriptomics or epigenomics data for the same individuals.

A: Yes. There is overlap between participants in the SomaScan dataset and participants in the iPSC-derived omics datasets. You can link participants across datasets using the participant ID. For questions about the extent of overlap or how to structure a multi-modal analysis, contact data@answerals.org.

---

# Section 5: Sample Source and Preparation

*Users ask about where the data comes from and whether different assay types use different tissue sources. This is particularly important for understanding the biological interpretation of the data and for comparing Answer ALS to ALS TDI data.*

Q: What tissue or sample type is used for Answer ALS omics data?

Context: Users sometimes assume all omics data comes from the same sample type. The tissue source varies by assay.

A: Answer ALS uses two primary sample sources depending on the assay:

**iPSC-derived motor neurons** — used for epigenomics, transcriptomics, and proteomics (SWATH-MS). Blood is drawn from participants at clinical sites and sent to Cedars-Sinai Medical Center, where it is reprogrammed into induced pluripotent stem cells (iPSCs). The iPSCs are then differentiated into spinal motor neurons using the diMN (direct iPSC-derived motor neuron) protocol developed at Cedars-Sinai under Dr. Svendsen and Dr. Sareen. All iPSC and motor neuron generation happens in the same lab with consistent personnel to minimize variability. Motor neuron pellets are sent to the respective omics centers for processing.

**Blood/plasma/serum** — used for whole genome sequencing (WGS) and post-study biomarker datasets (SomaScan, NfL). Blood samples are sent to the New York Genome Center (NYGC) for genomics processing.

This means that when you see epigenomics, transcriptomics, or proteomics data, you are looking at motor neuron biology — not blood biology.

---

Q: What is the difference between Answer ALS and ALS TDI data on the portal?

Context: The portal hosts data from two cohorts — Answer ALS and ALS TDI (ARC Study). Users are often confused about how they differ and whether the data is comparable.

A: The Neuromine Data Portal hosts data from two cohorts:

**Answer ALS** is the primary cohort. Its omics data (epigenomics, transcriptomics, proteomics) is derived from iPSC-derived motor neurons generated at Cedars-Sinai. This makes it a standardized cellular model of ALS.

**ALS TDI (ARC Study)** is data from the ALS Therapy Development Institute's ARC Study — the longest-running natural history study of ALS. ALS TDI data on the portal includes whole genome sequencing (551 participants), transcriptomics (115 participants), and proteomics (115 participants). ALS TDI data is updated on a yearly basis. Only U.S.-based ARC participants who have contributed omics data are shared on Neuromine; the full ARC Study dataset is available through the ARC Data Commons separately.

Unlike Answer ALS, all ALS TDI omics data is derived directly from blood samples — not iPSC-derived motor neurons. This is an important distinction when interpreting and comparing results across the two cohorts. Answer ALS omics reflects motor neuron biology; ALS TDI omics reflects blood biology.

For the rest of the ARC Study data, visit the ARC Data Commons at als.net/arc/data-commons.

---

Q: Does Neuromine have proteomic data from brain tissue?

Context: Users may ask whether Neuromine has proteomics from post-mortem brain tissue, given that ALS research frequently uses brain and spinal cord tissue. This is a common misconception driven by the broader ALS research literature.

A: No. Neuromine does not have proteomic data from brain tissue. All proteomics data on the portal comes from two sources:

1. **iPSC-derived motor neurons (Answer ALS, SWATH-MS)** — blood is drawn from participants, reprogrammed into iPSCs at Cedars-Sinai, and differentiated into spinal motor neurons. The proteomics assay is performed on these motor neuron pellets.
2. **Blood samples (ALS TDI, ARC Study)** — proteomic data for the ALS TDI cohort is derived from blood, not tissue.

Neither dataset includes post-mortem brain or spinal cord tissue proteomics. References to "brain tissue" in publications listed on the portal refer to external studies cited in that literature, not to data hosted on Neuromine.

---

# Section 6: Platform and Pipeline Details

*Users with computational backgrounds ask about the specific tools and platforms used to generate and process the data. This is relevant when they want to understand processing decisions, reproduce results, or extend the pipeline.*

Q: What platforms and tools are used for each omics assay?

Context: Researchers designing their own analyses need to know the upstream processing context to make appropriate methodological choices.

A: For **Answer ALS**, the following platforms and tools are used for each assay type. ALS TDI pipeline details (including the reference genome) are not documented here; if a user asks about ALS TDI processing, say so and refer them to data@answerals.org.

**Genomics (WGS)**
- Sequencing: New York Genome Center (NYGC)
- Reference: hg38
- Variant annotation (Level 4): ANNOVAR

**Epigenomics (ATAC-Seq)**
- Assay provider: Diagenode and MIT (under Dr. Fraenkel)
- Peak calling: DiffBind R package (minOverlap parameter set to 0.1 for consensus peakset)
- Differential accessibility: DiffBind

**Transcriptomics (RNA-Seq)**
- Sequencing and processing: University of California, Irvine (under Dr. Thompson)
- Reference: hg38
- Gene-level counting: featureCounts (Subread package)
- Differential expression: DESeq2 (Bioconductor)

**Proteomics (SWATH-MS)**
- Mass spectrometry: Sciex instrument, data-independent acquisition (DIA)
- Run at Cedars-Sinai under Dr. Van Eyk
- Level 1 → Level 2: Sciex converter (WIFF → profile mzML)
- Peptide extraction: openSWATH workflow against a custom-generated peptide library
- Scoring: mProphet algorithm (1% FDR cut-offs)
- Alignment: featurealignment script
- Normalization: Total Ion Current (TIC) normalization to remove systematic MS run bias
- Level 4 output: mapDIA software (transition-level → peptide and protein intensity matrices)

**Post-Study Biomarkers**
- SomaScan: SomaLogic 7k SomaScan Assay v4.1 (aptamer-based, plasma)
- NfL: Siemens Atellica immunoassay (serum)

---

# General Support Reference

For questions about data levels, file formats, batch correction, SomaScan, NfL, or platform details not covered in this document, contact the Neuromine Data Portal support team.

Support Email: data@answerals.org
