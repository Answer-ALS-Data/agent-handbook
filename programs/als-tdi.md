# ALS TDI

## What it is

ALS TDI is the ALS Therapy Development Institute. Its data comes from the ARC study (ALS Research Collaborative). Participants report most of their clinical data from home through online surveys: ALSFRS-R self-assessments, medical history, family history, medications, supplements and more. It also collects blood draws, genomics and transcriptomics.

## Who runs it

The ALS TDI team runs the ARC study and delivers each release to the Answer ALS data team. The data team checks the delivery, builds the index and sample mapping, writes the release notes and publishes it on Neuromine next to Answer ALS. The data owner on the team signs off on what goes public.

## What it publishes

- Index: one row per participant with availability flags and summary fields, plus two schema files (ElementsDefinition and HierarchyTree). The portal data table has the same content as the index.
- Clinical: curated clinical tables from the ARC surveys.
- OMOP: a copy of the OMOP CDM v5.4 tables as delivered.
- Sample mapping: ties each genomics and transcriptomics sample to a participant and a timepoint.
- Release notes and a README.
- High Charts: the four combined chart files shared with Answer ALS.

## Current release

- Public: Release 1. Index of 1,290 participants.
- Staged: Release 2. Built, go-live date set by the owner.
- Release 2 index: 1,688 rows, 39 columns.
- Release 2 clinical: 19 tables. Release 2 delivered 708 participants.
- Release 2 OMOP: 9 CDM v5.4 tables, 708 persons.
- Release 2 sample mapping: 1,267 rows, 703 genomics and 564 transcriptomics.

Documents for data users say "Release 2", never labels such as r2.3 or r2.5.

## Index names

Since index r2.5 the ALS TDI index uses the Answer ALS Release 8 column names, so both programs share one set of names. Only names changed; values were not recoded. Examples: Ethnicity became RACE, Family_with_Als became Sporadic_Familial, the ExpansionHunter repeat lengths became C9orf72_repeat_length and ATXN2_repeat_length, and the availability flags became EH_C9orf72 and EH_ATXN2. r2.5 is built but not on Neuromine yet; Release 2 goes live with the r2 names.

## Sample mapping

Columns: Participant ID, Sample ID, GUID-Batch, GUID, Cell Line, Omic, Batch #, Vial ID, Timepoint. Timepoints count from 1 per participant and omic (-G for genomics, -T for transcriptomics). Cell Line is Blood by default.

## Where things live

By name only. Never write or ask for SAS strings.

- Neuromine Data Portal: dataportal.answerals.org, the same portal as Answer ALS.
- data.answerals.org: the portal front end, also used for public document links.
- GitHub organization: Answer-ALS-Data. The ALS TDI curation scripts live in the data-scripts repo.
- Support contact for users: data@answerals.org.

## Related tools

- Variant Report tool: the Neuromine WGS Variant Report Tool.
- Lou: the portal chatbot. It holds the ALS TDI Release 1 index today.

## Words to use

- Say "ALS TDI" for the program and "ARC study" for the study.
- Participant types include ALS cases and healthy controls.
