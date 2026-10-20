# Design

How Answer ALS things look. Use it for every deck, memo, chart and page, so they read as one program. tokens.json holds the same values for code. Add no colors, fonts or sizes that are not here.

## Brand in one paragraph

Quiet and clinical. Brand blue on white, dark ink for text, thin grey rules, plenty of space. One strong element per page: a headline, a number or a chart. No decoration: no gradients, clip art, stock photos or ornamental icons, no color for its own sake. If a page looks plain, it is right.

## Color

Brand blue

- Brand #1F4FAE: headlines on slides, card titles, links, the eyebrow on white, the single series in a chart, the background behind the logo.
- Brand dark #163D8C: text or a command line set in blue on a white slide, pressed buttons.
- Brand light #4070D9: hover state on a web page only. Never for text.

Tints, for fills behind content

- Tint 1 #EEF4FF: lightest fill, for a placeholder box or a highlighted panel.
- Tint 2 #DCE8FF: hover fill.
- Tint 3 #C4D9FF: selected fill, and the eyebrow, rule and subline on a brand blue slide.

Ink and text

- Ink #1A2332: headings.
- Text #2C3E50: body copy.
- Text 2 #374151: secondary text and table cells.
- Caption #4B5563: captions, eyebrows, source lines.
- Placeholder #6E7581: muted text that still has to be read (placeholders, "no data" cells, page numbers).
- Muted #9CA3AF: disabled or decorative marks only. Never for text a reader needs.

Surfaces and rules

- Page #F8F9FA: page background behind cards.
- Surface #FFFFFF: cards, slides, table body, documents.
- Border #8A9097: borders that must be seen (inputs, card edges, dividers that separate content).
- Rule #E5E7EB: light dividers and the frame around a screenshot.
- Table border #DFE3EB, table head #F4F6FB, row hover #EEF3FB.

Status. Each has a strong color, a flat background and a text color for the box.

- Error #DC3545, background #F8D7DA, text #721C24.
- Success #28A745, background #D4EDDA, text #155724.
- Info #1F4FAE (brand), background #D1ECF1, text #0C5460.
- Warning #B45309, used as text color for an inline warning.
- Required #E02424: the asterisk on a required field.

Status colors mean status only, never chart series or decoration.

Chart colors, in this order: #008300, #E87BA4, #4A3AA7, #1BAF7A, #EDA100, #882255. See Charts.

Contrast rules

- Text must reach 4.5:1 against its background. Every text color above passes on white and on Page.
- A border or chart line a reader must see must reach 3:1. Use Border #8A9097 for these, not Rule #E5E7EB.
- Muted #9CA3AF (2.5:1) is only for disabled or decorative things. For any muted text a person must read, use Placeholder #6E7581.
- Chart axis text uses #6A7683, which passes 4.5:1.
- Chart colors are for marks (bars, points, lines), not text. Several of them fail 4.5:1 as text.
- On brand blue, use only white or Tint 3 for text.

## Type

Families

- Headings and body: Helvetica Neue, falling back to Arial, then sans-serif. On the web: "Helvetica Neue", Arial, sans-serif.
- Code, commands and file names: Courier New, falling back to monospace.

Sizes on a web page (px)

- 11: eyebrow label.
- 12: chips, counters, small table notes.
- 13: buttons, helper lines, captions.
- 14: body copy, inputs, status boxes, table cells.
- 15: card and panel titles.
- 28: the one page heading.

Sizes on a slide (pt, 16:9 at 13.333 by 7.5 in)

- 12: page number.
- 14: eyebrow.
- 16: command line, chart labels.
- 22: subline on a title slide.
- 40: content slide headline.
- 54: title slide headline.

Sizes in a document such as a memo or PDF (pt)

- 9: eyebrow, caption, source line.
- 11: body copy and table cells.
- 14: section heading.
- 20: document title.

Weights: 400 for body, 500 for button labels, 600 for headings and card titles, 700 for the eyebrow and slide headlines. Line height 1.6 for body copy.

Casing: sentence case everywhere: headlines, titles, buttons, table headers, axis labels. No all-caps, except the small eyebrow label, which is uppercase with a little letter spacing (0.3px on the web, 2pt on a slide). Program names keep their own casing: Answer ALS, ALS TDI, Neuromine.

## Spacing and shape

Spacing scale (px): 4, 6, 8, 12, 14, 16, 20, 24, and no other steps. 6 under an eyebrow, 14 between blocks in a card, 24 between sections.

Radius (px): 4 for buttons, 6 for inputs and tables, 8 for cards and status boxes, 10 for dialogs, 12 for chips. Slides and documents use square corners.

Shadows, web only and always soft and blue tinted:

- Card: 0 2px 8px rgba(31, 79, 174, 0.08).
- Card on hover: 0 4px 12px rgba(31, 79, 174, 0.12).
- Button: 0 2px 6px rgba(31, 79, 174, 0.25).
- Dialog: 0 12px 32px rgba(0, 0, 0, 0.2).

No shadows on slides, documents or charts.

Density: compact. Form controls and primary buttons are 42px high, action bar buttons 36px, table rows 24px, table headers 34px. Status boxes pad 14px top and bottom, 16px left and right.

## Layout patterns

Eyebrow plus headline. A small uppercase eyebrow names the section or topic, then one headline says the point. On white the eyebrow is Caption or Brand; on brand blue it is Tint 3. A short bar under the eyebrow is allowed on slides.

Cards. White surface, 8px radius, card shadow on the web, a 15px semibold title in Brand, 14 to 16px inside padding. One topic per card.

Tables. Table head #F4F6FB with a #D8DCE5 rule under it, outer border #DFE3EB, 6px radius on the web. Headers are plain words, never raw column names or snake_case. Numbers are right aligned, text left aligned. Use the same header for the same column everywhere.

Action bar. One row above the result: "start over" on the left as a plain button, the main action (such as Download) on the right as the only blue button in the view.

Status boxes. Full width, 8px radius, status background and text color, 14px body. Say what happened and how to fix it.

Title slide. Brand blue background, white logo top left at 0.75in high, eyebrow in Tint 3 to its right, a short Tint 3 bar, headline in white at 54pt, subline in Tint 3 at 22pt. The closing slide uses the same pattern.

Content slide. White background with a brand blue strip 0.18in wide down the left edge. Left half: eyebrow in Brand at 14pt, short brand bar, headline in Ink at 40pt, an optional command line in Courier New Brand dark. Right half: one screenshot or chart framed with a thin Rule line. Page number bottom right in Placeholder at 12pt.

## Charts

- Many categories: use the chart colors in order, #008300, #E87BA4, #4A3AA7, #1BAF7A, #EDA100, #882255. Keep a category on the same color across every chart in a set.
- More than six categories: group the small ones into "Other" or split the chart. No seventh color.
- One series: Brand #1F4FAE for every mark.
- Axis text and tick labels: #6A7683. Grid lines and baseline: #D9E1EA. Keep grid lines few and light.
- No 3D, no shadows, no gradients or patterns in data marks.
- Label every axis in sentence case with its unit.
- Put a source line under every chart in Caption at caption size: "Source: Answer ALS Release 7 index" or similar. Name the release.

## Logo

The logo is assets/answer-als-logo-light.png, the white Answer ALS mark. The web copy is https://dataportal.answerals.org/logo_light.png.

- Use it only on brand blue #1F4FAE. Never on white, a tint, a photo or any other color, where it disappears.
- Keep clear space of at least half the logo's height on every side.
- Never stretch, squash, recolor, rotate, crop or add a shadow. Scale it with its sides locked.
- Smallest size: 38px high on a screen, 0.5in on a slide.
- Top left on a title or closing slide or in a page header, once per page.

There is no dark logo. On a white page, write the program name in text instead.

## Voice on a page

The rules in AGENTS.md apply to every word on a page. In addition:

- A headline states the point in one short sentence, not a topic. "Release 8 adds cell line fields" beats "Cell lines".
- An eyebrow is two to four words naming the topic.
- A caption says what the reader is looking at and where it came from. One sentence.
- Labels are nouns: Participants, Genes, Release.
- Buttons are verbs: Download, New report.
