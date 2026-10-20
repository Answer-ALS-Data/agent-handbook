# SOP template

The house template for a standard operating procedure (SOP). Every SOP for Answer ALS, ALS TDI and Neuromine starts from it. It is shipped as the team uses it. Never rebuild it or restyle it.

Files: answer-als-sop-template.docx, and a finished example in examples/ (AALS-SOP-005-V1. Clinical Data Curation, docx and pdf). In the GitHub repo they are in design/templates/ and design/templates/examples/. On the board they sit under the data root at answer-als/agent-handbook/v1/templates/, not in the board repo.

## What the template holds

Letter size, 1 inch margins, header and footer 0.5 inch from the edge. The header is empty. The footer reads "Page | n", with n a page number field.

Page 1, the cover:

- The title "Standard Operating Procedure".
- The title table, one row of three cells: Title (<Title>), Version Number (<#>) and Effective Date (<Date>). The labels are bold; replace only the text in angle brackets.
- The title "Revision History" and its table: a header row (Version Number, Effective Date, Description) and three empty rows.
- A "Last Modified By:" and "Date:" line over two underscore lines, then a page break.

Page 2 on, the procedure. The title "Standard Operating Procedure" again, then five numbered sections, in this order:

1. Purpose
2. Scope
3. Definitions/Acronyms
4. Procedures
5. References

The section names are bold Normal paragraphs with automatic numbers (1 to 5). They are not Heading styles. Purpose, Scope, Definitions/Acronyms and References each hold one "Instruction:" line that says what goes there; replace it with your text.

- Definitions/Acronyms has two numbered term lines (3.1, 3.2) that read "First Term: ..." and "Second Term: ...".
- Procedures has two step headings that read "Heading 2" (numbered 4.1, 4.2), followed by two "Example bullets" lines one level down.

The "Heading 2" lines are the step headings of the SOP. Like the section names, they are Normal paragraphs with their own automatic number, not the Heading 2 style.

## Fill it in place

Fill the template itself, never a new document. Copy the file, rename the copy, and change only text. Do not change styles, fonts, numbering, the tables or the footer.

With python-docx:

1. Open the copy with Document(path).
2. To change a line, put the new text in its first run and remove its other runs. The paragraph keeps its style, its number and its bold.
3. To add a step heading, term line or bullet, deepcopy the XML of a paragraph of the same kind (paragraph._p) and insert it with addnext, then change its text. That keeps the automatic number.
4. Remove unused lines with p._p.getparent().remove(p._p). Remove every "Instruction:" line and every leftover placeholder.
5. Keep the three leading spaces of the step and term lines as the template has them.
6. Do not set paragraph.style to "Heading 2" or any other style. In this template that drops the automatic number.
7. In table cells, change the run that holds <Title>, <#> or <Date> and leave the bold label run alone.
8. Replace the underscore line under Last Modified By and Date with the author name and the date.

Step numbers under Procedures are fixed as 4.1, 4.2 and so on, so keep all five sections in their order.

The finished SOPs give each step the same short shape: what goes in, what you do, what comes out and one check. ALS TDI SOP-001 writes that as four lines under each step heading: Inputs, Steps, Outputs, Checks.

## House rules

- ASCII only. Word turns straight quotes into curly quotes and two hyphens into a dash as you type; turn that off or replace them before you hand back.
- Short plain sentences. Write for someone who runs the process for the first time.
- Word budget: 700 to 1,000 words, hard cap 1,100. Count the words of every body paragraph and table cell as python-docx reads them. Cut before you go over; do not pad a short process to reach 700, say so instead.
- One "what is verified against what" check per stage, written as one sentence that starts with Verify.
- One final validation section, as the last step under Procedures: a short list of "X against Y" checks run before handoff.
- References: "None." when nothing outside the SOP is cited.
- No typed section numbers on headings. The template numbers them; a typed number shows twice in the PDF.
- No ticket ids, tracker names or board paths in the text.
- A revised SOP stays at V1. Add a new Revision History row (Version Number 1, the date, what changed) unless the owner asks for V2.
- Cite index columns by name, never by letter. Letters move when a column is added.
- Dates as YYYY-MM-DD. Version Number as a plain number, 1.

## Names and numbers

Each program has its own prefix:

| Program | Prefix | Example |
|---|---|---|
| Answer ALS | AALS- | AALS-SOP-005-V1 |
| ALS TDI | ALSTDI- | ALSTDI-SOP-001-V1 |
| Neuromine | NEUROMINE- | NEUROMINE-SOP-001-V1 |

The file name is the code, a period, a space and the title: "AALS-SOP-005-V1. Clinical Data Curation.docx". The data owner assigns the number. Until then write NNN in the file name and leave the code out of the text.

## The PDF

The owner exports the PDF from Word when the SOP is cleared. If you export one, read the text of the PDF, not the docx, and check that no heading shows two numbers.
