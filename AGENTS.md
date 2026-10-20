# AGENTS.md

## How to start

1. Read this file to the end.
2. Print the menu from the "Give this to an agent" section of README.md: each option with its one-line description, as written there.
3. Ask the person what they want, in their own words.
4. Match the answer to one option. If it fits more than one, ask which.
5. Read that option's page under tasks/ and follow it.

If the answer fits no option, say so and ask how they want to go on.

Read this first. Then read the folder your task touches.

## Who we are

Answer ALS is a research program that collected clinical, genetic, molecular and cell line data from people with ALS and other motor neuron diseases, plus healthy controls. It was a prospective observational study run in clinic at NEALS centers, coordinated by Johns Hopkins and Massachusetts General Hospital, and it is not a clinical trial. The Answer ALS data team curates its releases and publishes them for approved researchers.

ALS TDI is the ALS Therapy Development Institute. Its ARC study (ALS Research Collaborative) collects data that participants mostly report from home through online surveys, plus blood draws and genomics. The Answer ALS data team receives ALS TDI deliveries, checks them and publishes them next to Answer ALS.

Neuromine is the data portal where both programs are published. It started as the Answer ALS Data Portal and was renamed to host more than one program, so the two names mean the same website.

## How to write

- ASCII only. No em dashes, no en dashes, no smart quotes, no symbols outside plain keyboard characters. Use "-", ",", ".", "(", ")".
- Plain words and short sentences.
- No filler openers or closers. Do not start with praise of the question or end with an offer to help more.
- Do not use "delve", "leverage", "robust", "seamless", "utilize", "cutting-edge", "comprehensive", "empower" or words like them.
- No exclamation marks.
- No bullet walls when a sentence does the job.
- No comments in code. Notes for later agents go in the notes file the task names.
- Say what was done and what was not. If a step was skipped or a check failed, say so.

## Privacy

- Never read, quote, count or hint at participant-level rows. That covers release indexes, clinical tables, sample mappings, OMOP tables and any file with a Participant_ID, GUID or Subject_ID column.
- Schemas are allowed, values are not. Column names, types and file layouts are fine to read and write. Cell values are not.
- Never say or imply that you saw data. Published program counts on the programs/ pages are the only counts you may repeat.
- No keys, tokens, passwords, SAS strings or .env contents. Do not read a .env file. If one is pasted to you, do not repeat it.

## How to use this repo

- programs/: what each program is, what it publishes and where it lives, by name only.
- design/: the look of our pages and documents (colors, type, layout).
- communication/: reusable text for emails, release notes and user replies.
- schemas/: column names and file layouts of our releases, never values.

## What not to do

- Do not invent program facts. If a fact is not in this repo or in the task, say you do not know and ask.
- Do not restyle the brand. Use the look in design/ as it is.
- Do not send anything on a person's behalf. Draft it and hand it back.
