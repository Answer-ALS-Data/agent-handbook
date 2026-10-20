# Design decisions

Where each part of the look came from, and what was left out. Read 2026-10-20 from the Neuromine Variant Report tool (docs/design/tokens.css, STYLE.md, HANDOFF.md, INVENTORY.md, variant_reports.py) and the talk deck (talks/github-for-researchers/theme.json, build_deck.py).

## Taken

| What | From | Note |
|---|---|---|
| Brand blue, dark and light steps, three tints | tokens.css | Same hex values. The header background in variant_reports.py is the same brand blue. |
| Ink and text steps, placeholder, muted | tokens.css | With the contrast rules of STYLE.md 1a. |
| Surfaces, borders, table colors | tokens.css | Border is the darkened value from STYLE.md 1a. |
| Status colors | tokens.css | Backgrounds made flat: the gradient end color is kept. |
| Six categorical chart colors | tokens.css cohort colors | In the same order. |
| Chart axis and grid colors | tokens.css analytics axis and grid | Axis is the darkened value from STYLE.md 1a. |
| Web size scale, weights, line height, eyebrow tracking | tokens.css | Unchanged. |
| Spacing scale, radii, shadows, control heights | tokens.css | Shadows are web only. |
| Eyebrow, card, table, action bar, status box patterns | tokens.css and STYLE.md | Described in words, not as CSS. |
| Sentence case, nouns for labels, plain error text | STYLE.md section 4 and INVENTORY.md | Folded into Voice on a page. |
| Fonts: Helvetica Neue, Arial fallback, Courier New mono | talks/CONTEXT.md and theme.json | One family for every output instead of the web system stack. |
| Slide sizes, title slide and content slide patterns | build_deck.py | Same sizes and positions. |
| White logo, its URL, header logo height | variant_reports.py and talks/reference/ | Logo used only on brand blue. |

## Left out

| What | Why |
|---|---|
| pmui, _BRAND_THEME and FastListTemplate notes | They describe one web app's code, not the look. |
| Tabulator CSS and shadow DOM rules | Web widget code; no other output needs it. |
| Mode tabs, skeleton loader, preview bar, header navigation, responsive breakpoints | Web-only widget rules for that tool. |
| Accessible names, focus rings, icon controls (STYLE.md 5a, 5b) | Rules for interactive widgets; the handbook makes documents and static pages. |
| Gradients on buttons and status boxes | The brand here is flat with no decoration. |
| Roboto header font and the system font stack | Not on every device; the talks topic settled on Helvetica Neue with Arial. |
| RNA-seq teal, missense and upstream colors, admin analytics text colors | Specific to that tool's views. |
| Genotype chips (STYLE.md 3) | That tool's signature element, not a program-wide pattern. |
| HANDOFF.md | Delivery history for one page; nothing about the look. |
| Transition timing | Web animation only. |

## Added here

| What | Why |
|---|---|
| Document size scale in pt (9, 11, 14, 20) | Memos and PDFs need a print scale and neither source had one. Chosen as plain print sizes. |
| Logo clear space and minimum slide size | Neither source wrote a rule. Half the logo height and 0.5in are the plainest safe values. |
| Square corners on slides and documents | The deck already uses square shapes. |
