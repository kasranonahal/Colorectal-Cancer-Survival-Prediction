# Colorectal Cancer Survival Prediction

**Bachelor's thesis research project** by Amirkasra Nonahal, supervised by Dr. Mansor Vali at K. N. Toosi University of Technology (2022 / 1401).

## Project overview

This research investigated whether artificial neural networks could estimate survival outcomes for patients diagnosed with colorectal cancer using records obtained from the **Surveillance, Epidemiology, and End Results (SEER)** registry.

The thesis described SEER cases diagnosed in **2010–2012**, with an age-based inclusion criterion of approximately **16–74 years**. The study combined data cleaning, feature selection, visualization, neural-network training, and comparison of alternative prediction formulations.

## Research workflow

1. **Data acquisition:** colorectal cancer registry data from SEER.
2. **Exploration and feature selection:** patient demographics, cancer stage and grade, tumor size and primary site, histology, surgery, perineural invasion, and examined/positive lymph-node counts.
3. **Data preprocessing:** missing-value handling, categorical encoding, scaling and sample selection.
4. **Model development:** artificial neural networks for survival prediction, including a regression-plus-classification approach and a three-class classification approach.
5. **Evaluation:** predicted versus observed classes, confusion matrices, accuracy measures, and training-time comparison.

## Reported thesis results

| Approach | Reported accuracy | Approximate runtime |
| --- | ---: | ---: |
| Regression followed by classification | **76.7%** | **5 minutes** |
| Three-class classification | **70.9%** | **3 minutes** |

**Source:** Bachelor's thesis, Chapter 4, Table 5, printed page 75 (PDF page 81). These figures are **historical results reported in the thesis**. They were **not reproduced or independently verified** in this repository.

The classification workflow used **SMOTE** to address class imbalance. The thesis also compared confusion matrices and noted that the regression-plus-classification approach performed better in that experiment.

## Repository structure

- `experiments/binary_survival_classification.py` — archived/adapted binary survival classification example.
- `examples/fashion_mnist_baseline.py` — unrelated neural-network tutorial code, clearly separated from the cancer study.
- `notebooks/` — intended location of the complete curated Jupyter notebook collection (not yet uploaded).
- `docs/PROJECT_REPORT.md` — detailed description of the research design and reported results.
- `data/README.md` — dataset handling and access notes.
- `requirements.txt` — approximate dependencies; original environment has not been restored.

## Running the research

The original experiments depend on historical datasets and notebook-specific library versions. **They are not currently a reproducible pipeline.** To execute them, obtain the relevant SEER data under its applicable access and redistribution conditions and update the notebook paths.

```bash
python -m venv .venv
python -m pip install -r requirements.txt
jupyter lab
```

## Limitations and responsible use

- The work is an **academic historical project, not a medical device or clinical tool**.
- Metrics are thesis-reported, not newly tested on an independent external cohort.
- Some original notebook experiments may contain train/test leakage or preprocessing/evaluation issues; validate all splits, resampling, encoding, and model assumptions before interpreting results.
- Patient-level CSV/XLSX data and unreviewed notebook outputs are not published here.
- The Fashion-MNIST example is not part of the colorectal cancer study.

## Next steps

Restore the complete curated notebooks; validate dataset provenance; refactor cross-validation and preprocessing; add reproducible environments and evaluation scripts.
