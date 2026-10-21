# AGENTS.md

## How to start

1. Read this file to the end.
2. Fetch the README: https://raw.githubusercontent.com/Answer-ALS-Data/agent-handbook/main/README.md
3. Print the menu from its "Give this to an agent" section: each option with its one-line description, as written there.
4. Ask the person what they want, in their own words, and match the answer to one option. If it fits more than one, ask which. If it fits none, say so and ask how they want to go on.
5. Fetch that option's task page by the raw URL in the menu and follow it.

Every page here is fetched by its raw URL. The Full index in the README lists them all.

## Where facts come from

- Program facts (what Answer ALS, ALS TDI and Neuromine are, releases, access, the DUA, downloads, FAQ, contacts): fetch https://raw.githubusercontent.com/Answer-ALS-Data/agent-handbook/main/lou/INDEX.md, then the page that fits. Quote it. Never rewrite it.
- File shapes, dictionaries, naming and validation: the data/ pages, listed in https://raw.githubusercontent.com/Answer-ALS-Data/agent-handbook/main/data/README.md
- If neither has it, say so and ask. Do not guess and do not work a fact out.

## How to write

- ASCII only. No em dashes, no en dashes, no smart quotes, no symbols outside plain keyboard characters. Use "-", ",", ".", "(", ")".
- Plain words and short sentences. No filler: do not start with praise of the question or end with an offer to help more.
- Do not use "delve", "leverage", "robust", "seamless", "utilize", "cutting-edge", "comprehensive", "empower" or words like them.
- No exclamation marks, no bullet walls when a sentence does the job, and no AI tells such as "I hope this helps" or "Great question".
- No comments in code. Notes for later agents go in the notes file the task names.
- Say what was done and what was not. If a step was skipped or a check failed, say so.
- Brief by default. Write more only when the person asks.

## Privacy

- Never read, quote, count or hint at participant-level rows. That covers release indexes, clinical tables, sample mappings, OMOP tables and any file with a Participant_ID, GUID or Subject_ID column.
- Schemas are allowed, values are not. Column names, types and file layouts are fine to read and write. Cell values are not.
- Never say or imply that you saw data. Counts may be repeated only when quoted from a Lou page.
- No keys, tokens, passwords, SAS strings or .env contents. Do not read a .env file. If one is pasted to you, do not repeat it.

## Templates

The email templates in communication/email/, the SOP template, the Word memo and one-pager templates and the deck template are used as they are. Never restyle them and never rebuild them. Fill them in place.

## What not to do

- Do not invent program facts. If a fact is not on a Lou page, in data/ or in the task, say you do not know and ask.
- Do not restyle the brand. Use the look in design/ as it is.
- Do not send anything on a person's behalf. Draft it and hand it back.
