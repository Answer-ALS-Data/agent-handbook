# OMOP tables: columns and joins

Both cohorts have their clinical data in the OMOP Common Data Model (CDM) as well: one CSV per OMOP table, keyed by person_id. This page lists the tables per cohort, their columns, how source values are mapped to OMOP concepts, and how to join an OMOP person back to the index and clinical files. It describes columns, never values.

## Answer ALS

The owner's notebook etl.ipynb (data-scripts, Answer ALS/Data Curation/OMOP) builds the tables from the curated clinical forms, using the mapping workbook omop_mapping.xlsx beside it. No Answer ALS OMOP output is kept on the board; the Release 8 notes hold a placeholder for it.

Tables the notebook builds: PERSON, VISIT_OCCURRENCE, DRUG_EXPOSURE, CONDITION_OCCURRENCE, PROCEDURE_OCCURRENCE.

| Table | Built from | Columns |
|---|---|---|
| PERSON | Demographics | person_id, gender_concept_id, year_of_birth, month_of_birth, day_of_birth, birth_datetime, race_concept_id, ethnicity_concept_id, location_id, provider_id, care_site_id, person_source_value, gender_source_value, gender_source_concept_id, race_source_value, race_source_concept_id, ethnicity_source_value, ethnicity_source_concept_id |
| VISIT_OCCURRENCE | Each distinct Participant_ID and Visit_Date | visit_occurrence_id, person_id, visit_concept_id, visit_type_concept_id, visit_start_date, visit_start_datetime, visit_end_date, visit_end_datetime, provider_id, care_site_id, visit_source_concept_id, admitted_from_concept_id, admitted_from_source_value, discharged_to_concept_id, discharged_to_source_value, preceding_visit_occurrence_id |
| DRUG_EXPOSURE | ANSWER_ALS_Medications_Log | drug_exposure_id, person_id, drug_concept_id, drug_exposure_start_date, drug_exposure_start_datetime, drug_exposure_end_date, drug_exposure_end_datetime, verbatim_end_date, drug_type_concept_id, stop_reason, refills, quantity, days_supply, sig, route_concept_id, lot_number, provider_id, visit_occurrence_id, visit_detail_id, drug_source_value, drug_source_concept_id, route_source_value, dose_unit_source_value |
| CONDITION_OCCURRENCE | NEUROLOG, one row per diagnosis column | condition_occurrence_id, person_id, condition_concept_id, condition_start_date, condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id, condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id, visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value |
| PROCEDURE_OCCURRENCE | Tracheostomy | procedure_occurrence_id, person_id, procedure_concept_id, procedure_date, procedure_datetime, procedure_end_date, procedure_end_datetime, procedure_type_concept_id, modifier_concept_id, quantity, provider_id, visit_occurrence_id, visit_detail_id, procedure_source_value, procedure_source_concept_id, modifier_source_value |

Rules in the notebook:

- person_id is a new integer counted up by the ETL. person_source_value is the clinical Participant_ID, so it has the index Participant_ID form (CASE- or CTRL- plus the GUID).
- Clinical day counts become dates by adding them to a fixed baseline of 2016-01-01. These are not real calendar dates.
- A missing date is filled with the placeholder 2099-01-01. Treat that date as missing.
- NEUROLOG gives only a diagnosis date, so condition start and end are the same day.
- Fields the source does not have are left empty.

### Mapping types in omop_mapping.xlsx

The workbook has one sheet per table. Each row maps one source code or value to an OMOP concept id.

| Sheet | Source | Map type | What it maps |
|---|---|---|---|
| ALL | (any) | report_concept | The type concept used for visit_type_concept_id |
| PERSON | demographics | sex | Sex code to gender concept |
| PERSON | demographics | raceamin, raceasn, raceblk, racenh, racewt | Each race flag to a race concept |
| PERSON | demographics | ethnicity | Ethnic category code to ethnicity concept |
| VISIT_OCCURRENCE | (any) | visit_concept | The concept used for visit_concept_id |
| DRUG_EXPOSURE | answer_als_medications_log | route | medrte code to route concept |
| DRUG_EXPOSURE | answer_als_medications_log | medication | Lower-cased medication name to drug concept |
| CONDITION_OCCURRENCE | neurolog | condition | NEUROLOG diagnosis code to condition concept |
| PROCEDURE_OCCURRENCE | tracheostomy | tracheostomy | Tracheostomy to procedure concept |
| DEVICE_EXPOSURE | (none) | (none) | Header only, no mappings |

The workbook and the notebook text disagree on the concept for raceamin (American Indian or Alaska Native). Check both before you rely on that mapping.

## ALS TDI

ALS TDI delivers its own OMOP tables in CDM v5.4 with Release 2. The board publishes them unchanged with a SHA256SUMS file. Nine tables:

| Table | Columns |
|---|---|
| person | person_id, gender_concept_id, year_of_birth, month_of_birth, day_of_birth, birth_datetime, race_concept_id, ethnicity_concept_id, location_id, provider_id, care_site_id, person_source_value, gender_source_value, gender_source_concept_id, race_source_value, race_source_concept_id, ethnicity_source_value, ethnicity_source_concept_id |
| observation_period | observation_period_id, person_id, observation_period_start_date, observation_period_end_date, period_type_concept_id |
| visit_occurrence | visit_occurrence_id, person_id, visit_concept_id, visit_start_date, visit_start_datetime, visit_end_date, visit_end_datetime, visit_type_concept_id, provider_id, care_site_id, visit_source_value, visit_source_concept_id, admitted_from_concept_id, admitted_from_source_value, discharged_to_concept_id, discharged_to_source_value, preceding_visit_occurrence_id |
| condition_occurrence | condition_occurrence_id, person_id, condition_concept_id, condition_start_date, condition_start_datetime, condition_end_date, condition_end_datetime, condition_type_concept_id, condition_status_concept_id, stop_reason, provider_id, visit_occurrence_id, visit_detail_id, condition_source_value, condition_source_concept_id, condition_status_source_value |
| drug_exposure | drug_exposure_id, person_id, drug_concept_id, drug_exposure_start_date, drug_exposure_start_datetime, drug_exposure_end_date, drug_exposure_end_datetime, verbatim_end_date, drug_type_concept_id, stop_reason, refills, quantity, days_supply, sig, route_concept_id, lot_number, provider_id, visit_occurrence_id, visit_detail_id, drug_source_value, drug_source_concept_id, route_source_value, dose_unit_source_value |
| measurement | measurement_id, person_id, measurement_concept_id, measurement_date, measurement_datetime, measurement_time, measurement_type_concept_id, operator_concept_id, value_as_number, value_as_concept_id, unit_concept_id, range_low, range_high, provider_id, visit_occurrence_id, visit_detail_id, measurement_source_value, measurement_source_concept_id, unit_source_value, unit_source_concept_id, value_source_value, measurement_event_id, meas_event_field_concept_id |
| observation | observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id, value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id, observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, value_source_value, observation_event_id, obs_event_field_concept_id |
| death | person_id, death_date, death_datetime, death_type_concept_id, cause_concept_id, cause_source_value, cause_source_concept_id |
| care_site | care_site_id, care_site_name, place_of_service_concept_id, location_id, care_site_source_value, place_of_service_source_value |

ALS TDI's own mapping from its source tables to concepts is described in the documentation that came with the delivery, not in the owner's workbook.

### person_source_value grammar (ALS TDI)

person_source_value is a cohort word, an underscore and the numeric ARC participant number: PREFIX_n.

- PREFIX is one of three words: CASE (ALS), CONTROL (healthy volunteer) or ASYMP (asymptomatic carrier).
- n is the participant number without leading zeros.

The clinical package uses only two prefixes, CASE- and CTRL-, joined to the GUID with a hyphen. So the prefixes do not line up: a CONTROL_ or an ASYMP_ person both have a CTRL- GUID.

## Join rules

- Inside OMOP, every table joins to person on person_id. person_id is an ETL counter; never join it to anything outside OMOP.
- Answer ALS: person_source_value equals the clinical and index Participant_ID.
- ALS TDI: take person_source_value, drop the prefix and the underscore, read the rest as an integer, and join it to Participant ID in TDI_Participants_V2 (and so to every clinical table). Never match the OMOP prefix to the GUID prefix.
- ALS TDI check after the join: the OMOP prefix must agree with the participant's clinical cohort (ALS Patient or ALS Patient - Reversals is CASE, Healthy Volunteer is CONTROL, Asymptomatic Carrier is ASYMP).
- To reach the index from ALS TDI OMOP, go through the participant table: numeric Participant ID, then GUID, which holds the index Participant_ID form.

## Source

omop_mapping.xlsx and the markdown cells of etl.ipynb in data-scripts (read only), the header lines of the nine ALS TDI Release 2 OMOP files, brain row 29 and the als-tdi decision of 2026-09-18.
