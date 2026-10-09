#!/usr/bin/env python3
"""Run lightweight offline integrity checks; does not train or download data."""
from pathlib import Path
import ast
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "AfriTune_Fon_NER_Public_English.ipynb"
REQUIRED = [
    "README.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "CITATION.md",
    "CHANGELOG.md",
    "docs/reproducibility.md",
    "docs/notebook_audit.md",
    "docs/licensing.md",
    "docs/roadmap.md",
    "results/ner_validation_report.csv",
    "results/ner_test_report.csv",
    "results/validation_loss.png",
    "results/ner_metrics.png",
    "results/global_comparison.png",
    "results/entity_f1_comparison.png",
    "results/generalization_gap.png",
]
missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
if missing:
    sys.exit("Missing repository files: " + ", ".join(missing))

notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
assert notebook.get("nbformat") == 4, "Notebook must use nbformat 4"
assert isinstance(notebook.get("cells"), list) and notebook["cells"], "Notebook is empty"
for index, cell in enumerate(notebook["cells"]):
    assert cell.get("cell_type") in {"code", "markdown", "raw"}, index
    assert isinstance(cell.get("source"), (str, list)), index

script = ROOT / "scripts/download_fon.py"
ast.parse(script.read_text(encoding="utf-8"), filename=str(script))
print(f"Static checks passed: {len(notebook['cells'])} notebook cells; "
      f"{len(REQUIRED)} required repository files.")
print("No notebook cells, training, or network downloads were executed.")
