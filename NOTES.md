# NOTES

Choices made where the first ticket left something open. Dated 2026-10-20.

- House style seed: the operator preferences paragraph named as the seed lived in a session prompt that was not on disk when this was built. The same paragraph is in every board ticket prompt, so that copy was used.
- Style wording: the ASCII rule follows the Hard rules block of the Variant Tool STYLE.md. The banned word list in AGENTS.md adds a few more of the same kind ("utilize", "cutting-edge", "comprehensive", "empower").
- Program facts: taken from the board's topic notes and the Lou training documents. Where they disagree, the board notes win because they are newer.
- Public release: Answer ALS Release 7 is named as public and Release 8 as staged, because Release 8 has no confirmed release date yet. ALS TDI Release 1 is public and Release 2 staged for the same reason. Update both pages on release day.
- Counts: only release-level counts that already appear in release notes or the board's notes are given. No count is broken down below the release level.
- Storage: storage accounts and containers are not named, since the repo is public, and never linked with a SAS.
- Who runs it: the pages name the Answer ALS Foundation, the data team and the data owner by role, not by person.
- communication/ and schemas/ are named in README.md and AGENTS.md. communication/ was added by the communication kit and schemas/ by the schema pages (sections below). (communication/ removed 2026-11-04; schemas/ is now data/.)
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

communication/ and its eight email templates were removed 2026-11-04 (see Two services below). The lines in this section are kept as history.

Choices:

- Templates follow the Lou training documents for how access works: the DUA request on the Datasets tab, screening by the team, Data Access Committee review, DocuSign after approval, then the team countersigns. Their words (Datasets tab, Download Data, "How to download Big Data?", Learning Center, Issue Log) are used so users see the same terms in email and on the portal.
- Links in templates are only public URLs from answer-als/links/link-registry.csv marked needs_update=N: dataportal.answerals.org, its /datasets and /learning-center pages, the standardized-omop GitHub repo and data@answerals.org. The release notes pages are still marked for update, so the release announcement leaves that link as a field.
- Counts in examples are only those on the programs/ pages (for example the 1,047 clinical participants of Release 8). (programs/ removed 2026-10-21; counts are now quoted from a Lou page.)
- Escalation is by role: the Data Access Committee for access and commercial use, the data owner for release status and counts, the program lead for partners, funders and the press. The privacy and legal contacts are not named anywhere on the board, so they are fields.
- The Lou training documents name individual staff addresses; the templates use only data@answerals.org and roles.
- Talk outlines use the Title slide and Content slide layouts from design/README.md, with the closing slide on the Title slide pattern. (talks/ removed 2026-10-21.)
- Each email template has the headings When to use, Subject, Body and Fill in. check.py reads those headings and looks for exclamation marks inside Body only.
- The one review cadence the documents give ("three times a week") is kept as a field to confirm, not written as fact.

Fields left in the templates. check.py fails if a bracketed field under communication/ is missing from this list.

Facts the team has not settled, to fill once and then keep:

- [Review cadence]: how often the team reviews access requests (access-request-needs-info.md). The Lou documents say three times a week.
- [Follow-up window]: how soon after a meeting the follow-up goes out (meeting-follow-up.md).
- [Standard bug reply time]: the usual time to a first real answer on a bug report (bug-or-data-issue-acknowledged.md).
- [Privacy escalation role]: who takes a possible privacy problem the same day (communication/README.md, bug-or-data-issue-acknowledged.md).
- [Legal escalation role]: who answers DUA terms and legal questions (communication/README.md).
- [Usage figure], [One sentence on use, from a published figure only]: a published usage number, such as approved users (program-update-outline.md). None is in the handbook yet. (Removed 2026-10-21 with talks/.)

Filled per message:

- Every template: [First name], [First name or all], [Program], [Sender name], [Their subject line].
- Access: [Missing item, in one plain sentence], [Reason, as agreed with the Data Access Committee], [What the requester can do next].
- Data question: [Topic], [The answer, with its source], [Where to look next], [What is still open].
- Release: [Release number], [Release date], [Release notes link], [Change 1], [Change 2], [Change 3], [What behaves differently].
- Partner: [Partner organization], [Idea in a few words], [How you know of them], [The proposal], [Proposed times].
- Meeting: [Meeting name], [Meeting date], [Decision], [Owner], [Action], [Due date], [Open question].
- Bug or data issue: [The problem], [Who is looking], [What to do meanwhile], [One ask], [Reply-by date].
- Talks: [Talk date], [live or staged], [Participant count], [One sentence on the state of the program today], [The biggest change in the release, as a sentence], [One sentence on which data types grew], [The next milestone and when], [One line the audience should remember], [One sentence on what the program is, from programs/]. (Removed 2026-10-21 with talks/.)

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

deck-template.md was removed 2026-11-04. build_deck_template.py and its deck were removed 2026-11-04 when the PowerPoint format replaced them (see PowerPoint format below).

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

docx-templates.md was removed 2026-11-04. build_docx_templates.py and the memo and one-pager templates were removed 2026-11-04, replaced by scripts/build_word.py (see Word format, 2026-11-04).

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

The menu and tasks/ were removed 2026-11-04 (see Two services below). The lines in this section are kept as history.

- The menu is a bullet list, no numbers, as the ticket asks. Each line reads "- Option (tasks/page.md): description" so the agent sees which page to open and check.py can tie each option to its page.
- Option names follow the ticket wording with a capital first letter: Draft an email, Build a slide deck, Write a memo or one-pager, Create an SOP, Answer a question about the data files, Answer a question about a program, Review a draft against the house style. (Replaced 2026-10-21 by the six option menu below.)
- Descriptions say what the person gets back, not how the agent works, in one line each.
- The README section ends with one line for requests that fit no option, matching the How to start rule in AGENTS.md.
- AGENTS.md keeps its old opening line ("Read this first. Then read the folder your task touches.") after the new section, since the ticket allows no other change there.
- Paths under Read first are from the handbook root. The built pptx and docx are named in Steps, not Read first, because on the board they live on the data root; in the GitHub repo they sit in design/templates/.
- Menu files and tasks/ pages are checked against the AGENTS.md banned list; AGENTS.md itself is not, since it holds the list.
- tasks/create-sop.md is a one-line placeholder until the SOP kit ticket writes it.

## SOP kit, 2026-10-20

sop-template.md and tasks/create-sop.md were removed 2026-11-04. The house SOP template docx is published in assets/; the worked example stays on the data root and is no longer published (design/templates/ removed from the GitHub repo 2026-11-04).

Inputs: the house SOP template, AALS-SOP-005-V1 (docx and pdf) and ALSTDI-SOP-001-V1, dropped by the operator. Only headings, tables and page setup were read with python-docx; no body text was copied into the handbook.

Choices:

- The template is shipped byte for byte as the team uses it, not rebuilt from tokens.json like the memo and deck. It keeps its own look (Calibri, black headings).
- The template has no paragraph in the Heading 2 style. Its five section names and its two "Heading 2" step lines are Normal paragraphs with automatic numbers. sop-template.md says to fill those in place and never to apply the Heading 2 style; a test fill with python-docx kept every number. check.py reads both kinds of heading from the template.
- Step numbers under Procedures are fixed as 4.n in the template's numbering, so the page says to keep all five sections in order.
- The house rules are the ones the finished SOPs follow. The 700 to 1,000 word budget is the ALS TDI SOP's; the older Answer ALS SOPs are shorter (005 and 006 are about 350 words). The page says not to pad a short process.
- The step shape (Inputs, Steps, Outputs, Checks) is named as ALS TDI SOP-001 uses it, as a pattern, not a rule.
- Neuromine is named as a program with the NEUROMINE- prefix because a finished SOP uses it, though it has no programs/ page. (programs/ removed 2026-10-21.)

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

- programs/answer-als.md, Where things live: the two lines naming the release storage account and its container, and the portal storage account and its container, became one line saying release files and documents are reached through the portal and the README links, without naming storage. (Removed 2026-10-21 with programs/.)
- design/templates/deck-template.md, docx-templates.md and sop-template.md, Files line: the absolute data root paths for both devices and the board device name became "under the data root at answer-als/agent-handbook/v1/templates/", plus where the files sit in the GitHub repo. (Removed 2026-11-04.)
- design/tokens.json, source: the absolute path of the Variant Tool checkout became "Variant Tool docs/design/tokens.css".
- communication/email/data-question-reply.md: the cell line vendor link (a link registry host) became the vendor named, with its catalog named, not linked. (Removed 2026-11-04.)
- schemas/index-answer-als-r8.md, has_discordant_sample: the lab named after a person became "MIT".
- NOTES.md: two ticket ids, one absolute path, the board device name and the vendor host removed; the Storage and repo lines now say the repo is public.
- SOP template copy (answer-als-sop-template.docx): file author changed from a staff name to "Answer ALS data team". Paragraph text had no name.
- SOP example copy (AALS-SOP-005-V1 docx): the staff name on the Last Modified By line became "Answer ALS data team"; file author and last modified by became "Answer ALS data team"; the example SubjectUID became NEUxxxxxxxx in both places (the given value and the CASE- value), matching the CASE-NEUxxx form the same SOP uses later.
- SOP example copy (AALS-SOP-005-V1 pdf): the same name and example SubjectUID replaced in the page text; the pdf author field set to "Answer ALS data team".

## Lou mirror, 2026-10-21

lou/ holds a copy of Lou's knowledge base pages, so program facts can come from Lou's own pages and nothing is synced by hand. Lou's pages also sit in a blob storage folder, but that folder cannot be opened to anonymous read: Azure sets anonymous read per container, never per folder, and the container also holds private data. So the GitHub Action .github/workflows/lou-mirror.yml copies the pages from the data-scripts repo instead.

- Access is a read-only deploy key on the data-scripts repo, titled "agent-handbook lou mirror (read only)". Its private half is held only as the Actions secret LOU_SOURCE_KEY in this repo. It cannot push to data-scripts.
- The Action runs daily and on demand. It copies every .md file under Lou/lou-data/ in data-scripts into lou/, keeping the subfolder names, and writes lou/INDEX.md with one raw URL per page. Other file types are not copied.
- Links to the portal's backend host are rewritten to data.answerals.org, and links to files in blob storage become "(document on the portal)". Every other byte is as Lou has it. A guard then fails the run if a storage name, backend host or SAS signature is still in a page.
- It commits only when a page changed. If the data-scripts checkout fails, lou/ is not touched and the last good copy stays.
- lou/ and lou/INDEX.md are never edited by hand and are not kept on the board. Change a page in data-scripts and the next run picks it up.

## Data domain, 2026-10-21

schemas/ became data/ (git mv, the eight pages kept) and gained a glossary, the two clinical dictionaries in full, naming conventions and validation checks. Inputs: the Answer ALS clinical dictionary CSV and the ALS TDI data dictionary xlsx (dictionary rows only), the Answer ALS data submission and naming SOP, the SOP masters (Definitions sections), the Index Validation notes, the release file names in the index schema folders, and the check scripts and validation reports of both cohorts (what is compared and the pass rule only). No data row was read and no count or value from a data file was copied.

Choices:

- Lift-out clean: nothing under data/ links to design/, communication/ or tasks/, names a drive or volume path, a ticket id, the board, a topic folder or a brain row. The old pages had "on the board", topic notes and a brain row in their Source lines; those were reworded to name the file or the decision only. The privacy line no longer points at programs/; it says published release-level counts come from the release notes.
- data/README.md lists every file in data/ by its raw GitHub URL on main, the build script included. The overview, identifiers and join keys from the old README are kept below the list.
- Dictionary pages are generated by data/build_dictionaries.py, never edited by hand. Each form gets a table of Field name, Label, Type and Coded values. Label is New Field Label for Answer ALS and Additional Notes for ALS TDI (the ALS TDI dictionary has no label column). Forms keep dictionary order, fields keep row order.
- The Answer ALS dictionary passes 1,000 lines on one page, so it is split into three form groups: clinical assessments, diagnosis history and demographics, events logs labs and samples. dictionary-answer-als.md is then the list of forms with each one's field count and part page. The ALS TDI page fits on one page. A form not named in a group lands in an "other" part, so a new form is never dropped.
- Text is made ASCII: curly quotes and dashes become plain ones, the multiplication sign becomes x, the greater-or-equal sign becomes >=. A pipe inside a cell is escaped as \| so a table stays intact; the codes read the same in a rendered page.
- Two dictionary texts conflict with the page rules, so the builder rewrites them and the page header says so: a # sign right before a number (the FVC and SVC trial labels) becomes the word number, since # and digits read as a ticket id; a web link becomes "(web link in the dictionary file)", since the public-repo guard blocks hosts from the link registry (the ALS TDI voice score row links a PubMed Central article).
- With no arguments the builder finds the dictionaries on the data root through board_check; in a lifted copy, pass --answer-als and --als-tdi. It writes ASCII with LF line ends, so two runs give the same bytes on any device.
- check.py reads the dictionaries itself (not through the builder) to count rows per form, then compares with the table rows on the pages and the counts on the cohort page, and rebuilds the pages into a temp folder to compare bytes.
- naming.md writes the Neuromine SOP prefix in words, because the prefix in capitals matches the identifier guard pattern NEU followed by six capitals. Omics paths are given as patterns with <Participant_ID>, never with the example identifiers the naming SOP uses.
- validation.md gives no numbers from a data file. Rule parameters stay in words (a one or two day shift, the Healthy Control code).

Found and not found:

- The naming SOP never names Answer ALS OMOP release files; naming.md says that is not settled.
- No written pass rule was found for the Answer ALS sample mapping or for a delivery of Answer ALS omics files; validation.md covers the ALS TDI sample mapping and the splicing release only.
- The Index Validation notes list cross-column rules for the Answer ALS index without saying which script runs them; validation.md lists them as release checks on the index.
- The answer-als and als-tdi decisions give no glossary definition for "sub-release" or "bundle"; both are written from how the decisions use them.

## Handbook rework, 2026-10-21

The menu, tasks/, communication/ and the README Full index from this section were removed 2026-11-04 (see Two services below).

The handbook is trimmed to four things: SOPs, user emails, agent instructions and output practice, and the data domain. Agents cannot browse GitHub folders, so every page is fetched by raw URL. Program facts now come from the mirrored Lou pages in lou/. The operator approved the trim on 2026-10-21.

- Removed: programs/answer-als.md, programs/als-tdi.md, tasks/program-question.md, tasks/data-question.md and communication/talks/ (both outlines). Older lines above that name them are marked removed.
- AGENTS.md is short: How to start, Where facts come from, How to write, Privacy, Templates, What not to do. The who-we-are text and the old "Read this first" line are gone. Counts may be repeated only when quoted from a Lou page.
- The menu has six options: Draft an email, Create an SOP, Answer a question, Build a slide deck, Write a memo or one-pager, Review a draft against the house style. Each menu line links its task page by raw URL, so the agent can fetch it.
- tasks/answer-question.md replaces the two question pages. Program, access, DUA, download, FAQ and contact questions go to the lou/ page that fits; column, form, file, naming and validation questions go to data/.
- Every Read first entry is a raw URL. lou/INDEX.md is linked though it exists on GitHub only. The built templates are fetched in Steps, not Read first, because they are not on the board.
- Every task page has a Steps line saying to use the template as it is and not restyle it. AGENTS.md says templates are never restyled or rebuilt, so the task pages no longer tell an agent to run a build script.
- README.md Full index lists every file in the GitHub repo by raw URL, one per line, grouped by folder, with lou/INDEX.md as the one entry for lou/. It includes the files that exist on GitHub only (the built templates, the cleaned SOP copies, CHANGELOG.md and .gitignore). Spaces in a file name are written %20.
- CLAUDE.md is one line pointing at AGENTS.md, for agents that read CLAUDE.md first.

## Two services, 2026-11-04

The operator decided on 2026-11-04 that the handbook serves two things only: the design (branding) and the rules for agents working on the Neuromine data set. The rest was never used.

- Removed: communication/ (README.md and the eight email templates), tasks/ (README.md and the six task pages), design/templates/sop-template.md, deck-template.md and docx-templates.md, the README menu and the README Full index.
- Kept: design/ (with build_deck_template.py and build_docx_templates.py until the design skill replaces them), data/, the SOP template docx and the worked example on the data root, .github/ and the Lou mirror.
- AGENTS.md has two sections only: Design, then Neuromine data rules (where facts come from, privacy, how to write with the banned word list, what not to do). The Design section points at design/README.md by raw URL until the design skill's SKILL.md lands.
- README.md is one intro line, the line to paste, and two short sections, Design and Neuromine data, each naming its entry page by raw URL.
- CLAUDE.md is unchanged.
- TEST.md still records the 2026-10-21 run against the old menu; a later rewrite replaces it.

## Design skill, 2026-11-04

The design service now works as an Agent Skill. An agent fetches SKILL.md, reads references/brand.md, reads the one format file, starts from the matching template in assets/ and runs the checker.

- SKILL.md at the root: frontmatter name answer-als-document-skill and a description, What it covers and How to use it. Every link is a raw URL under main. The format files word.md, powerpoint.md, excel.md and html.md are listed as coming; each lands with its template and checker.
- references/brand.md holds the brand rules in thirteen sections: Palette, Typography, Headings, Body text, Tables, Header and footer, Cover page, Callouts, Lists, Charts, Page setup, Dates, Writing. design/README.md is now a pointer to it. What moved and what was added is in design/DECISIONS.md.
- Charts gained a Sequential and a Diverging series built from the brand blue steps and the error reds; tokens.json has them as chart_seq_1 to 6 and chart_div_1 to 6.
- scripts/prose.py: find_banned(text) returns (word, snippet) pairs for the em dash, en dash and the banned words and phrases in brand.md. The banned list in brand.md is written in inline code so the page can name the words; the board check skips inline code.
- scripts/check_all.py runs every scripts/check_<ext>.py against assets/*sample*.<ext> and exits 0 when all pass or skip. With no checkers yet it prints SKIP and exits 0.
- AGENTS.md Design and README.md Design now point at SKILL.md. The line above that says AGENTS.md points at design/README.md is out of date.

## Word format, 2026-11-04

The design skill has its Word format, in the shape of the DWD document skill: references/word.md, scripts/build_word.py (builds the template and a sample), scripts/check_docx.py and assets/README.md.

- references/word.md has the DWD sections (Start from the template, Starter, Styles, Fonts, Page setup, Header and footer, Cover page recipe, Table recipe, Callout recipe, Lists, Charts, Voice, Checklist before sending) plus SOPs, with the Answer ALS values from brand.md and tokens.json. No DWD name, color or font.
- Styles: Title 20pt bold brand blue; Subtitle 14pt Text 2; Cover Eyebrow and Cover Date, Caption, Header and Footer in Courier New 9pt; Heading 1 14pt Ink, Heading 2 11pt Ink, Heading 3 11pt Text 2, all bold Helvetica Neue; Normal 11pt Text. brand.md names only two heading levels below the title, so Heading 3 takes Text 2 to read apart from Heading 2 at the same size. Only the sizes 20, 14, 11 and 9 are used.
- Body font, size and color sit in docDefaults and Normal is empty, so the Answer ALS Table style's Text 2 cell color is not overridden by Normal in Word.
- The cover band is one PNG (brand blue, 8.5 by 2.75 in, the logo pasted at 0.75 in high, 1 in from the left edge and 0.5 in from the top) anchored behind the text at the page corner in the first-page header. The logo appears nowhere else. On a white cover the eyebrow reads Answer ALS and there is no logo.
- Header: "Answer ALS" as plain text, a tab, STYLEREF Heading 1. brand.md has no header mark, so the DWD filled mark style was dropped; check_docx.py has no mark exemption.
- Tables put the Caption under the table, as the DWD skill does and the checker expects; brand.md says above for other formats, and word.md says the format file wins.
- Table header text is Ink on the light #F4F6FB fill, not Automatic: the DWD Automatic rule is for a dark fill.
- check_docx.py also fails when the first Heading 1 has no page break before. Prose hits use scripts/prose.py; table cells with no letter are skipped as data.
- The chart uses Arial in matplotlib (Helvetica Neue is not on Windows). Builds are byte stable on one device; a MacBook rebuild may differ in the chart bytes if its Arial or matplotlib differs, in which case check.py fails the sha256 match and the files must be rebuilt and REPORT.md updated there.
- build_word.py writes to <data root>/answer-als/agent-handbook/v1/assets/ when the board's board_check.py is three folders up, else to assets/ beside scripts/ (the public repo case); an output folder can be given as the only argument.
- scripts/check_all.py takes an optional folder; check.py runs it on the data root assets. A missing folder prints SKIP.
- The memo and one-pager templates were deleted from the data root templates/ folder. The SOP template stays as is; on GitHub it moves from design/templates/ to assets/. The deck and the worked SOP example stay in design/templates/ until the PowerPoint format lands.
- Not checked by eye: nobody opened the built files in Word on this ticket (no window may open). The operator should open answer-als-sample.docx and confirm the band and logo sit at the top of page 1, the header and footer show from page 2, and the table and chart look right.

## PowerPoint format, 2026-11-04

The design skill has its PowerPoint format, in the shape of the DWD document skill: references/powerpoint.md, scripts/aals_pptx.py (the helpers), scripts/build_powerpoint.py (builds the template and a sample) and scripts/check_deck.py. It replaces the 2026-10-20 deck template and build_deck_template.py.

- Eight layouts: Title, Section, Title and Content, Two Content, Table, Chart, Picture, Closing. The DWD set plus Table, with its caption above the table as brand.md says.
- Title and Closing are brand blue layouts with the white logo at 0.75 in from the top and left edges, 0.75 in high, the eyebrow (a placeholder, idx 15, for the program and event), a Tint 3 bar, the white 54pt headline and the Tint 3 22pt subline, the look of the old deck's title slide. The logo is a picture on these two layouts only; check.py fails if any other part of the file refers to it.
- Content layouts are white with the 0.18 in brand blue strip, the headline 40pt bold in brand blue (brand.md Headings) and the footer: the deck name at left and the slide number at right, both Courier New 12pt, below a Rule line. brand.md says a content slide footer is the page number only; the DWD check list asks for the footer too, so powerpoint.md wins for PowerPoint.
- Only the six slide sizes in brand.md are used: 22pt body level 1 and section text, 16pt level 2, tables and chart labels, 14pt eyebrow and captions, 12pt footer and page number.
- The theme names Helvetica Neue for headings and body; Arial is the fallback a reader without it sees. Courier New is set by name for the footer, page number and date.
- The callout is the brand.md callout: a Tint 1 box with a 3pt brand blue bar at its left edge. Bullets are round and brand blue at both levels.
- The python-pptx default theme and notes theme carry gradient fills and shadows in their format scheme; the build replaces them with flat fills and empty effect lists, and check_deck.py and check.py fail on any gradient or shadow.
- The template holds one guide slide per layout, each slide's text and notes its own instruction; powerpoint.md Starter drops them before adding slides. The sample is about building a deck with the skill, so every number in it comes from brand.md, not from a release.
- Builds are byte stable (fixed core dates, fixed zip times, the embedded chart workbook rewritten the same way, the matplotlib picture saved without a Software tag). A MacBook rebuild may differ in the picture bytes if its Arial or matplotlib differs; rebuild there and update REPORT.md.
- scripts/check_all.py maps check_deck.py to *sample*.pptx.
- Not checked by eye: nobody opened the built files in PowerPoint on this ticket (no window may open). The operator should open answer-als-sample.pptx and confirm the logo and text sit clear on the two blue slides, nothing runs off a slide, and the table, chart and picture look right.

## Markdown and HTML formats, 2026-11-04

The design skill has its two text formats, in the shape of the DWD document skill: references/markdown.md and references/html.md, a hand-written sample of each in assets/ (answer-als-sample.md with answer-als-sample-figure-1.png, and answer-als-report.html), scripts/check_md.py, scripts/check_html.py and scripts/build_markdown_figure.py. No binaries are built; the samples and the PNG are committed.

- Markdown: line 1 eyebrow `ANSWER ALS` in inline code, the title H1 on line 3, the italic subtitle and date on line 5. Everything else is the DWD rule set with the Answer ALS chart colors and a source line under each figure, as brand.md asks.
- The Markdown figure has the same name as the Word sample chart. build_markdown_figure.py calls figure_png in build_word.py (split out of build_sample, no change in output), so both are the same bytes and one file serves both samples on GitHub. PUBLISH.md now copies it from the repo.
- HTML: no link element at all. The DWD Google Fonts exception is gone; the stacks are "Helvetica Neue", Arial, sans-serif and "Courier New", monospace. Colors in :root are the brand.md values; check_html.py reads the brand hex list from design/tokens.json instead of a hardcoded list.
- HTML follows brand.md where DWD differs: no rule under h1; h1 28px brand blue, h2 15px and h3 14px Ink, weight 600; body 14px at line height 1.6; table head on the light #F4F6FB fill with Ink text, 6px radius; callout with Tint 1 fill and 8px radius; round brand blue bullets; quotes with no italics; @page margin 1in and the page number in Courier New 9pt Placeholder.
- The header mark is `<span class="mark">Answer ALS</span>` in plain Courier New Caption text, not a filled block, the same choice word.md made. The cover has a brand blue band with the white logo as a data URI, the only place the logo appears.
- check_html.py builds its Windows browser fallback from SYSTEMDRIVE (or C:) so the file holds no absolute path for the public-repo guard.
- check_all.py maps check_html.py to *report*.html (the HTML template and sample are one file) and now shows a checker's SKIP lines, such as print-render, under its PASS line.
- The md sample links to an unnumbered H3 fragment: a fragment like a numbered H2 slug trips the public-repo guard's ticket id rule.
- Print check: headless Chrome printed the report to 7 pages: the cover alone on page 1, each of the five sections on a new page, the 26 row table over two pages with its header repeated, page numbers from page 2. Nobody looked at it by eye.

## Excel format, 2026-11-04

The design skill has its Excel format, in the shape of the DWD document skill: references/excel.md, scripts/aals_excel.py (the helpers, the DWD signatures), scripts/build_excel.py (builds the template and a sample) and scripts/check_xlsx.py. The two built workbooks live on the data root and go to GitHub as assets/answer-als-template.xlsx and assets/answer-als-sample.xlsx.

- Named styles: the seventeen sheet styles Answer ALS Title, Subtitle, Eyebrow, Date, Table Title, Header, Text, Text Wrap, Integer, Decimal, Percent, Total Label, Total Integer, Total Decimal, Total Percent, Caption and Note, plus Answer ALS Date Cell for a date column, kept from the DWD set so dates in a table still have a style. check_xlsx.py requires all eighteen.
- Answer ALS Note is the source line: Helvetica Neue 9pt Caption color, on the row under a table caption or a figure caption ("Source: ..."), as brand.md asks for a source line under every chart. Captions are Courier New 9pt, as in Word.
- The header row is brand blue #1F4FAE with fixed bold white text, not the light #F4F6FB head of brand.md and not the DWD Automatic font color. White on brand blue reads in Excel, LibreOffice and Google Sheets alike, so the DWD dark mode reason for Automatic does not apply. check_xlsx.py fails any other fill or text color.
- Body cells are Text 2 #374151 with a #DFE3EB rule below; totals are Ink bold with a Border #8A9097 rule above (a rule a reader must see, per brand.md Contrast). Table title is Ink bold 11pt. The eyebrow reads ANSWER ALS, the print header Answer ALS. No logo in a workbook.
- Sizes are the document sizes only: 20 title, 14 subtitle, 11 body and table, 9 eyebrow, date, caption, source line, print header and footer.
- Charts: categorical chart_1 to chart_6 by default (they are also the theme accents), single brand blue for one series (a categorical chart with one series switches to it), sequential and diverging from tokens.json. Axis line and gridlines #D9E1EA, axis text #6A7683, legend at the top with overlay off. check.py fails if the aals_excel.py palettes differ from tokens.json.
- Fonts name Helvetica Neue with the Swiss family, so Windows Excel shows Arial; Excel has no fallback list. The theme font scheme is Helvetica Neue too.
- save writes each formula's computed value as its cached value (the DWD fix for Protected View blanks) and sets fullCalcOnLoad. The sample has 10 formula cells, all cached; check.py checks each one with data_only.
- Builds are byte stable: fixed core dates and zip times. The sample numbers are made up and say so on every sheet.
- scripts/check_all.py with no argument now looks in the data root assets folder for a sample not in assets/, so the docx, pptx and xlsx samples are checked there instead of skipped.
- The public clone's .gitignore lists *.xlsx, so PUBLISH.md step 5 adds the two workbooks with git add -f by name.
- Not checked by eye: nobody opened the workbooks in Excel on this ticket (no window may open). The operator should open answer-als-sample.xlsx from Downloads, confirm Protected View shows the numbers and both charts, the header row reads white on blue, and the charts sit between the source lines without covering them.

## Republish, 2026-11-04

The two-service handbook and the design skill went to GitHub in one push. communication/, tasks/ and design/templates/ were deleted there, whole. The SOP template moved to assets/; the worked SOP example is not published any more, since no page points at it. lou/, CHANGELOG.md (one new line) and .gitignore were kept.

## Design skill moved, 2026-11-04

The design skill left this repo. It is now the Neuromine brand skill in its own public repo, https://github.com/Neuromine-Data/brand-skill, and agents fetch https://raw.githubusercontent.com/Neuromine-Data/brand-skill/main/SKILL.md for every document, deck, sheet, page, SOP or figure. SKILL.md, references/, scripts/, assets/ and design/ (the logo included) are gone from this repo, here and on GitHub. There is no second copy. This repo now serves the Neuromine data rules only: AGENTS.md, data/ and lou/.

The Word, PowerPoint, Excel, Markdown, HTML, SOP and public-copy lines above are history. They describe the design skill as it was in this repo, not how it works now. The brand skill repo has its own notes.
