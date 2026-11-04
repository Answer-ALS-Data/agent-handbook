---
name: answer-als-document-skill
description: Brand rules, templates and checkers for Answer ALS documents, decks, sheets, pages and figures, for use with any Answer ALS, ALS TDI or Neuromine output.
---

# Answer ALS Document Skill

Brand rules and templates for Answer ALS outputs. It covers the shared brand (palette, type, layout, voice) and, as they are written, the rules for each output format.

## What it covers

- https://raw.githubusercontent.com/Answer-ALS-Data/agent-handbook/main/references/brand.md: the brand rules every format shares.
- https://raw.githubusercontent.com/Answer-ALS-Data/agent-handbook/main/references/word.md: rules for Word documents (.docx), including SOPs.
- https://raw.githubusercontent.com/Answer-ALS-Data/agent-handbook/main/references/powerpoint.md: rules for PowerPoint decks (.pptx).
- https://raw.githubusercontent.com/Answer-ALS-Data/agent-handbook/main/references/excel.md: rules for Excel workbooks (.xlsx): counts tables and small summaries.
- https://raw.githubusercontent.com/Answer-ALS-Data/agent-handbook/main/references/markdown.md: rules for Markdown files (.md): READMEs, reports and notes.
- https://raw.githubusercontent.com/Answer-ALS-Data/agent-handbook/main/references/html.md: rules for single-file HTML pages (.html).
- https://raw.githubusercontent.com/Answer-ALS-Data/agent-handbook/main/assets/README.md: ready-made templates and sample files, one set per format as each format file lands, each by raw URL. The logo is https://raw.githubusercontent.com/Answer-ALS-Data/agent-handbook/main/design/assets/answer-als-logo-light.png.
- scripts/: the checkers for finished files and the runner. See https://raw.githubusercontent.com/Answer-ALS-Data/agent-handbook/main/scripts/README.md.

## How to use it

1. Read https://raw.githubusercontent.com/Answer-ALS-Data/agent-handbook/main/references/brand.md in full, first.
2. Then read the one file under references/ that matches the output format.
3. If a matching template exists under assets/, start from it instead of a blank file. Fill it in place; never restyle or rebuild it.
4. Where a format file and brand.md disagree, the format file wins for that format.
5. For a format with no file under references/ yet, apply brand.md and say so in the output.
6. When a checker exists for the format, run it on the finished file and fix every FAIL.

Writing rules (voice, punctuation, banned words) live in brand.md and apply to every format.
