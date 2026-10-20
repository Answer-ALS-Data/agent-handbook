# Answer ALS

## What it is

Answer ALS is a prospective, multi-center, longitudinal observational study of people with ALS and other motor neuron diseases, plus healthy controls. Clinical data was collected in clinic by physicians at NEALS centers. The study was coordinated by Johns Hopkins University School of Medicine and Massachusetts General Hospital. It is not a clinical trial.

## Who runs it

The Answer ALS Foundation supports the program and the Neuromine portal. The Answer ALS data team curates each release, writes the release notes and keeps the portal pages current. The data owner on the team signs off on what goes public.

## What it publishes

- Index: one row per participant with availability flags and summary fields, plus two schema files (ElementsDefinition and HierarchyTree). The portal data table is the index under the name aals_dataportal_datatable.csv.
- Clinical: curated clinical forms with a data dictionary and a participant reference table.
- Omics: genomics (WGS), transcriptomics, epigenomics and proteomics, with a sample mapping file that ties samples to participants.
- Cell lines: iPSC and diMN lines. Each product has a Has, Line and For_Sale field in the index. Lines are sold through Cedars-Sinai.
- Splicing: LeafCutter intron matrices.
- QTL: multi-omic cis-QTL results, described by the owner in the release notes.
- High Charts: four combined chart files (sex, age at onset, subject group, race) for the portal home page, shared with ALS TDI.

## Current release

- Public: Release 7 (r7.2.5 is the last confirmed public build). Ask the owner before you call Release 8 public.
- Staged: Release 8. Built, release date not set yet.
- Release 8 index: 1,273 participants, 74 columns.
- Release 8 clinical package: 34 forms for 1,047 participants, in the same shape as Release 7.
- Release 8 splicing matrices: 1,191 sample columns from 1,037 participants, 252,338 introns.
- Release 8 ships no new sample mapping. The portal links to Sample_Mapping_File_April_2026.csv.

Documents for data users say "Release 8", never sub-release labels such as r8.1 or r8.3.

## Where things live

By name only. Never write or ask for SAS strings.

- Neuromine Data Portal: dataportal.answerals.org.
- data.answerals.org: the same portal front end, also used for public document links.
- GitHub organization: Answer-ALS-Data. Scripts live in its repos; data does not.
- Release files and portal documents: in the program's cloud storage, reached only through the portal and the README links. Do not name or guess storage accounts.
- Support contact for users: data@answerals.org.

## Related tools

- Variant Report tool: the Neuromine WGS Variant Report Tool, which lets approved users look up variants in the WGS data. It has its own repo and its own design rules.
- Lou: the portal chatbot that answers user questions from a set of training documents about the programs, the portal and access.

## Words to use

- Say "Neuromine" for the portal and "Answer ALS" for the program.
- Say "participants", not "patients" or "subjects".
- Subject groups: ALS, Asymptomatic ALS Gene Carrier, Non-ALS MND, Healthy Control.
