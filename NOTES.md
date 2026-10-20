# NOTES

Choices made where the first ticket left something open. Dated 2026-10-20.

- House style seed: the operator preferences paragraph named as the seed lived in a session prompt that was not on disk when this was built. The same paragraph is in every board ticket prompt, so that copy was used.
- Style wording: the ASCII rule follows the Hard rules block of the Variant Tool STYLE.md. The banned word list in AGENTS.md adds a few more of the same kind ("utilize", "cutting-edge", "comprehensive", "empower").
- Program facts: taken from the board's topic notes and the Lou training documents. Where they disagree, the board notes win because they are newer.
- Public release: Answer ALS Release 7 is named as public and Release 8 as staged, because Release 8 has no confirmed release date yet. ALS TDI Release 1 is public and Release 2 staged for the same reason. Update both pages on release day.
- Counts: only release-level counts that already appear in release notes or the board's notes are given. No count is broken down below the release level.
- Storage: storage accounts and containers are not named, since the repo is public, and never linked with a SAS.
- Who runs it: the pages name the Answer ALS Foundation, the data team and the data owner by role, not by person.
- communication/ and schemas/ are named in README.md and AGENTS.md. communication/ was added by the communication kit and schemas/ by the schema pages (sections below).
- The repo is public in the Answer-ALS-Data organization since 2026-10-20. It holds the handbook pages and this file. The checker and the build report stay on the board.
- check.py reads no data. It still calls board_check.data_path like the other checkers, so it skips only on a device with no data root in devices.json.

## Design system, 2026-10-20

- Source: the Variant Report tool tokens.css, STYLE.md and variant_reports.py, read from the Variant Tool checkout without changing it, plus the talk deck theme.json and build_deck.py. design/DECISIONS.md lists what was taken and left out.
- Fonts: Helvetica Neue with Arial fallback and Courier New mono for every output, as the talks topic chose, not the web system stack of the tool. One family is plainer than one per medium.
- Status backgrounds are flat (the end color of the tool's gradient), because the brand has no gradients.
- A document size scale in pt (9, 11, 14, 20) was added, since memos need one and neither source had it.
- Logo clear space (half the logo height) and minimum size (38px on screen, 0.5in on a slide) were added; neither source wrote a rule.
- Example headlines and source lines name Release 7 or a fact already in the board notes, so no new count is introduced.
- design/ is not pushed to the GitHub repo by this change; the ticket did not ask for it.

## Communication kit, 2026-10-20

Choices:

- Templates follow the Lou training documents for how access works: the DUA request on the Datasets tab, screening by the team, Data Access Committee review, DocuSign after approval, then the team countersigns. Their words (Datasets tab, Download Data, "How to download Big Data?", Learning Center, Issue Log) are used so users see the same terms in email and on the portal.
- Links in templates are only public URLs from answer-als/links/link-registry.csv marked needs_update=N: dataportal.answerals.org, its /datasets and /learning-center pages, the standardized-omop GitHub repo and data@answerals.org. The release notes pages are still marked for update, so the release announcement leaves that link as a field.
- Counts in examples are only those on the programs/ pages (for example the 1,047 clinical participants of Release 8).
- Escalation is by role: the Data Access Committee for access and commercial use, the data owner for release status and counts, the program lead for partners, funders and the press. The privacy and legal contacts are not named anywhere on the board, so they are fields.
- The Lou training documents name individual staff addresses; the templates use only data@answerals.org and roles.
- Talk outlines use the Title slide and Content slide layouts from design/README.md, with the closing slide on the Title slide pattern.
- Each email template has the headings When to use, Subject, Body and Fill in. check.py reads those headings and looks for exclamation marks inside Body only.
- The one review cadence the documents give ("three times a week") is kept as a field to confirm, not written as fact.

Fields left in the templates. check.py fails if a bracketed field under communication/ is missing from this list.

Facts the team has not settled, to fill once and then keep:

- [Review cadence]: how often the team reviews access requests (access-request-needs-info.md). The Lou documents say three times a week.
- [Follow-up window]: how soon after a meeting the follow-up goes out (meeting-follow-up.md).
- [Standard bug reply time]: the usual time to a first real answer on a bug report (bug-or-data-issue-acknowledged.md).
- [Privacy escalation role]: who takes a possible privacy problem the same day (communication/README.md, bug-or-data-issue-acknowledged.md).
- [Legal escalation role]: who answers DUA terms and legal questions (communication/README.md).
- [Usage figure], [One sentence on use, from a published figure only]: a published usage number, such as approved users (program-update-outline.md). None is in the handbook yet.

Filled per message:

- Every template: [First name], [First name or all], [Program], [Sender name], [Their subject line].
- Access: [Missing item, in one plain sentence], [Reason, as agreed with the Data Access Committee], [What the requester can do next].
- Data question: [Topic], [The answer, with its source], [Where to look next], [What is still open].
- Release: [Release number], [Release date], [Release notes link], [Change 1], [Change 2], [Change 3], [What behaves differently].
- Partner: [Partner organization], [Idea in a few words], [How you know of them], [The proposal], [Proposed times].
- Meeting: [Meeting name], [Meeting date], [Decision], [Owner], [Action], [Due date], [Open question].
- Bug or data issue: [The problem], [Who is looking], [What to do meanwhile], [One ask], [Reply-by date].
- Talks: [Talk date], [live or staged], [Participant count], [One sentence on the state of the program today], [The biggest change in the release, as a sentence], [One sentence on which data types grew], [The next milestone and when], [One line the audience should remember], [One sentence on what the program is, from programs/].

## Schema pages, 2026-10-20

Inputs: the index ElementsDefinition and HierarchyTree files, als-tdi/index/CROSSWALK.csv and NOTES.md, the two clinical dictionaries, the OMOP mapping workbook and etl.ipynb markdown, and the header line of each sample mapping and ALS TDI OMOP file. No data row was used.

Choices:

- Index tables split the ticket's "Facet or Field" into two columns, Facet and Field, because a column can be both.
- Meaning is the Description cut to its first sentence. Where the Description was a bare label, a list of categories or a long rule, it was rewritten in one sentence from the same text, and the categories moved to the vocabulary table. Typos in the source ("nmost", "nueron") were not carried over.
- Group is the parent group of the column's leaf in the HierarchyTree. Columns that are not leaves show "Data table only".
- The Values column of both definition files holds facet range edges, not vocabularies, so those are in their own "Facet ranges" table. Vocabularies come from Description text only (and HierarchyTree text for Site_of_Onset).
- index-shared-columns.md takes vocabularies from als-tdi/index/NOTES.md and adds a Compare verdict (Yes, After recode, With care, No) for each of the 25 names.
- Clinical pages give the form, its label, what it collects, the number of dictionary rows and a few key fields, not every field.
- Field counts are dictionary rows, which is the column count of each form. They are not data counts.
- OMOP pages write the person_source_value grammar as PREFIX_n and identifiers as "prefix plus GUID", with no example value.

Found and not found:

- ALS TDI clinical dictionary: found at clinical/inputs/delivery-r2/clinical_data_package/TDI_data_dictionary.xlsx. It covers 17 tables; TDI_Participants_V2 has no rows in it, and it spells TDI_ACTIVITY as TDI_ACTVITY. The participant table columns (Participant ID, GUID, Cohort) are taken from brain row 29, not from the file.
- ALS TDI sample mapping header has seven columns: Participant ID, Sample ID, GUID, Cell Line, Omic, Vial ID, Timepoint. als-tdi/CONTEXT.md lists nine (also GUID-Batch and Batch #). The page follows the header.
- Answer ALS sample mapping: the input was Sample_Mapping_File_March_2026.csv in data-scripts; the portal links the April 2026 file, which was not read. Column meanings are read from the names and the matching index columns, since no column description ships with the file.
- Sample mapping Participant ID is described as the index Participant_ID form, from the als-tdi decision of 2026-08-28 about updating Participant ID; it was not checked against values.
- Answer ALS clinical Participant_ID is described as the same form as the index Participant_ID, from the answer-als decision of 2026-08-21 that sets the prefix from subject_group_id; it was not checked against values.
- No Answer ALS OMOP output is on the board, so its table list and columns come from the etl.ipynb markdown (the ERD), not from header lines. DEVICE_EXPOSURE has a sheet in the workbook with no mappings and is not built.
- omop_mapping.xlsx maps raceamin to a different concept than the etl.ipynb table states. The page flags it and does not say which is right. Owner to check.
- The ALS TDI OMOP documentation that came with the delivery (2026 OMOP Data Refresh Documentation.docx) was not an input and was not read.

## Deck template, 2026-10-20

Inputs: design/tokens.json, design/README.md, the logo, talks/github-for-researchers/build_deck.py and theme.json, and the title and closing target screenshots in talks/reference/. No operator input.

Choices:

- The script copies the approach of the talk build_deck.py (blank layout, text boxes, brand bars, logo picture) and does not import it, so the handbook stands alone. Title and closing slides use the same positions as the talk deck, which the operator liked.
- Slide size is 7.5 in high and exactly 16:9 wide (12192000 by 6858000 EMU), not 13.333 in, so the 16:9 check is exact. The difference is under 0.001 in.
- One example slide per layout, ten in all. The slide text is the instruction for that slot and the speaker notes hold the one-sentence rule, so the file is its own guide. No real counts or release data appear on any slide.
- Content slides keep the talk deck look: brand blue strip on the left edge, eyebrow, short brand bar, headline in Ink at 40 pt, page number bottom right.
- Content eyebrows are uppercase, as design/README.md says. The title slide eyebrow keeps the mixed case of the target screenshot (bold program name, then regular text).
- Body lines use 22 pt (the subline size), table cells, chart labels and the picture slot text 16 pt (command and chart label size), captions and source lines 14 pt in Caption. tokens.json has no slide body or caption size, so the nearest existing sizes were used and none was added.
- Numbers use 54 pt in Brand, the title headline size. The takeaway sentence also uses 54 pt in Brand.
- The section divider has no logo and no eyebrow: the ticket asks for one headline only.
- Table header fill is Tint 1 #EEF4FF, as the ticket asks ("tint header"). design/README.md names Table head #F4F6FB for web tables; the two are close, and the slide follows the ticket. The rule under the header is #D8DCE5, every other line is Table border #DFE3EB. The table uses PowerPoint's No Style, No Grid style so only these colors show.
- The chart is a native clustered column chart with three series in chart_1 to chart_3, axis text in #6A7683 and grid lines in #D9E1EA. The example values and labels are placeholders (Category 1, Series 1).
- The picture slot is a Tint 1 box with a Rule line; the user deletes it and inserts the picture in its place. A real PowerPoint picture placeholder needs a slide layout in the master, which the blank-layout approach does not build.
- The built pptx lives only under the data root, like the talk deck. Hand edits there are lost on rebuild; the how-to says to copy the file before editing.

## Word templates, 2026-10-20

Inputs: design/tokens.json, design/README.md and the page setup of ALSTDI-SOP-001-V1 (the board copy under the data root, read only): Letter, 1 inch margins, header and footer 0.5 inch from the edge, empty header, page number in the footer. No operator input. python-docx 1.2.0.

Choices:

- Header and footer follow the SOP: empty header, footer 0.5 inch from the edge. The footer reads "Answer ALS" on the left and "Page n" on the right in Caption size and Placeholder grey, instead of the SOP's "Page | n".
- Sizes are the document sizes in tokens.json: Title 20 pt, Heading 1 14 pt, Heading 2 and Body 11 pt, Caption 9 pt. tokens.json has no Heading 2 size, so it uses the body size in bold brand blue; none was added.
- Title, Heading 1 and Heading 2 are brand blue #1F4FAE in bold, as the ticket asks. design/README.md names Ink for headings on a page; the ticket wins for these files.
- Body line spacing is exactly 11 x 1.6 = 17.6 pt (tokens line_height). Table cells and the number row use single spacing so the one-pager stays short.
- The font is Helvetica Neue, and word/fontTable.xml names Arial as its altName, which is how Word records a fallback. docDefaults and every style name Helvetica Neue directly, with no theme fonts, so the theme cannot swap it.
- The thin brand blue rule is a bottom border on the last paragraph of the title block (the Subject line in the memo, the headline in the one-pager), not part of the Title style, so a Title used elsewhere has no rule.
- Callout is a paragraph style with Tint 1 #EEF4FF shading and a border in the same tint, so it reads as a padded box with no visible edge. Consecutive Callout paragraphs join into one box.
- Table Grid borders use Table border #DFE3EB, the table color in design/README.md. The ticket says "brand rule color"; Rule #E5E7EB is the light divider and fails the 3:1 line rule just as much, and #DFE3EB is the token for table edges. The example table header has the Table head #F4F6FB fill and a #D8DCE5 rule, as design/README.md says.
- The three numbers on the one-pager sit in a borderless 3 column table (no style), 20 pt bold brand blue over a Caption label.
- Heading 1 and Heading 2 carry outline levels and no numbering, so no auto-number can appear (brain row 24).
- Builds are byte for byte the same: core properties use a fixed date of 2026-10-20 and the zip entries a fixed time. A rebuild changes the sha256 only when the script or tokens.json changes.
- A letter has no template of its own; the how-to says to start from the memo.
- Page count: neither docx2pdf nor LibreOffice is installed on the board's Windows device, so check.py prints "page count not checked". Word is installed but was not driven, since that can open a window on the operator's desktop. The one-pager placeholder text was kept short so it should fit; the operator checks by opening it in Word.

## Menu and tasks, 2026-10-20

- The menu is a bullet list, no numbers, as the ticket asks. Each line reads "- Option (tasks/page.md): description" so the agent sees which page to open and check.py can tie each option to its page.
- Option names follow the ticket wording with a capital first letter: Draft an email, Build a slide deck, Write a memo or one-pager, Create an SOP, Answer a question about the data files, Answer a question about a program, Review a draft against the house style.
- Descriptions say what the person gets back, not how the agent works, in one line each.
- The README section ends with one line for requests that fit no option, matching the How to start rule in AGENTS.md.
- AGENTS.md keeps its old opening line ("Read this first. Then read the folder your task touches.") after the new section, since the ticket allows no other change there.
- Paths under Read first are from the handbook root. The built pptx and docx are named in Steps, not Read first, because on the board they live on the data root; in the GitHub repo they sit in design/templates/.
- Menu files and tasks/ pages are checked against the AGENTS.md banned list; AGENTS.md itself is not, since it holds the list.
- tasks/create-sop.md is a one-line placeholder until the SOP kit ticket writes it.

## SOP kit, 2026-10-20

Inputs: the house SOP template, AALS-SOP-005-V1 (docx and pdf) and ALSTDI-SOP-001-V1, dropped by the operator. Only headings, tables and page setup were read with python-docx; no body text was copied into the handbook.

Choices:

- The template is shipped byte for byte as the team uses it, not rebuilt from tokens.json like the memo and deck. It keeps its own look (Calibri, black headings).
- The template has no paragraph in the Heading 2 style. Its five section names and its two "Heading 2" step lines are Normal paragraphs with automatic numbers. sop-template.md says to fill those in place and never to apply the Heading 2 style; a test fill with python-docx kept every number. check.py reads both kinds of heading from the template.
- Step numbers under Procedures are fixed as 4.n in the template's numbering, so the page says to keep all five sections in order.
- The house rules are the ones the finished SOPs follow. The 700 to 1,000 word budget is the ALS TDI SOP's; the older Answer ALS SOPs are shorter (005 and 006 are about 350 words). The page says not to pad a short process.
- The step shape (Inputs, Steps, Outputs, Checks) is named as ALS TDI SOP-001 uses it, as a pattern, not a rule.
- Neuromine is named as a program with the NEUROMINE- prefix because a finished SOP uses it, though it has no programs/ page.

Publishing (resolved when the repo went public, see Public repo guard below):

- The worked example (examples/, AALS-SOP-005-V1) named a staff member on its cover, on the Last Modified By line, and both files named staff members as author or last editor in their file properties. The title table holds no name.
- The example held one identifier shaped example value in its body text (docx and pdf).
- The originals stay as they are on the data root. The GitHub repo gets cleaned copies from the data root folder answer-als/agent-handbook/v1/public/.

## Public repo guard, 2026-10-20

The repo went public on 2026-10-20 so a bare link works in any agent. check.py now runs a public repo guard over every handbook text file and the text of every docx and pptx that is published (paragraphs, tables, headers, footers, the title table, slide text and notes, file author fields, and the pdf text). It fails on: a storage account name, a host from the link registry other than answerals.org and its subdomains and github.com, an Azure app, blob, static site or Front Door host, a named storage container, a SAS signature, an absolute Windows drive or Mac volume path, a ticket id in the form # and a number, a known staff name, or the board device name.

Choices:

- The link registry has no host column, so the guard takes the host of each url. It allows every answerals.org subdomain, since dataportal.answerals.org is the public portal the pages send users to.
- A hex color such as #008300 is not a ticket id: the guard matches # and one to five digits only when no further hex character follows.
- People's names cannot be found by pattern, so the guard holds a short list of the names found in the handbook files and the SOP files. Add a name there when a new file brings one.
- The SOP example pdf could not be rebuilt from the docx (no Word export on the board without a window), so its text was replaced in place with PyMuPDF redactions in the same place and size.

Strings replaced, and where:

- programs/answer-als.md, Where things live: the two lines naming the release storage account and its container, and the portal storage account and its container, became one line saying release files and documents are reached through the portal and the README links, without naming storage.
- design/templates/deck-template.md, docx-templates.md and sop-template.md, Files line: the absolute data root paths for both devices and the board device name became "under the data root at answer-als/agent-handbook/v1/templates/", plus where the files sit in the GitHub repo.
- design/tokens.json, source: the absolute path of the Variant Tool checkout became "Variant Tool docs/design/tokens.css".
- communication/email/data-question-reply.md: the cell line vendor link (a link registry host) became the vendor named, with its catalog named, not linked.
- schemas/index-answer-als-r8.md, has_discordant_sample: the lab named after a person became "MIT".
- NOTES.md: two ticket ids, one absolute path, the board device name and the vendor host removed; the Storage and repo lines now say the repo is public.
- SOP template copy (answer-als-sop-template.docx): file author changed from a staff name to "Answer ALS data team". Paragraph text had no name.
- SOP example copy (AALS-SOP-005-V1 docx): the staff name on the Last Modified By line became "Answer ALS data team"; file author and last modified by became "Answer ALS data team"; the example SubjectUID became NEUxxxxxxxx in both places (the given value and the CASE- value), matching the CASE-NEUxxx form the same SOP uses later.
- SOP example copy (AALS-SOP-005-V1 pdf): the same name and example SubjectUID replaced in the page text; the pdf author field set to "Answer ALS data team".
