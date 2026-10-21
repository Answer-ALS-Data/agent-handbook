Document Title: Participant Counts Reference
Knowledge Base: KB 2: Data & Science Reference
Category: User-Facing Guide
Platform: Neuromine Data Portal (Answer ALS)
Support Contact: data@answerals.org
Last Updated: June 02, 2026
Version: 1.0 (release index r7.2.4)

# Purpose

This document provides authoritative, pre-computed participant counts for the
Answer ALS dataset: cohort composition, per-modality totals, modality
co-availability (intersections), and breakdowns by subject group and sex. These
are the figures Lou should report for "how many participants have X" questions.
Every figure here is final and privacy-checked; report them as published. For any
count that is NOT in this document (see Section 7), say it is not published and
direct the user to data@answerals.org rather than estimating.

# Section 1: Cohort Composition

Total participants: **1,273**

| Subject group | Participants |
|---|---|
| ALS | 852 |
| Healthy Control | 340 |
| Non-ALS MND | 69 |
| Asymptomatic ALS Gene Carrier | 12 |

By sex: Male 735, Female 536 (sex is blank for 2 participants).

Controls: of the 340 Healthy Controls, 232 are external controls (added from an external source, CDI) and 108 are internal controls.

# Section 2: Modality Availability (totals)

| Modality | Participants |
|---|---|
| Transcriptomics | 1,102 |
| Proteomics | 1,094 |
| diMN | 1,062 |
| Epigenomics | 1,039 |
| Genomics | 939 |
| NfL | 911 |
| iPSC | 726 |
| SomaScan | 357 |

These are totals across all subject groups. A blank availability flag in the source data means No.

# Section 3: Two-Modality Intersections (participants with BOTH)

Symmetric matrix; the diagonal equals each modality total. Read intersections from this table; the smaller total is not a subset of the larger.

| both / and | Geno | Epig | Trans | Prot | NfL | Soma | iPSC | diMN |
|---|---|---|---|---|---|---|---|---|
| **Genomics** | 939 | 768 | 815 | 810 | 853 | 339 | 674 | 830 |
| **Epigenomics** | 768 | 1039 | 1039 | 1030 | 761 | 293 | 668 | 986 |
| **Transcriptomics** | 815 | 1039 | 1102 | 1090 | 802 | 314 | 716 | 1047 |
| **Proteomics** | 810 | 1030 | 1090 | 1094 | 798 | 312 | 710 | 1039 |
| **NfL** | 853 | 761 | 802 | 798 | 911 | 355 | 665 | 813 |
| **SomaScan** | 339 | 293 | 314 | 312 | 355 | 357 | 257 | 320 |
| **iPSC** | 674 | 668 | 716 | 710 | 665 | 257 | 726 | 726 |
| **diMN** | 830 | 986 | 1047 | 1039 | 813 | 320 | 726 | 1062 |

# Section 4: Three-Modality Intersections (participants with ALL THREE)

Every three-way combination of modalities. All values are final.

| Modalities | Participants |
|---|---|
| Genomics + Epigenomics + Transcriptomics | 768 |
| Genomics + Epigenomics + Proteomics | 759 |
| Genomics + Epigenomics + NfL | 711 |
| Genomics + Epigenomics + SomaScan | 278 |
| Genomics + Epigenomics + iPSC | 619 |
| Genomics + Epigenomics + diMN | 768 |
| Genomics + Transcriptomics + Proteomics | 806 |
| Genomics + Transcriptomics + NfL | 750 |
| Genomics + Transcriptomics + SomaScan | 299 |
| Genomics + Transcriptomics + iPSC | 664 |
| Genomics + Transcriptomics + diMN | 815 |
| Genomics + Proteomics + NfL | 747 |
| Genomics + Proteomics + SomaScan | 297 |
| Genomics + Proteomics + iPSC | 659 |
| Genomics + Proteomics + diMN | 810 |
| Genomics + NfL + SomaScan | 337 |
| Genomics + NfL + iPSC | 624 |
| Genomics + NfL + diMN | 761 |
| Genomics + SomaScan + iPSC | 249 |
| Genomics + SomaScan + diMN | 305 |
| Genomics + iPSC + diMN | 674 |
| Epigenomics + Transcriptomics + Proteomics | 1030 |
| Epigenomics + Transcriptomics + NfL | 761 |
| Epigenomics + Transcriptomics + SomaScan | 293 |
| Epigenomics + Transcriptomics + iPSC | 668 |
| Epigenomics + Transcriptomics + diMN | 986 |
| Epigenomics + Proteomics + NfL | 754 |
| Epigenomics + Proteomics + SomaScan | 288 |
| Epigenomics + Proteomics + iPSC | 659 |
| Epigenomics + Proteomics + diMN | 977 |
| Epigenomics + NfL + SomaScan | 292 |
| Epigenomics + NfL + iPSC | 618 |
| Epigenomics + NfL + diMN | 761 |
| Epigenomics + SomaScan + iPSC | 232 |
| Epigenomics + SomaScan + diMN | 293 |
| Epigenomics + iPSC + diMN | 668 |
| Transcriptomics + Proteomics + NfL | 794 |
| Transcriptomics + Proteomics + SomaScan | 309 |
| Transcriptomics + Proteomics + iPSC | 706 |
| Transcriptomics + Proteomics + diMN | 1035 |
| Transcriptomics + NfL + SomaScan | 312 |
| Transcriptomics + NfL + iPSC | 657 |
| Transcriptomics + NfL + diMN | 802 |
| Transcriptomics + SomaScan + iPSC | 252 |
| Transcriptomics + SomaScan + diMN | 314 |
| Transcriptomics + iPSC + diMN | 716 |
| Proteomics + NfL + SomaScan | 310 |
| Proteomics + NfL + iPSC | 653 |
| Proteomics + NfL + diMN | 798 |
| Proteomics + SomaScan + iPSC | 250 |
| Proteomics + SomaScan + diMN | 312 |
| Proteomics + iPSC + diMN | 710 |
| NfL + SomaScan + iPSC | 255 |
| NfL + SomaScan + diMN | 318 |
| NfL + iPSC + diMN | 665 |
| SomaScan + iPSC + diMN | 257 |

# Section 5: Modality Availability by Subject Group

The two smallest groups (Non-ALS MND and Asymptomatic ALS Gene Carrier) are combined into "Other" so that no cell falls below the privacy threshold; per-modality counts for those two groups individually are not published.

| Group | Geno | Epig | Trans | Prot | NfL | Soma | iPSC | diMN | Group total |
|---|---|---|---|---|---|---|---|---|---|
| ALS | 774 | 678 | 718 | 716 | 741 | 245 | 614 | 731 | 852 |
| Healthy Control | 99 | 299 | 319 | 313 | 95 | 76 | 85 | 266 | 340 |
| Other (Non-ALS MND + Asymptomatic) | 66 | 62 | 65 | 65 | 75 | 36 | 27 | 65 | 81 |

# Section 6: Modality Availability by Sex

| Sex | Geno | Epig | Trans | Prot | NfL | Soma | iPSC | diMN | Total |
|---|---|---|---|---|---|---|---|---|---|
| Male | 557 | 585 | 630 | 625 | 550 | 200 | 431 | 616 | 735 |
| Female | 382 | 454 | 472 | 469 | 361 | 157 | 295 | 446 | 536 |

Sex is blank for 2 participants, who are not shown.

# Section 7: What Is Not Published Here

The following are intentionally not provided. For any of these, tell the user the figure is not published and direct them to data@answerals.org:

- "Has X but NOT Y" counts (set differences) and exact membership patterns, which can produce groups below the privacy threshold.
- Per-modality counts for the Non-ALS MND or Asymptomatic ALS Gene Carrier groups individually.
- Intersections of four or more modalities.
- Any breakdown crossing modality with a small subgroup.

Never derive, narrow, or reconstruct a withheld figure by subtracting published numbers.

# General Support Reference

For participant-count questions not covered here, contact the Neuromine Data Portal support team at data@answerals.org.
