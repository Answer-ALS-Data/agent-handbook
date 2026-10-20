# Answer a question about the data files

## What you get

A plain answer about what a column, form or file holds and how the files join, taken from the schema pages.

## Read first

- AGENTS.md
- schemas/README.md
- schemas/index-shared-columns.md
- programs/answer-als.md
- programs/als-tdi.md

## Steps

1. If the person did not say which program (Answer ALS or ALS TDI) and which file or column, ask.
2. Find the page in schemas/ for that file: the index pages, the clinical pages, sample-mapping.md or omop.md. schemas/README.md lists them and gives the join keys.
3. Answer from the page: column names, types, codes from a dictionary and file layouts. Columns and layouts, never values. Do not open a data file and do not quote, count or hint at any row.
4. If the question needs values or counts, say the schema pages cannot answer it. Give the published counts from programs/ if they fit, or say who to ask.
5. If the page does not have the answer, say you do not know.

## Hand back

The answer in a few sentences, naming the schema page it came from. Never send it to anyone. The person passes it on.
