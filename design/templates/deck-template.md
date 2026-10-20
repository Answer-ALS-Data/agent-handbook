# Deck template

The standard Answer ALS deck. Start every talk and program update from it so they all look like the same program.

File: answer-als-deck-template.pptx, 16:9, ten slides, one per layout. In the GitHub repo it is in design/templates/. On the board it is built under the data root at answer-als/agent-handbook/v1/templates/, not in the board repo.

The text on each slide says what goes there and how many words fit. The speaker notes on each slide hold the rule for that layout. So the file is its own guide.

## Use it

1. Copy the file and rename the copy for your talk. Never edit the template itself; a rebuild overwrites it.
2. Open the copy in PowerPoint.
3. For each slide you need, duplicate the layout slide that fits and replace its text.
4. Delete the example slides you did not use.
5. Replace the speaker notes with what you will say.

## The layouts

| Slide | Layout | Use it for |
|---|---|---|
| 1 | Title | Brand blue, logo top left, eyebrow, headline, presenter line. |
| 2 | Section divider | Brand blue, one headline to start a new part. |
| 3 | Headline plus text | Eyebrow, headline, up to four short lines. |
| 4 | Two column | Headline and two text columns to compare two things. |
| 5 | Headline plus image | Headline left, one picture right, caption under it. |
| 6 | Table | Headline and a table of at most 5 rows and 4 columns. |
| 7 | Chart | Headline and one native bar chart with a source line. |
| 8 | Numbers | Three big published figures with labels. |
| 9 | Quote or takeaway | One sentence, large. |
| 10 | Closing | Brand blue, logo, "Your challenge:" eyebrow, one action, name line. |

## Rules

- One idea per slide. If a slide makes two points, split it.
- Headline under 10 words. It states the point, not the topic.
- No bullet walls. At most four short lines of text on a slide.
- Charts use the palette colors in tokens.json, in order. One series uses brand blue. No seventh color.
- A source line under every chart and table that names the release.
- The logo goes only on brand blue slides (Title and Closing). On a white slide, write the program name in text.
- Do not add colors, fonts or sizes. Everything comes from design/tokens.json and design/README.md.
- Counts on a slide come from published figures only. See AGENTS.md, Privacy.
- ASCII text only, as in AGENTS.md.

To edit the chart, right click it and choose Edit Data. To swap the picture, delete the picture slot box and insert your image in the same place.

## Rebuild it

The template is built by design/templates/build_deck_template.py from design/tokens.json. When the tokens change, rebuild it; never fix the look by hand in the pptx.

From the repo root:

    python answer-als/agent-handbook/design/templates/build_deck_template.py

It reads the data root from devices.json (through board_check.data_path) and overwrites the pptx. Then run python check.py answer-als/agent-handbook and put the new sha256 in answer-als/agent-handbook/REPORT.md.

Fonts: Helvetica Neue for text, Courier New for code. On Windows PowerPoint shows Arial in place of Helvetica Neue.

On the MacBook: use python3, not python. If python-pptx fails to import, run it as arch -arm64 python3 answer-als/agent-handbook/design/templates/build_deck_template.py. The script also retries under arch -arm64 on its own.
