# data/generate_data.py

import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker for generating fake data
fake = Faker('en_IN') # Using Indian locale for more relevant data

# --- Configuration ---
NUM_POLICYHOLDERS = 5000
NUM_HOSPITALS = 200
NUM_CLAIMS = 15000
FRAUD_PERCENTAGE = 0.05 # 5% of claims will be fraudulent

# --- 1. Generate Policyholders ---
def generate_policyholders(n):
    data = {
        'policyholder_id': [f'PH{i:05d}' for i in range(n)],
        'age': [random.randint(18, 80) for _ in range(n)],
        'gender': [random.choice(['Male', 'Female']) for _ in range(n)],
        'location': [fake.city() for _ in range(n)]
    }
    return pd.DataFrame(data)

# --- 2. Generate Hospitals ---
def generate_hospitals(n):
    # Designate a few hospitals as potentially fraudulent
    fraudulent_hospitals = [f'H{i:04d}' for i in range(5)] # First 5 hospitals are high-risk
    data = {
        'hospital_id': [f'H{i:04d}' for i in range(n)],
        'name': [f"{fake.company()} Hospital" for _ in range(n)],
        'location': [fake.city() for _ in range(n)]
    }
    return pd.DataFrame(data), fraudulent_hospitals

# --- 3. Generate Claims ---
def generate_claims(n, policyholders_df, hospitals_df, fraudulent_hospitals):
    policyholder_ids = policyholders_df['policyholder_id'].tolist()
    hospital_ids = hospitals_df['hospital_id'].tolist()
    
    claims_data = []
    for i in range(n):
        claim_id = f'C{i:06d}'
        policyholder_id = random.choice(policyholder_ids)
        is_fraud = np.random.rand() < FRAUD_PERCENTAGE
        
        # --- Fraud Logic ---
        if is_fraud:
            # Fraudulent claims are more likely to come from high-risk hospitals
            hospital_id = random.choice(fraudulent_hospitals)
            # Fraudulent claims have significantly higher amounts
            claim_amount = round(random.uniform(80000, 250000), 2)
            # Fraudulent claims might use specific procedure codes
            procedure_code = random.choice(['P301', 'P302']) # Codes associated with fraud
        else:
            # --- Normal Logic ---
            hospital_id = random.choice(hospital_ids)
            claim_amount = round(random.uniform(5000, 75000), 2)
            procedure_code = random.choice(['P101', 'P102', 'P201', 'P202'])

        start_date = datetime(2023, 1, 1)
        end_date = datetime(2025, 9, 10)
        claim_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        
        claims_data.append({
            'claim_id': claim_id,
            'policyholder_id': policyholder_id,
            'hospital_id': hospital_id,
            'claim_amount': claim_amount,
            'diagnosis_code': f"D{random.randint(100, 500)}",
            'procedure_code': procedure_code,
            'claim_date': claim_date.strftime('%Y-%m-%d'),
            'is_fraud': is_fraud
        })
        
    return pd.DataFrame(claims_data)

# --- Main Execution ---
if __name__ == "__main__":
    print("Generating synthetic data...")
    
    # Generate data
    policyholders = generate_policyholders(NUM_POLICYHOLDERS)
    hospitals, fraudulent_hospitals_list = generate_hospitals(NUM_HOSPITALS)
    claims = generate_claims(NUM_CLAIMS, policyholders, hospitals, fraudulent_hospitals_list)
    
    # Save to CSV files inside the 'data' directory
    policyholders.to_csv('data/policyholders.csv', index=False)
    hospitals.to_csv('data/hospitals.csv', index=False)
    claims.to_csv('data/claims.csv', index=False)
    
    print(f"Data generation complete! {len(claims)} claims created.")
    print(f"Fraudulent claims: {claims['is_fraud'].sum()}")
    print("CSV files saved in the 'data/' directory.")