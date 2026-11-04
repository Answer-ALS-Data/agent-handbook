# Scripts

Checkers for finished files, the runner that calls them and the build scripts for the templates. They target Python 3.10 and use the standard library, plus python-docx, python-pptx or openpyxl where a checker needs one.

## prose.py

The banned list from the Writing section of `references/brand.md`: em dash, en dash, the stock words and the quoted phrases. `find_banned(text)` returns a list of `(word, snippet)` pairs. URLs in the text are skipped. It uses the standard library only and does nothing at import. Each format checker imports it and adds a `prose` check that prints one FAIL line per hit:

    import sys; sys.path.insert(0, "scripts")
    import prose
    hits = prose.find_banned(text)

## check_all.py

Runs every `scripts/check_<ext>.py` that exists against each sample file `*sample*.<ext>` in `assets/`, for example `check_docx.py` against `assets/answer-als-sample.docx`; `check_deck.py` runs against `*sample*.pptx` and `check_html.py` against `*report*.html`. A SKIP line from a checker (such as print-render) is shown under its PASS line. With no argument, a sample not in `assets/` is looked for in the board's data root assets folder (`<data root>/answer-als/agent-handbook/v1/assets/`, where the built docx, pptx and xlsx live) when the script runs on the board; its line ends in "(data root)". Give another folder as the only argument to check the samples there instead; a folder that does not exist is a SKIP. It prints one PASS, FAIL or SKIP line per checker and sample, and exits 1 on any FAIL. A checker with no sample is a SKIP, and no checkers at all is a pass:

    python scripts/check_all.py

## build_word.py

Builds the Word template `answer-als-template.docx` and the sample `answer-als-sample.docx` (with its chart, `answer-als-sample-figure-1.png`) from `design/tokens.json` and the logo, the same bytes on every run. It installs python-docx and matplotlib if they are missing. Give an output folder as the only argument; without one it writes to `assets/`:

    python scripts/build_word.py

Change the Word look here and rebuild; never edit the built .docx by hand.

## check_docx.py

Checks a finished Word document against `references/word.md`: the template styles are defined, no body run has a direct font, size or color, no Title word is over 13 characters, each Heading 1 reads "N. Name", heading levels never skip, only the first Heading 1 has page break before, every table uses Answer ALS Table with a Caption after it and row 1 marked as the header, number cells and their headers are right aligned, the file name has no spaces, the cover date and header section are not the template placeholders, and the prose check from `prose.py`. It prints one PASS or FAIL line per check and exits 1 on any FAIL. It does not run on SOPs:

    python scripts/check_docx.py answer-als-release-8-summary.docx

## aals_pptx.py

The PowerPoint helpers named in `references/powerpoint.md`: `layout_named`, `add_hf`, `set_lines`, `add_table`, `add_chart`, `add_image`, `add_callout` and `set_core`. It needs python-pptx and lxml and does nothing at import:

    import sys; sys.path.insert(0, "scripts")
    import aals_pptx

## build_powerpoint.py

Builds the PowerPoint template `answer-als-template.pptx` (the master, the eight layouts, the Answer ALS Table style and one guide slide per layout) and the sample `answer-als-sample.pptx` from `design/tokens.json` and the logo, the same bytes on every run. It installs python-pptx, XlsxWriter and matplotlib if they are missing. Give an output folder as the only argument; without one it writes to `assets/`:

    python scripts/build_powerpoint.py

Change the PowerPoint look here and rebuild; never edit the built .pptx by hand.

## check_deck.py

Checks a finished deck against `references/powerpoint.md`: the Answer ALS Table style is defined, every slide uses a template layout, the deck opens with Title and ends with Closing, content slides carry the footer and slide number, placeholder runs have no direct font, size or color, tables use Answer ALS Table, fit 7 rows and 5 columns with no merged cells and right align numbers and their headers, bullets keep to six items and two levels, numbered lists are in brand blue with no typed numbers, titles are at most 55 characters, Chart and Picture slides hold their object with alt text and a caption and Table slides a table and a caption, Title and Content or Two Content slides hold three paragraphs or an object, no gradient or shadow, the file name has no spaces, and the prose check from `prose.py`. It prints one PASS or FAIL line per check and exits 1 on any FAIL. `check_all.py` runs it on `*sample*.pptx`:

    python scripts/check_deck.py answer-als-release-8-summary.pptx

## build_markdown_figure.py

Builds `assets/answer-als-sample-figure-1.png`, the chart in the Markdown sample, with `figure_png` from `build_word.py`, so it is the same bytes as the chart in the Word sample. It needs matplotlib and python-docx. Give an output folder as the only argument; without one it writes to `assets/`:

    python scripts/build_markdown_figure.py

## check_md.py

Checks a finished Markdown file against `references/markdown.md`: UTF-8 with LF endings and one final newline, the eyebrow `ANSWER ALS` on line 1, the only H1 on line 3 and the italic subtitle and date on line 5, no front matter, headings to H3 with no skipped level, H2 all numbered in order or none, no trailing punctuation, bold or links in headings, bullets with `-`, every table with a bold `Table N.` label, a `---` or `---:` separator and no empty cells, every image with alt text, a bold `Figure N.` label in order and a relative path that resolves, a language on every code fence, callouts labeled Note, Key point or Warning at most one per H2, no HTML, relative links and `#fragment` links that resolve, and the prose check from `prose.py`. It prints one PASS or FAIL line per check and exits 1 on any FAIL. `check_all.py` runs it on `*sample*.md`:

    python scripts/check_md.py answer-als-release-8-notes.md

## check_html.py

Checks a finished HTML page against `references/html.md`: UTF-8 with LF endings, `lang`, charset, viewport and color-scheme metas, a title ending in " - Answer ALS", no script, no link and no remote image, one style block that starts with the stylesheet of `assets/answer-als-report.html` unchanged, no style attribute but a width on `.bar`, brand hex only in `:root`, `@page` and inline SVG (the brand hex are read from `design/tokens.json`), every mark reading "Answer ALS", numbered h1 sections each after a `header.doc-header` with the same number, no `.doc-footer`, table captions with `aria-labelledby`, `thead` and `scope="col"`, figure captions in order, no empty cells, `num` on number cells and their headers, callouts, SVG with role img, title and desc, quotes with a p and a footer, no bare `&` or `<` in text, and the prose check from `prose.py`. Last it prints the page in headless Chrome or Edge (`--headless=new`, its own temp profile) and reports print-render apart: PASS with the page count, SKIP when no browser is found or it does not finish in 60 seconds, FAIL only when the browser exits without a PDF. It exits 1 on any FAIL. `check_all.py` runs it on `*report*.html`:

    python scripts/check_html.py answer-als-release-8-report.html

## aals_excel.py

The Excel helpers named in `references/excel.md`: `setup_sheet`, `new_sheet`, `set_widths`, `add_table`, `add_chart`, `chart_text`, `finish` and `save`, with the brand constants. `save` writes each formula's computed value as its cached value, so Protected View shows numbers. It needs openpyxl and does nothing at import:

    import sys; sys.path.insert(0, "scripts")
    import aals_excel

## build_excel.py

Builds the Excel template `answer-als-template.xlsx` and the sample `answer-als-sample.xlsx` (two data sheets with a table, a total row and a chart, and a Notes sheet) with `aals_excel.py`, the same bytes on every run. It installs openpyxl if it is missing. Give an output folder as the only argument; without one it writes to `<data root>/answer-als/agent-handbook/v1/assets/` on the board, else to `assets/`:

    python scripts/build_excel.py

Change the Excel look here and in `aals_excel.py` and rebuild; never edit the built .xlsx by hand.

## check_xlsx.py

Checks a finished workbook against `references/excel.md`: the eighteen Answer ALS named styles and the Answer ALS theme, the title block in A1:A4 with a real date in A4 and an empty row 5, every cell from row 6 down in an Answer ALS style with no direct font, fill or number format, row 7 in Answer ALS Header (bold white on brand blue), one style per body column with numbers stored as numbers, no summed percent total, no merged cells or hidden rows and columns, freeze pane, gridlines off, print titles, one page wide and "Answer ALS" in the print header, a table title above and a "Table N." caption under every table, a "Figure N." caption under every chart, chart series in brand colors with no title and the legend at the top off the plot area, the Notes sheet labels, fullCalcOnLoad, a cached value in every formula cell, no default sheet name and no space in the file name, and the prose check from `prose.py`. It prints one PASS or FAIL line per check and exits 1 on any FAIL. `check_all.py` runs it on `*sample*.xlsx`:

    python scripts/check_xlsx.py answer-als-visits-by-site.xlsx
