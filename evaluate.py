# evaluate_new_data.py

import pandas as pd
import joblib
from sklearn.metrics import classification_report, accuracy_score, f1_score
import os
from scipy.sparse import issparse

print("--- Starting Final Evaluation on New 10,000 Sample Test Set ---")

# --- 1. Load Model and Preprocessor ---
try:
    preprocessor = joblib.load('backend/preprocessor.joblib')
    model = joblib.load('backend/model.joblib')
    print("Model and preprocessor loaded successfully.")
except FileNotFoundError:
    print("\nError: 'preprocessor.joblib' or 'model.joblib' not found.")
    print("Please make sure you have run the Jupyter Notebook to train and save the model first.")
    exit()

# --- 2. Load New Test Data ---
print("Loading new test data from CSV files...")
try:
    new_claims_df = pd.read_csv('data/new_claims.csv')
    new_policyholders_df = pd.read_csv('data/new_policyholders.csv')
    new_hospitals_df = pd.read_csv('data/new_hospitals.csv')
except FileNotFoundError:
    print("\nError: New test data CSV files not found.")
    print("Please run 'python data/generate_new_test_data.py' first.")
    exit()

# --- 3. Merge and Prepare Data ---
print("Merging and preparing the new test data...")
# Merge the data into a single comprehensive DataFrame
df_new = pd.merge(new_claims_df, new_policyholders_df, on='policyholder_id', how='left')
df_new = pd.merge(df_new, new_hospitals_df, on='hospital_id', how='left', suffixes=('_policyholder', '_hospital'))

# Define the exact feature set the model was trained on
features = ['claim_amount', 'age', 'gender', 'location_policyholder', 'location_hospital', 'procedure_code']
target = 'is_fraud'

# Ensure all required columns are present
if not all(feature in df_new.columns for feature in features):
    print("\nError: The new data is missing some of the required feature columns.")
    exit()

X_new_test = df_new[features].copy()
y_new_test = df_new[target]

# Ensure column names are strings, just in case
X_new_test.columns = [str(col) for col in X_new_test.columns]

# --- 4. Preprocess the New Data ---
print("Applying the preprocessor to the new data...")
X_new_test_processed = preprocessor.transform(X_new_test)

# Convert to dense array if it's a sparse matrix
if issparse(X_new_test_processed):
    X_new_test_processed = X_new_test_processed.toarray()

# --- 5. Make Predictions ---
print("Making predictions on the new data...")
y_new_pred = model.predict(X_new_test_processed)

# --- 6. Report Final Performance ---
print("\n--- FINAL PERFORMANCE REPORT (on 10,000 new samples) ---")

accuracy = accuracy_score(y_new_test, y_new_pred)
f1 = f1_score(y_new_test, y_new_pred, pos_label=True)

print(f"\nAccuracy on New Test Set: {accuracy:.4f}")
print(f"F1-Score for Fraud Class: {f1:.4f}")

print("\n--- Full Classification Report ---")
print(classification_report(y_new_test, y_new_pred, target_names=['Not Fraud (False)', 'Fraud (True)']))
