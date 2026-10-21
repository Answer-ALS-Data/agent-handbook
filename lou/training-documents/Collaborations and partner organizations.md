Document Title: Collaborations and Partner Organizations
Knowledge Base: KB 1: Portal & Program Information
Category: Organizational Reference
Platform: Neuromine Data Portal (Answer ALS)
Support Contact: data@answerals.org
Last Updated: July 10, 2026
Version: 1.1

# Purpose

This document details the organizations and groups that make the Neuromine Data
Portal run — those that collaborate with, contribute data to, operate, fund, or
otherwise relate to Neuromine — and the specific relationship each holds. Its goal is
to give a single authoritative account of who is involved and how, so that the groups
and people behind Neuromine are correctly represented.

This is a supporting-context document. It exists so Lou can correctly attribute and
frame who is behind Neuromine when a user asks — not to be surfaced as primary answer
material. Use it for background and accurate credit; do not volunteer the full
organizational roster unless the user asks who is involved. For what the data is, how
to access it, or how to use the portal, the topic-specific documents remain
authoritative.

# Section 0: Framing note (read first)

Neuromine is the Answer ALS data portal expanded to host other groups. The portal was
originally built for Answer ALS data and later rebranded to Neuromine so it could hold
multiple datasets; the "Answer ALS Data Portal" and the "Neuromine Data Portal" are
the same website. Neuromine is supported and maintained by the Answer ALS Foundation.

The organizations below fall into three tiers:
- **Platform / operations** — the groups that run, build, and fund the portal itself.
- **Answer ALS lineage** — the study, its origin and funders, its coordinators, and the
  labs and centers that generated the original Answer ALS data now hosted on Neuromine.
- **Additional contributing initiatives and consortia** — other programs whose data or
  platforms connect to Neuromine, plus related challenges and downstream use.

Many groups in the lineage tier (philanthropic funders, clinical enrollment sites)
fund or support the Answer ALS *study*, not the portal directly. They are included for
context because the Answer ALS study produced the founding Neuromine dataset.

# Section 1: Platform, operations, and funding

## Answer ALS / Answer ALS Foundation
The Answer ALS Foundation supports and maintains Neuromine. Answer ALS is also the
founding and primary dataset on the platform and the data provider for that dataset.
Portal support is handled at data@answerals.org.

## OnPoint Scientific
OnPoint Scientific oversees the Neuromine Data Portal. They staff Neuromine and serve
as its data stewards, responsible for the quality, governance, and stewardship of the
data on the platform. OnPoint provides the program- and portal-facing team — program
direction, office hours, and the mentorship program — and maintains the WGS Variant
Report Tool.

OnPoint's services span the full data lifecycle:
- **Data Management** — structuring, versioning, and governing multimodal data
  (genomic, transcriptomic, metadata) for consistency, traceability, and compliance;
  version control for data integrity; governance of data quality, security, and access.
- **Data Standardization** — curation, cleaning, and integration of diverse datasets
  into standardized, interoperable formats, including implementation of the OMOP
  (Observational Medical Outcomes Partnership) Common Data Model and integration with
  large-scale databases.
- **Project Support** — data and scientific project managers, scientists, data
  scientists, developers, and bioinformaticians available on a project or on-demand
  basis.
- **Cloud & Platform Support** — cloud environment configuration and setup,
  infrastructure management, and support for data repositories, including migration
  and multi-cloud and data-platform integration.
- **Additional capabilities** — Data Lifecycle Management; ETL; Data Pipelines; Data
  Processing; Data Integration; OMOP Standardization; Project Management Support;
  Bioinformatics Support; Visualization Tool Development.

## Microsoft
Microsoft is a funder of Neuromine: through its non-profit arm it provides the Azure
resources that underpin the platform's infrastructure. Microsoft technology also runs
throughout Neuromine's operations — authentication is handled through Microsoft Azure
AD B2C (and a Microsoft account is a supported sign-in method), WGS data is stored in
Azure SQL Server, and office hours are held over Microsoft Teams.

## EPAM Systems
EPAM Systems provided substantial portal infrastructure and technical support for
Neuromine, delivering the engineering work behind the platform.

## IBM Research and Accenture
IBM Research and Accenture are technology partners of Answer ALS that contributed to
the data and computational effort behind the program. They are named among Answer ALS's
participating technology partners alongside Microsoft and EPAM.

# Section 2: Answer ALS lineage — origin, funders, coordination, and data generation

These groups founded, funded, coordinated, or produced the original Answer ALS dataset
now hosted on Neuromine.

## Origin and founding
Answer ALS grew out of a 2013 idea championed by former NFL player Steve Gleason, who
lives with ALS, and his advocacy group **Team Gleason**. The **Robert Packard Center
for ALS Research at Johns Hopkins** assembled the research consortium and is the
academic home of the initiative. Answer ALS was publicly launched in September 2015 by
three founding institutions: the Packard Center at Johns Hopkins, the **Cedars-Sinai
Regenerative Medicine Institute**, and the **Massachusetts General Hospital
Neurological Clinical Research Institute**.

## Study coordination and clinical sites
Johns Hopkins University School of Medicine (through the Packard Center) coordinated
the Answer ALS study together with Massachusetts General Hospital. Answer ALS is a
prospective, multi-center, longitudinal observational study; clinical data was
collected at a set of NEALS clinical sites, which include Johns Hopkins, Cedars-Sinai,
Massachusetts General Hospital, the University of California, Irvine, Emory University,
Northwestern University, Ohio State University, Washington University in St. Louis, and
Texas Neurology.

## Founding and philanthropic supporters
The Answer ALS study and Foundation are backed by a coalition of philanthropic,
corporate, and advocacy funders. These fund the study/Foundation rather than the portal
directly, but they made the founding dataset possible. Do not present them as portal
operators.
- **Initial stakeholder funders** — ALS Finding a Cure (a project of the Leandro P.
  Rizzuto Foundation, which led the founding ~$20M raise), the National Football League,
  the PGA TOUR, Travelers, the Fishman Family, and the Bari Lipp Foundation.
- **Corporate and advocacy supporters** — American Airlines, Caterpillar, Gates
  Ventures, The ALS Association, the Muscular Dystrophy Association (MDA), the Les Turner
  ALS Foundation, the Bruce Edwards Foundation, the Hartford Foundation, Aviators
  Against ALS, and Stay Strong Against ALS.
- **Pharmaceutical partner** — AbbVie.

## NeuroBANK (at Massachusetts General Hospital)
NeuroBANK is the secure electronic data capture system used by Answer ALS. It
de-identified the Answer ALS data at MGH before that data was provided to the portal,
and it calculated several of the pre-computed clinical fields present in the portal
(for example, the ALSFRS-R and cognitive progression slopes).

## Cedars-Sinai Medical Center
Cedars-Sinai Medical Center processes Answer ALS samples, generates the iPSC lines and
diMN motor neurons, and runs the proteomics (SWATH-MS). It also distributes the Answer
ALS iPSC lines through the Cedars-Sinai Biomanufacturing Center (with CIRM supplying
many control lines). Pricing and fulfillment for biosamples and iPSC lines are managed
by Cedars-Sinai directly rather than by Neuromine; the portal links out for ordering.
The lines are not distributed through Coriell.

## UCI Thompson Lab (University of California, Irvine)
The UCI Thompson Lab generates and processes the transcriptomics (RNA-Seq) data for
Answer ALS.

## MIT Fraenkel Lab
The MIT Fraenkel Lab generates the epigenomics (ATAC-Seq) data for Answer ALS, with
Diagenode as co-provider of the assay.

## New York Genome Center (NYGC) & Gladstone Institutes
Whole-genome sequencing for every Answer ALS participant is performed by the New York
Genome Center's Center for Genomics of Neurodegenerative Disease (NYGC-CGND). The
genomics data is generated through the Gladstone Institutes.

## Genomic data-sharing consortia (Project MinE and the NYGC ALS Consortium)
Answer ALS shares its whole-genome sequencing data with Project MinE and the New York
Genome Center's ALS Consortium (a partnership announced in 2017). This is a data-sharing
relationship for genomics, distinct from the Neuromine portal itself.

# Section 3: Additional contributing initiatives and consortia

## ALS TDI (ALS Therapy Development Institute)
ALS TDI partnered with Neuromine to share extensive longitudinal data from its ALS
Research Collaborative (ARC) Study, a significant portion of which is now integrated
into the Neuromine platform. ALS TDI de-identified its own dataset before providing it;
it is a data contributor, not an operator. The complete, continuously updated dataset
lives at the separate ARC Data Commons (als.net/arc/data-commons/).

## AD Data Initiative (ADDI) / AD Workbench
ADDI built and operates the AD Workbench, a separate, optional cloud analysis
environment in which Neuromine data from Answer ALS is accessible to approved users.
ADDI is also a supported Neuromine sign-in method. AD Workbench requires separate
credentials from the portal; its support is at support@alzheimersdata.org.

## GNPC (Global Neurodegeneration Proteomics Consortium)
Neuromine (Answer ALS) is a member of the GNPC consortium, and GNPC ran a portion of
the proteomic data. The GNPC brings together 23 contributing cohorts and more than
40,000 biosamples to build one of the largest harmonized neurodegeneration proteomics
datasets; it is funded primarily by Gates Ventures and Johnson & Johnson (Gates
Ventures funded the Answer ALS proteomic analyses). ADDI serves as the GNPC's data
platform partner; joining or GNPC data access is routed to info@neuroproteome.org.

# Section 4: Challenges and downstream use

## Longitude Prize on ALS
Neuromine data is used in the Longitude Prize on ALS: the challenge's competitors work
with Neuromine data to develop algorithms that identify novel drug targets for ALS. The
Prize draws on leading ALS initiatives — including Answer ALS and ALS TDI, both hosted
on Neuromine. It is principally funded by the Motor Neurone Disease (MND) Association
and designed and delivered by Challenge Works, part of Nesta, the UK's innovation agency
for social good. Additional funders include Nesta, the Alan Davidson Foundation, the
My Name'5 Doddie Foundation, LifeArc, FightMND, The 10,000 Brains Project, Answer ALS,
and the Packard Center. Its data and technology partners include Project MinE, ALS
Compute, the New York Genome Center, ALS TDI, Amazon Web Services (AWS), and DNAnexus —
note that the Prize's own compute (AWS, DNAnexus) is separate from Neuromine's Azure
infrastructure.

## GATC Health, Pennington Biomedical Research Center, and Tulane
Answer ALS launched an AI drug-development collaboration with GATC Health, the
Pennington Biomedical Research Center, and Tulane University to advance ALS treatment
discovery through AI-driven analysis of ALS data.

# General Support Reference

For questions about the data, access, downloads, or accounts, contact the Neuromine
Data Portal support team at data@answerals.org.
