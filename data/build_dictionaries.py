"""Build dictionary-answer-als.md and dictionary-als-tdi.md from the two clinical dictionaries.

Reads only the dictionary files: the Answer ALS clinical dictionary CSV and the ALS TDI data dictionary xlsx. Writes one table per form with field name, label, type and coded values as the dictionary gives them. A cohort page longer than 1,000 lines is split into one page per form group, and the cohort page becomes the list of forms and parts. Output is ASCII with LF line ends, the same bytes on every run.

    python build_dictionaries.py                      dictionaries from the data root, pages written next to this script
    python build_dictionaries.py --answer-als CSV --als-tdi XLSX --out DIR
"""
import argparse
import csv
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
ANSWER_ALS = "answer-als/dictionary/r8/__Clinical_Dictionary_Sep_2026.csv"
ALS_TDI = "als-tdi/clinical/inputs/delivery-r2/clinical_data_package/TDI_data_dictionary.xlsx"
MAX_LINES = 1000
ASCII = {"\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"', "\u2013": "-", "\u2014": "-", "\u00d7": "x", "\u2265": ">=", "\u2264": "<=", "\u00a0": " "}
GROUPS = {
    "answer-als": [
        ("assessments", "Clinical assessments", ["ALS_CBS", "ALSFRS_R", "Ashworth_Spasticity_Scale", "CNS_Lability_Scale", "Grip_Strength_Testing", "Hand_Held_Dynamometry", "Reflexes", "Vital_Capacity", "Vital_Signs"]),
        ("history", "Diagnosis, history and demographics", ["AALSDXFX", "AALSHXFX", "ALS_Gene_Mutations", "Demographics", "Environmental_Questionnaire", "Family_History_Log", "Medical_History", "NEUROLOG", "subjects"]),
        ("events-and-samples", "Events, logs, labs and samples", ["ANSASFD", "ANSWER_ALS_MobileApp", "ANSWER_ALS_Medications_Log", "Auxiliary_Chemistry", "Auxiliary_Chemistry_Labs", "Cerebrospinal_Fluid", "Diaphragm_Pacing_System_Device", "DNA_Sample_Collection", "Feeding_Tube_Placement", "Mortality", "NIV_Log", "PBMC_Sample_Collection", "Permanent_Assisted_Ventilation", "Plasma_Sample", "Serum_Sample", "Tracheostomy"]),
    ],
}
COHORTS = {
    "answer-als": {
        "title": "Answer ALS clinical dictionary",
        "source": "__Clinical_Dictionary_Sep_2026.csv",
        "about": [
            "Every field of the Answer ALS clinical forms, one table per form, generated from the clinical dictionary __Clinical_Dictionary_Sep_2026.csv (Release 8). The dictionary ships inside the clinical package and has one row per form column. Form Name is the CSV file name without .csv.",
            "Columns: Field name is the column header in the form CSV. Label is the dictionary's New Field Label. Type is numeric or text. Coded values are the codes and labels for a coded field, as \"code, label\" pairs separated by a pipe, as the dictionary gives them. Coded fields are stored as the code. Text is written in ASCII (curly quotes and dashes become plain ones) and a # before a number is written as the word number, and a web link is replaced by the words (web link in the dictionary file).",
        ],
    },
    "als-tdi": {
        "title": "ALS TDI clinical dictionary",
        "source": "TDI_data_dictionary.xlsx",
        "about": [
            "Every field of the ALS TDI clinical tables, one table per form, generated from the data dictionary that came with the Release 2 delivery, TDI_data_dictionary.xlsx (published as TDI_data_dictionary.csv). Form names are as the dictionary gives them: the file name without the _V2 suffix, and TDI_ACTVITY is the TDI_ACTIVITY_V2 file. A table with no dictionary rows is not listed.",
            "Columns: Field name is the column header in the table. Label is the dictionary's Additional Notes column, blank where the dictionary has none. Type is numeric or text. Coded values are the codes and labels for a coded field, as the dictionary gives them. Text is written in ASCII (curly quotes and dashes become plain ones) and a # before a number is written as the word number, and a web link is replaced by the words (web link in the dictionary file).",
        ],
    },
}


def clean(value):
    text = "" if value is None else str(value)
    text = "".join(ASCII.get(ch, ch) for ch in text)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"#(?=\d)", "number ", text)
    text = re.sub(r"https?://[^\s)]+", "(web link in the dictionary file)", text)
    return re.sub(r"\s+", " ", text).strip().replace("|", "\\|")


def read_answer_als(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    head = rows[0]
    at = {name: head.index(name) for name in ("Form Name", "Form Label", "Field Name", "New Field Label", "Values", "Field Type")}
    forms = {}
    for row in rows[1:]:
        if not any(cell.strip() for cell in row):
            continue
        form = forms.setdefault(row[at["Form Name"]].strip(), {"label": clean(row[at["Form Label"]]), "fields": []})
        form["fields"].append((clean(row[at["Field Name"]]), clean(row[at["New Field Label"]]), clean(row[at["Field Type"]]), clean(row[at["Values"]])))
    return forms


def read_als_tdi(path):
    import openpyxl

    book = openpyxl.load_workbook(path, read_only=True, data_only=True)
    rows = [list(row) for row in book.worksheets[0].iter_rows(values_only=True)]
    book.close()
    head = [str(cell).strip() if cell is not None else "" for cell in rows[0]]
    at = {name: head.index(name) for name in ("Form Name", "Field Name", "Values", "Field Type", "Additional Notes")}
    forms = {}
    for row in rows[1:]:
        if not any(cell is not None and str(cell).strip() for cell in row):
            continue
        cell = lambda name: row[at[name]] if at[name] < len(row) else None
        form = forms.setdefault(str(cell("Form Name")).strip(), {"label": "", "fields": []})
        form["fields"].append((clean(cell("Field Name")), clean(cell("Additional Notes")), clean(cell("Field Type")), clean(cell("Values"))))
    return forms


def form_block(name, form):
    lines = [f"## {name}", ""]
    lines.append(f"Form label: {form['label']}. Fields: {len(form['fields'])}." if form["label"] else f"Fields: {len(form['fields'])}.")
    lines += ["", "| Field name | Label | Type | Coded values |", "|---|---|---|---|"]
    lines += [f"| {field} | {label} | {kind} | {values} |" for field, label, kind, values in form["fields"]]
    return lines + [""]


def page(title, about, source, forms, names):
    lines = [f"# {title}", ""]
    for para in about:
        lines += [para, ""]
    lines += [f"Source: {source}. Written from the dictionary rows only, never from a data file.", ""]
    for name in names:
        lines += form_block(name, forms[name])
    return "\n".join(lines).rstrip("\n") + "\n"


def pages_for(cohort, forms):
    info = COHORTS[cohort]
    stem = f"dictionary-{cohort}"
    whole = page(info["title"], info["about"], info["source"], forms, list(forms))
    if whole.count("\n") <= MAX_LINES:
        return {f"{stem}.md": whole}
    parts = []
    placed = set()
    for slug, title, names in GROUPS.get(cohort, []):
        names = [n for n in forms if n in names]
        placed.update(names)
        parts.append((slug, title, names))
    rest = [n for n in forms if n not in placed]
    if rest:
        parts.append(("other", "Other forms", rest))
    out = {}
    index = [f"# {info['title']}", ""]
    for para in info["about"]:
        index += [para, ""]
    index += [f"Source: {info['source']}. Written from the dictionary rows only, never from a data file.", ""]
    index += [f"The full dictionary passes {MAX_LINES:,} lines on one page, so it is split into one page per form group. This page lists every form, its field count (dictionary rows) and the page that holds its table.", ""]
    index += ["## Parts", ""]
    index += [f"- {stem}-{slug}.md: {title}." for slug, title, names in parts if names]
    index += ["", "## Forms", "", "| Form Name | Form label | Fields | Page |", "|---|---|---|---|"]
    where = {n: f"{stem}-{slug}.md" for slug, title, names in parts for n in names}
    index += [f"| {n} | {forms[n]['label']} | {len(forms[n]['fields'])} | {where[n]} |" for n in forms]
    out[f"{stem}.md"] = "\n".join(index) + "\n"
    for slug, title, names in parts:
        if names:
            out[f"{stem}-{slug}.md"] = page(f"{info['title']}: {title.lower()}", [f"Part of {stem}.md, which lists every form and the page that holds it."] + info["about"][1:], info["source"], forms, names)
    return out


def build(answer_als, als_tdi, out_dir):
    out_dir = Path(out_dir)
    written = []
    for cohort, forms in (("answer-als", read_answer_als(answer_als)), ("als-tdi", read_als_tdi(als_tdi))):
        for name, text in pages_for(cohort, forms).items():
            path = out_dir / name
            path.write_bytes(text.encode("ascii"))
            written.append(path)
    return written


def default_path(relative):
    for parent in HERE.parents:
        if (parent / "board_check.py").is_file():
            sys.path.insert(0, str(parent))
            import board_check

            return board_check.data_path(relative)
    sys.exit(f"dictionary not found, pass it as an argument: {relative}")


def main():
    parser = argparse.ArgumentParser(description="Build the clinical dictionary pages.")
    parser.add_argument("--answer-als", help="Answer ALS clinical dictionary CSV")
    parser.add_argument("--als-tdi", help="ALS TDI data dictionary xlsx")
    parser.add_argument("--out", default=str(HERE), help="folder to write the pages to")
    args = parser.parse_args()
    answer_als = Path(args.answer_als) if args.answer_als else default_path(ANSWER_ALS)
    als_tdi = Path(args.als_tdi) if args.als_tdi else default_path(ALS_TDI)
    for path in build(answer_als, als_tdi, args.out):
        print(f"wrote {path.name}: {len(path.read_text(encoding='ascii').splitlines())} lines")


if __name__ == "__main__":
    main()
