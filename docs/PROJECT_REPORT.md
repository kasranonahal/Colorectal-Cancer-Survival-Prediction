# Research methodology and reported results

## Thesis provenance

**Title (translated):** Investigation of Colorectal Cancer Patient Survival Using Patient Registry Data  
**Researcher:** Amirkasra Nonahal  
**Supervisor:** Dr. Mansor Vali  
**Institution:** K. N. Toosi University of Technology  
**Source:** *Bachelor Thesis.pdf*, 90-page uploaded thesis, especially Chapters 2–5.

## Problem and data

The thesis studies colorectal cancer survival using cases obtained from the US **SEER (Surveillance, Epidemiology, and End Results)** cancer registry. The selected cohort was diagnosed during **2010–2012** with an approximately 16–74-year age criterion.

The work considers demographic, tumor and pathology features, including sex, race, AJCC stage, grade, perineural invasion, tumor size and location, histology, surgery, and lymph-node counts. The thesis describes substantial challenges from missing values, inconsistent registry codes and class imbalance.

## Methodology

1. Extract colorectal cancer data from SEER using the documented filtering criteria.
2. Review feature distributions, missingness and outliers.
3. Encode categorical attributes and scale numeric features.
4. Train neural-network models for survival outcome estimation.
5. Compare two formulations:
   - **Regression followed by classification** of the predicted survival period.
   - **Three-class classification**, with class balancing via **SMOTE** in the experiments documented in the thesis.
6. Evaluate models using accuracy, confusion matrices and runtime.

## Results recorded in the thesis

| Method | Reported accuracy | Reported training / evaluation time |
|---|---:|---:|
| Regression + classification | **76.7%** | ~5 minutes |
| Three-class classification | **70.9%** | ~3 minutes |

The comparison originates from **Table 5 on printed page 75 / PDF page 81** of the thesis. This repository does not claim to have reproduced the reported numbers.

The thesis notes that the three-class dataset was imbalanced and describes SMOTE as an approach for creating synthetic minority-class training examples. The reported test-set distribution in Table 3 on printed pages 73–74 contains **4,735 observations** across the documented categories (449, 932, 3,354). These are historical values from the thesis, not independently verified counts.

## Technical limitations

- The original experimental notebooks contain multiple versions and exploratory variants.
- Legacy notebook workflows depend on original CSV/XLSX files, which are excluded from the public repository pending access and disclosure review.
- Preprocessing, resampling and cross-validation should be rechecked for leakage before interpreting accuracy.
- The notebook labeled Fashion-MNIST is a separate learning example, **not a colorectal-cancer model**.
- These results are not suitable for clinical use.

## Reproduction roadmap

1. Document authorized SEER extraction criteria and dataset schema.
2. Pin dependency versions and record Python environment.
3. Keep held-out test data isolated from imputation, scaling and resampling.
4. Implement stratified CV with preprocessing inside training folds.
5. Report uncertainty, sensitivity/recall by class, and external validation when possible.
