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

## Design skill, 2026-11-04

The handbook now has a design skill in the Agent Skills shape: SKILL.md at the root, references/brand.md, scripts/prose.py and scripts/check_all.py. An agent reads brand.md, then the one format file, starts from the matching template and runs the checker. The format files, templates and checkers come one format at a time.

### Moved

| What | From | To |
|---|---|---|
| Palette, contrast rules, type families, sizes, weights, casing | design/README.md Color and Type | references/brand.md Palette and Typography |
| Table, title slide, content slide and status box patterns | design/README.md Layout patterns | references/brand.md Tables, Cover page, Callouts, Page setup |
| Chart rules and the six chart colors | design/README.md Charts | references/brand.md Charts |
| Logo rules | design/README.md Logo | references/brand.md Cover page |
| Voice on a page | design/README.md | references/brand.md Writing |
| The how-to-write rules | AGENTS.md How to write | references/brand.md Writing (AGENTS.md keeps its copy) |

design/README.md is now a short pointer. tokens.json stays and holds every color in brand.md.

### Added

| What | Why |
|---|---|
| Sequential chart series: #EEF4FF, #DCE8FF, #C4D9FF, #4070D9, #1F4FAE, #163D8C (tokens chart_seq_1 to 6) | Ordered data needs one hue light to dark. Built from the brand blue tints and steps, so no new color. |
| Diverging chart series: #163D8C, #1F4FAE, #C4D9FF, #F8D7DA, #DC3545, #721C24 (tokens chart_div_1 to 6) | Data above and below a midpoint needs two hues. Brand blue against the error reds, light in the middle; blue and red stay apart for most color vision types. It is the one chart use of a status color. |
| Courier New for labels and page furniture (header and footer text, page numbers) | The skill shape gives page furniture a mono face. Courier New was already the brand mono. |
| Header and footer: program name in text at left, section at right, page number at right in the footer | There is no dark logo, so white pages carry the name in text. |
| Document cover: brand blue band at the top with the white logo | The logo may sit only on brand blue; the band gives it a place on a white page. |
| Callout: Tint 1 fill with a 3px brand blue left border | Matches the flat look and keeps status boxes for status only. |
| Headings: title in Brand, H2 and H3 in Ink, no rules under headings | Matches the Word templates (brand blue title) and the Ink heading color. |
| Dates: 3 November 2026, November 2026 on a cover, 2026-11-03 in a file name | Neither source had a date rule. |
| Voice options (plain first person, neutral third person, formal) and the extra banned patterns | Shared writing rules from the skill shape, with Answer ALS examples. |
