---
title: "OMIC Data Dictionary"
url: (document on the portal)
slug: doc-answer-als-data-level-descriptions_wsize_complete-091522
scraped_at: 2026-04-15T18:28:16Z
content_hash: bc27401ee9b3500a
source: dataportal.answerals.org
---

# OMIC Data Dictionary

## Summary

|  |  | level1 | level2 | level3 | level4 | level5 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Genomics |  | FASTQ | CRAM | VCF | Joint VCF |  |  |
| Epigenomics |  | FASTQ | BAM | Peaks | Matrix of Consensus Peak Counts | Diff Peaks (DiffBind) |  |
| Transcriptomics |  | FASTQ | BAM | Counts | Matrix of Counts | Diff Genes: (DESeq) |  |
| Proteomics |  | WIFF | mzML |  | Matrix of Intensities | Diff Proteins |  |
|  |  |  |  |  |  |  |  |
| Description |  | Level 1 data is raw, immutable data coming off an instrument (e.g. a sequencer). For genomics, we only provide data corresponding to this level upon special request. | Level 2 data is raw data mapped against the appropriate reference. Genomics (wgs) uses hg38 as a reference. | Level 3 data the most processed form of patient-specific data. | Level 4 data is attained from the joining of a cohort of patients’ level 3 data from a particular assay. | Level 5 data is comparative data between two specific cohorts typically labelled as differentially expressed genes (DESeq) or proteins or enriched sites within the genome (DiffBind) |  |

## Epigenomic Data Dictionary

| Data Level | Description | File Format | Format Description | Entry # | Field Content Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | raw, immutable data coming off an instrument (e.g. a sequencer). | FASTQ | FASTQ is a text-based sequencing data file format that stores both raw sequence data and quality scores. |  |  |  |
|  |  | ~5GB/individual |  | 1 | sequence identifier with information about the sequencing run and the cluster | information about the sequencing run and the cluster. The exact contents of this line vary by based on the BCL to FASTQ conversion software used. |
|  |  |  |  | 2 | Sequence | The sequence (the base calls; A, C, T, G and N). |
|  |  |  |  | 3 | Separator | A separator, which is simply a plus (+) sign. |
|  |  |  |  | 4 | Quality Score | The base call quality scores. These are Phred +33 encoded, using ASCII characters to represent the numerical quality scores. |
| 2 | raw data mapped against the appropriate reference. Genomics (wgs) uses hg38 as a reference. | BAM | The Sequence Alignment/Map (SAM) format is a generic alignment format for storing reads aligned to a reference genome, supporting short and long reads (up to 128 Mb) produced by different sequencing platforms. SAM is a text format file that is human-readable. The Binary Alignment/Map (BAM) keeps the same information as SAM, but in a compressed, binary format that is only machine readable.  Detailed information can be found at https://samtools.github.io/hts-specs/SAMv1.pdf. Information copied from https://support.illumina.com/help/BS_App_RNASeq_Alignment_OLH_1000000006112/Content/Source/Informatics/BAM-Format.htm |  |  |  |
|  |  | ~6.5GB/individual |  | RG | Read Group | Read group, which indicates the number of reads for a specific sample. |
|  |  |  |  | BC | Barcode Tag | Barcode tag, which indicates the demultiplexed sample ID associated with the read. |
|  |  |  |  | SM | Single-end alignment quality | Single-end alignment quality. |
|  |  |  |  | AS | Paired-end alignment quality | Paired-end alignment quality. |
|  |  |  |  | NM | Edit distance tag | Edit distance tag, which records the Levenshtein distance between the read and the reference. |
|  |  |  |  | XN | Amplicon name tag | Amplicon name tag, which records the amplicon tile ID associated with the read. |
|  |  |  |  |  |  |  |
| 3 | Level 3 data the most processed form of patient-specific data. | narrowPeak | This format is used to provide called peaks of signal enrichment based on pooled, normalized (interpreted) data. It is a BED6+4 format.  Information copied from: http://genome.ucsc.edu/FAQ/FAQformat.html#format12 | 1 | chrom | Name of the chromosome (or contig, scaffold, etc.). |
|  |  | ~26MB/individual |  | 2 | chromStart | The starting position of the feature in the chromosome or scaffold. The first base in a chromosome is numbered 0. |
|  |  |  |  | 3 | chromEnd | The ending position of the feature in the chromosome or scaffold. The chromEnd base is not included in the display of the feature. For example, the first 100 bases of a chromosome are defined as chromStart=0, chromEnd=100, and span the bases numbered 0-99. |
|  |  |  |  | 4 | name | Name given to a region (preferably unique). Use "." if no name is assigned. |
|  |  |  |  | 5 | score | Indicates how dark the peak will be displayed in the browser (0-1000). If all scores were "'0"' when the data were submitted to the DCC, the DCC assigned scores 1-1000 based on signal value. Ideally the average signalValue per base spread is between 100-1000. |
|  |  |  |  | 6 | strand | +/- to denote strand or orientation (whenever applicable). Use "." if no orientation is assigned. |
|  |  |  |  | 7 | signalValue | Measurement of overall (usually, average) enrichment for the region. |
|  |  |  |  | 8 | pValue | Measurement of statistical significance (-log10). Use -1 if no pValue is assigned. |
|  |  |  |  | 9 | qValue | Measurement of statistical significance using false discovery rate (-log10). Use -1 if no qValue is assigned. |
|  |  |  |  | 10 | peak | Point-source called for this peak; 0-based offset from chromStart. Use -1 if no point-source called. |
|  |  |  |  |  |  |  |
| 4 | Level 4 data is attained from the joining of a cohort of patients’ level 3 data from a particular assay. | csv | Matrix of consensus peak counts as comma separated values | rows | chromatin regions | chromatin regions are identified by generating a consensus peakset across all samples using the dba.counts function from the R package DiffBind with the minOverlap parameter set to 0.1. |
|  |  | 100MB matrixed file |  | columns | sample IDs |  |

## Proteomic Data Dictionary

| Data Level | Description | File Format | Format Description | Entry # | Field Content Description |
| --- | --- | --- | --- | --- | --- |
| 1 | raw data coming off a mass spectrometer | wiff |  |  |  |
|  |  | ~2.5GB/individual |  |  |  |
| 2 | mzML files that have been converted from vendor raw files into standard open-source format | mzML | MS .wiff files from the data-independent acquisition were first converted to profile mzML using Sciex converter. |  |  |
|  |  | 12GB/individual |  | 1 | sample list |
|  |  |  |  | 2 | instrument configuration list |
|  |  |  |  | 3 | data processing list |
|  |  |  |  | 4 | acquisition settings list |
|  |  |  |  | 5 | sprectrum list |
|  |  |  |  | 6 | chromatogram list |
| 3 | raw data mapped against the appropriate reference. Normalized and unnormalized transition level intensities in tab separated format | txt | Raw intensity data for peptide fragments was extracted from DIA files using the open source openSWATH workflow against the custom generated library. Target and decoy peptides were then extracted, scored, and analyzed using the mProphet algorithm to determine scoring cut-offs consistent with 1% FDR. Peak group extraction data from each DIA file was combined using the “featurealignment” script, which performs data alignment and modeling analysis across an experimental data set. The fragment-level intensities were normalized based on TIC (Total Ion Current) from each DIA MS run to remove systematic bias between MS runs. |  |  |
|  |  |  |  | 1 | Uniprot derived ProteinID |
|  |  |  |  | 2 | Peptide Sequence |
|  |  |  |  | 3 | Transition/Fragment |
|  |  |  |  | 4 | Sample wise intensities |
|  |  |  |  | 5 | Average Retention Time |
| 4 | Protein and peptide intensities in tab separated format along with summary of number of proteins and peptides quantified per sample | txt | Normalized transition-level data was then processed using the mapDIA software to produce quantitative peptide and protein level summary outputs were then used for all downstream biological analysis. |  |  |
|  |  | 11MB matrixed files | Protein Level | 1 | Uniprot derived ProteinID |
|  |  |  |  | 2 | Sample wise intensities |
|  |  |  |  | 3 | number of fragments associated with the proteinID |
|  |  |  |  | 4 | number of peptides associated with the proteinID |
|  |  |  | Peptide Level | 1 | Uniprot derived ProteinID |
|  |  |  |  | 2 | Peptide Sequence |
|  |  |  |  | 3 | Sample wise intensities |
|  |  |  |  | 4 | number of fragments associated with the peptide sequence |

## Transcriptomic Data Dictionary

| Data Level | Description | File Format | Format Description | Entry # | Field Content Description |  |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | raw data coming off an instrument (e.g. a sequencer). | FASTQ(Text) | FASTQ is a text-based sequencing data file format that stores both raw sequence data and quality scores. |  |  |  |
|  |  | ~5GB/individual |  | 1 | sequence identifier with information about the sequencing run and the cluster | information about the sequencing run and the cluster. The exact contents of this line vary by based on the BCL to FASTQ conversion software used. |
|  |  |  |  | 2 | Sequence | The sequence (the base calls; A, C, T, G and N). |
|  |  |  |  | 3 | Separator | A separator, which is simply a plus (+) sign. |
|  |  |  |  | 4 | Quality Score | The base call quality scores. These are Phred +33 encoded, using ASCII characters to represent the numerical quality scores. |
| 2 | cleaned data mapped against the appropriate reference. Genomics (wgs) uses hg38 as a reference. | BAM/CRAM(Binary) | The Sequence Alignment/Map (SAM) format is a generic alignment format for storing reads aligned to a reference genome, supporting short and long reads (up to 128 Mb) produced by different sequencing platforms. SAM is a text format file that is human-readable. The Binary Alignment/Map (BAM) keeps the same information as SAM, but in a compressed, binary format that is only machine readable. |  |  |  |
|  |  | ~5GB/individual |  | 1 | Each row is one alignment |  |
|  |  |  |  | 2 | Column headers are query name, FLAG, reference name, position, mapping quality, CIGAR string, ref name of mate, position of mate, template length, segment sequence ,quality score |  |
|  |  |  |  |  | Details are at https://samtools.github.io/hts-specs/SAMv1.pdf |  |
|  |  |  |  |  |  |  |
| 3 | Level 3 data the most processed form of patient-specific data. | tsv (Text) | number of reads mapped to each gene  counted resulting in a  table of counts, which is then  statistically  analyzed  to determine differentially expressed genes and pathways. |  |  |  |
|  |  | ~35MB/individual |  | 1 | Row headers are gene symbols |  |
|  |  |  |  | 2 | Column headers are chromosome number,  gene start, gene end, gene strand, gene length |  |
|  |  |  |  |  | Details are at http://subread.sourceforge.net/featureCounts.html |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
| 4 | A matrix of participant counts data | csv(Text) | Text file of merged level 3 data from multiple patients |  |  |  |
|  |  | ~45MB single file |  | 1 | Row headers are gene symbols | gene symbols are standard gene identifiers |
|  |  |  |  | 2 | Column headers are participant IDs | Each column is a participant ID |
|  |  |  |  | 3 | Each entry is the count for the correpsonding gene in the corresponding patient |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
| 5 | A table of differentially expressed genes | csv(Text) | Text file of identified differentially expressed genes |  |  |  |
|  |  |  |  | 1 | Row names are gene symbols |  |
|  |  |  |  | 2 | Column names are base mean, log fold change, log fold change standard error, test statistic, p value and adjusted p value |  |
|  |  |  |  |  | Details are at https://bioconductor.org/packages/devel/bioc/vignettes/DESeq2/inst/doc/DESeq2.html |  |

## WGS Data Dictionary

- **Data Level**: 1
- **Description**: raw, immutable data coming off an instrument (e.g. a sequencer).
- **File Format**: FASTQ
- **Format Description**: FASTQ is a text-based sequencing data file format that stores both raw sequence data and quality scores.
- **Estimated Size**: 24 files ~ 48 GB
- ****: CRAM = ~15 GB
- ****: VCF = 4GB

- **File Format**: ~54.5 GB/individual
- **Entry #**: 1
- **Field Content Description**: sequence identifier with information about the sequencing run and the cluster
- ****: information about the sequencing run and the cluster. The exact contents of this line vary by based on the BCL to FASTQ conversion software used.

- **Entry #**: 2
- **Field Content Description**: Sequence
- ****: The sequence (the base calls; A, C, T, G and N).

- **Entry #**: 3
- **Field Content Description**: Separator
- ****: A separator, which is simply a plus (+) sign.

- **Entry #**: 4
- **Field Content Description**: Quality Score
- ****: The base call quality scores. These are Phred +33 encoded, using ASCII characters to represent the numerical quality scores.

- **Data Level**: 2
- **Description**: raw data mapped against the appropriate reference. Genomics (wgs) uses hg38 as a reference.
- **File Format**: BAM/CRAM
- **Format Description**: The Sequence Alignment/Map (SAM) format is a generic alignment format for storing reads aligned to a reference genome, supporting short and long reads (up to 128 Mb) produced by different sequencing platforms. SAM is a text format file that is human-readable. The Binary Alignment/Map (BAM) keeps the same information as SAM, but in a compressed, binary format that is only machine readable. More details: https://samtools.github.io/hts-specs/SAMv1.pdf

- **File Format**: ~15GB/individual
- **Entry #**: 1
- **Field Content Description**: QNAME
- ****: String  Query template NAME

- **Entry #**: 2
- **Field Content Description**: FLAG
- ****: Int bitwise FLAG

- **Entry #**: 3
- **Field Content Description**: RNAME
- ****: String Reference sequence NAME

- **Entry #**: 4
- **Field Content Description**: POS
- ****: Int 1-based leftmost mapping POSition

- **Entry #**: 5
- **Field Content Description**: MAPQ
- ****: Int MAPping Quality

- **Entry #**: 6
- **Field Content Description**: CIGAR
- ****: String  CIGAR string

- **Entry #**: 7
- **Field Content Description**: RNEXT
- ****: String Reference name of the mate/next read

- **Entry #**: 8
- **Field Content Description**: PNEXT
- ****: Int Position of the mate/next read

- **Entry #**: 9
- **Field Content Description**: TLEN
- ****: Int observed Template LENgth

- **Entry #**: 10
- **Field Content Description**: SEQ
- ****: String  segment SEQuence

- **Entry #**: 11
- **Field Content Description**: QUAL
- ****: String  ASCII of Phred-scaled base QUALity

- **Data Level**: 3
- **Description**: Level 3 data the most processed form of patient-specific data.
- **File Format**: VCF
- **Format Description**: VCF is a text file format (most likely stored in a compressed manner). It contains meta-information lines, a header line, and then data lines each containing information about a position in the genome. The format also has the ability to contain genotype information on samples for each position. More details: https://samtools.github.io/hts-specs/VCFv4.2.pdf

- **File Format**: ~10GB/individual
- **Entry #**: 1
- **Field Content Description**: #CHROM
- ****: chromosome: An identifier from the reference genome or an angle-bracketed ID String (“<ID>”) pointing to a contig in the assembly file (cf. the ##assembly line in the header). All entries for a specific
CHROM should form a contiguous block within the VCF file. (String, no whitespace permitted, Required).

- **Entry #**: 2
- **Field Content Description**: POS
- ****: position: The reference position, with the 1st base having position 1. Positions are sorted numerically, in increasing order, within each reference sequence CHROM. It is permitted to have multiple records with the same POS. Telomeres are indicated by using positions 0 or N+1, where N is the length of the corresponding chromosome or contig. (Integer, Required)

- **Entry #**: 3
- **Field Content Description**: ID
- ****: identifier: Semicolon-separated list of unique identifiers where available. If this is a dbSNP variant it is encouraged to use the rs number(s). No identifier should be present in more than one data record. If there is no identifier available, then the missing value should be used. (String, no whitespace or semicolons permitted)

- **Entry #**: 4
- **Field Content Description**: REF
- ****: reference base(s): Each base must be one of A,C,G,T,N (case insensitive). Multiple bases are permitted. The value in the POS field refers to the position of the first base in the String. For simple insertions and deletions in which either the REF or one of the ALT alleles would otherwise be null/empty, the REF and ALT Strings must include the base before the event (which must be reflected in the POS field), unless the event occurs at position 1 on the contig in which case it must include the base after the event; this padding base is not required (although it is permitted) for e.g. complex substitutions or other events where all alleles have at least one base represented in their Strings. If any of the ALT alleles is a symbolic allele (an angle-bracketed ID String “”) then the padding base is required and POS denotes the coordinate of the base preceding the polymorphism. Tools processing VCF files are not required to preserve case in the allele Strings. (String, Required).

- **Entry #**: 5
- **Field Content Description**: ALT
- ****: alternate base(s): Comma separated list of alternate non-reference alleles. These alleles do not have to be called in any of the samples. Options are base Strings made up of the bases A,C,G,T,N,*, (case insensitive) or an angle-bracketed ID String (“”) or a breakend replacement string as described in the section on breakends. The ‘*’ allele is reserved to indicate that the allele is missing due to a upstream deletion. If there are no alternative alleles, then the missing value should be used. Tools processing VCF files are not required to preserve case in the allele String, except for IDs, which are case sensitive. (String; no whitespace, commas, or angle-brackets are permitted in the ID String itself)

- **Entry #**: 6
- **Field Content Description**: QUAL
- ****: QUAL - quality: Phred-scaled quality score for the assertion made in ALT. i.e. −10log10 prob(call in ALT is wrong). If ALT is ‘.’ (no variant) then this is −10log10 prob(variant), and if ALT is not ‘.’ this is −10log10 prob(no variant). If unknown, the missing value should be specified. (Numeric)

- **Entry #**: 7
- **Field Content Description**: FILTER
- ****: filter status: PASS if this position has passed all filters, i.e., a call is made at this position. Otherwise, if the site has not passed all filters, a semicolon-separated list of codes for filters that fail. e.g. “q10;s50” might indicate that at this site the quality is below 10 and the number of samples with data is below 50% of the total number of samples. ‘0’ is reserved and should not be used as a filter String. If filters have not been applied, then this field should be set to the missing value. (String, no whitespace or semicolons permitted)

- **Entry #**: 8
- **Field Content Description**: INFO
- ****: additional information: (String, no whitespace, semicolons, or equals-signs permitted; commas are permitted only as delimiters for lists of values) INFO fields are encoded as a semicolon-separated series of short keys with optional values in the format: =[,data]. If no keys are present, the missing value must be used.

- **Entry #**: 9, 10, 11, ...
- **Field Content Description**: Genotype fields
- ****: If genotype information is present, then the same types of data must be present for all samples. First a FORMAT field is given specifying the data types and order (colon-separated alphanumeric String). This is followed by one field per sample, with the colon-separated data in this field corresponding to the types specified in the format. The first sub-field must always be the genotype (GT) if it is present. There are no required sub-fields. More details: https://samtools.github.io/hts-specs/VCFv4.2.pdf (pages 5-6)

- **Data Level**: 4
- **File Format**: Annotated VCF
- **Format Description**: The annotated VCF is also a regular VCF file (level 3), so it has the exact same fields. In column INFO, more information about the variant and gene functions will be added. For more details, go to https://annovar.openbioinformatics.org/en/latest/user-guide/gene/

- **File Format**: 190GB marixed file

