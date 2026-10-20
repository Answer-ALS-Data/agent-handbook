# Word templates

The standard Answer ALS memo and one-pager. Start every memo, letter and one-page summary from one of them so they look like the deck and the same program.

Files: answer-als-memo-template.docx and answer-als-one-pager-template.docx. In the GitHub repo they are in design/templates/. On the board they are built under the data root at answer-als/agent-handbook/v1/templates/, not in the board repo.

Both are Letter size with 1 inch margins. The title block ends in a thin brand blue rule. The footer shows the program name on the left and the page number on the right. Every text in square brackets is the instruction for that spot, with its word limit. Replace it, brackets and all.

## Use it

1. Copy the file and rename the copy for your document. Never edit the template itself; a rebuild overwrites it.
2. Open the copy in Word.
3. Replace each bracketed instruction with your text. Keep the style that is already on the paragraph.
4. Delete any section or slot you do not need, such as the Ask section of a memo with no ask.
5. For a letter, start from the memo: change the title to Letter, keep To, From, Date and Subject, and write the body under Summary and What is next only.

## The styles

Apply styles by name, from the Styles pane in Word or with python-docx (paragraph.style = "Body"). Do not format by hand.

| Style | Use it for |
|---|---|
| Title | The memo title or the one-pager headline. 20 pt, brand blue. One per document. |
| Heading 1 | A section heading. 14 pt, brand blue. |
| Heading 2 | A step or part inside a section. 11 pt, brand blue. |
| Body | All running text, the To to Subject lines and table cells. 11 pt. |
| Caption | Source lines, number labels and notes under a table. 9 pt grey. |
| Callout | A tint box for the one thing the reader must act on: the Ask, How to get access. |
| Table Grid | Tables. Thin grey borders; put the header row in bold on the light head fill, as the example table does. |

## The memo

To, From, Date and Subject, the rule, then five sections: Summary, Background, What we did, What is next and Ask. The word limits are in each section's text. A memo is at most two pages; if it runs longer, cut Background and What we did first.

## The one-pager

A headline, one paragraph, three numbers with labels in a row, a short table with a source line, a How to get access box and a contact line.

## Rules

- One page is one page. If the text does not fit, cut words. Do not shrink the type, the margins or the spacing.
- Numbers come from the release index or the published release notes, never from a data file you opened yourself. Name the release in the label or the source line. See AGENTS.md, Privacy.
- No participant identifiers, rows or small counts that could point to a person.
- No SAS or expiring links. Name the portal page or use a public link from answer-als/links/link-registry.csv.
- ASCII text only, as in AGENTS.md. Word turns straight quotes into curly quotes and two hyphens into a dash as you type; turn that off (File, Options, Proofing, AutoCorrect Options, AutoFormat As You Type) or replace them before you send.
- The logo goes only on brand blue. These templates are white pages, so the program name is written in the footer instead.
- Do not add colors, fonts or sizes. Everything comes from design/tokens.json and design/README.md.

## Rebuild it

The templates are built by design/templates/build_docx_templates.py from design/tokens.json. When the tokens change, rebuild; never fix the look by hand in the docx.

From the repo root:

    python answer-als/agent-handbook/design/templates/build_docx_templates.py

It reads the data root from devices.json (through board_check.data_path) and overwrites both files. The build gives the same bytes each time, so the sha256 changes only when the script or tokens.json changes. Then run python check.py answer-als/agent-handbook and put any new sha256 in answer-als/agent-handbook/REPORT.md.

Fonts: Helvetica Neue for text. The file names Arial as its stand-in, so Word on a computer without Helvetica Neue shows Arial.

On the MacBook: use python3, not python. If python-docx fails to import, run it as arch -arm64 python3 answer-als/agent-handbook/design/templates/build_docx_templates.py. The script also retries under arch -arm64 on its own.
