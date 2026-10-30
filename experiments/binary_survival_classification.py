"""Archived binary survival classification experiment, adapted from original notebook 03.

Requires a local CSV dataset; no patient-level data is included here.
Research code only: the original preprocessing performed resampling before
cross-validation, which risks optimistic evaluation. Do not use clinically.
"""
import numpy as np
import pandas as pd
import tensorflow as tf
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, confusion_matrix
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# Set this to your local, authorized dataset. Original path was Windows-specific.
DATA_PATH = "data/main.csv"
df = pd.read_csv(DATA_PATH)

# Historical project feature/target construction (column order dependent).
def class_survival(months):
    return "less than 10 months" if months < 10 else "10 months or more"

df["Survival_Months"] = df["Survival_Months"].apply(class_survival)
df = df.drop(columns=["Cause of death"], errors="ignore")
X = df.iloc[:, [1, 2, 4, 12]]
y = pd.factorize(df.iloc[:, 6])[0]

# WARNING: Historical procedure undersamples before the CV split.
# Future work should move resampling into each training fold.
sampler = RandomUnderSampler(random_state=0)
X_resampled, y_resampled = sampler.fit_resample(X, y)
y_categorical = tf.keras.utils.to_categorical(y_resampled)

predictions = []
truth = []
folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
for fold, (train_idx, test_idx) in enumerate(folds.split(X_resampled, y_resampled), 1):
    x_train, x_test = X_resampled.iloc[train_idx], X_resampled.iloc[test_idx]
    y_train, y_test = y_categorical[train_idx], y_categorical[test_idx]
    model = Sequential([
        Dense(25, input_dim=X_resampled.shape[1], activation="tanh"),
        Dense(20, activation="tanh"),
        Dense(10, activation="tanh"),
        Dense(2, activation="softmax"),
    ])
    model.compile(loss="categorical_crossentropy",
                  optimizer=tf.keras.optimizers.Adam(learning_rate=0.001))
    model.fit(x_train, y_train, validation_data=(x_test, y_test),
              verbose=0, batch_size=256, epochs=100)
    predicted = np.argmax(model.predict(x_test, verbose=0), axis=1)
    actual = np.argmax(y_test, axis=1)
    predictions.extend(predicted.tolist())
    truth.extend(actual.tolist())
    print(f"Fold {fold} accuracy: {accuracy_score(actual, predicted):.3f}")

print("Overall accuracy:", accuracy_score(truth, predictions))
print("Confusion matrix:\n", confusion_matrix(truth, predictions))
