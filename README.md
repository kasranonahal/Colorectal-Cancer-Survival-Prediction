# Colorectal Cancer Survival Prediction

Exploratory analysis and machine-learning experiments for colorectal cancer outcomes, including survival classification, survival-period prediction, neural-network models, and missing-data imputation.

## Contents

- `notebooks/`: curated representative notebooks, numbered by topic.
- `docs/notebook_inventory.csv`: mapping between original and curated notebook files.
- `data/README.md`: guidance on acquiring and handling datasets.

## Important notes

- This is a **curated archival organization**, not a verified reproduction or refactoring of all experiments.
- Notebooks retain original code, including original dataset paths and dependencies; you may need to adapt those paths before running.
- Notebook outputs and execution counts have been cleared to avoid publishing embedded dataset previews.
- Original CSV, Excel, PDF files, and alternate notebook copies were **not included** in this shareable package.
- Before public distribution of datasets, verify source licensing and that no patient-level identifying data are present.
- This project is for research/education, not clinical decision-making.

## Getting started

```bash
python -m venv .venv
python -m pip install -r requirements.txt
jupyter lab
```

Package versions are not pinned because the original environment was not supplied.