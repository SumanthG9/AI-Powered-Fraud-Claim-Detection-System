# data/generate_new_test_data.py

import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import os

# Initialize Faker for generating fake data
fake = Faker('en_IN')

# --- Configuration for New Test Data ---
NUM_NEW_POLICYHOLDERS = 3000
NUM_NEW_HOSPITALS = 100
NUM_NEW_CLAIMS = 10000
FRAUD_PERCENTAGE = 0.06 # Slightly different fraud rate for a robust test

# --- ID Starting Points to Avoid Overlap with Original Data ---
POLICYHOLDER_START_ID = 5000
HOSPITAL_START_ID = 200
CLAIM_START_ID = 15000

# --- 1. Generate New Policyholders ---
def generate_policyholders(n, start_id):
    data = {
        'policyholder_id': [f'PH{i:05d}' for i in range(start_id, start_id + n)],
        'age': [random.randint(18, 80) for _ in range(n)],
        'gender': [random.choice(['Male', 'Female']) for _ in range(n)],
        'location': [fake.city() for _ in range(n)]
    }
    return pd.DataFrame(data)

# --- 2. Generate New Hospitals ---
def generate_hospitals(n, start_id):
    # Designate a few new hospitals as potentially fraudulent
    fraudulent_hospitals = [f'H{i:04d}' for i in range(start_id, start_id + 5)]
    data = {
        'hospital_id': [f'H{i:04d}' for i in range(start_id, start_id + n)],
        'name': [f"{fake.company()} Hospital" for _ in range(n)],
        'location': [fake.city() for _ in range(n)]
    }
    return pd.DataFrame(data), fraudulent_hospitals

# --- 3. Generate New Claims ---
def generate_claims(n, start_id, policyholders_df, hospitals_df, fraudulent_hospitals):
    policyholder_ids = policyholders_df['policyholder_id'].tolist()
    hospital_ids = hospitals_df['hospital_id'].tolist()
    
    claims_data = []
    for i in range(n):
        claim_id = f'C{start_id + i:06d}'
        policyholder_id = random.choice(policyholder_ids)
        is_fraud = np.random.rand() < FRAUD_PERCENTAGE
        
        # Fraud Logic
        if is_fraud:
            hospital_id = random.choice(fraudulent_hospitals)
            claim_amount = round(random.uniform(90000, 300000), 2)
            procedure_code = random.choice(['P301', 'P302'])
        else:
        # Normal Logic
            hospital_id = random.choice(hospital_ids)
            claim_amount = round(random.uniform(5000, 85000), 2)
            procedure_code = random.choice(['P101', 'P102', 'P201', 'P202'])

        start_date = datetime(2025, 1, 1) # Future dates to ensure it's "new"
        end_date = datetime.now()
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
    print("Generating new synthetic test data...")
    
    # Generate data
    new_policyholders = generate_policyholders(NUM_NEW_POLICYHOLDERS, POLICYHOLDER_START_ID)
    new_hospitals, fraudulent_hospitals_list = generate_hospitals(NUM_NEW_HOSPITALS, HOSPITAL_START_ID)
    new_claims = generate_claims(NUM_NEW_CLAIMS, CLAIM_START_ID, new_policyholders, new_hospitals, fraudulent_hospitals_list)
    
    # Define output paths
    output_dir = 'data'
    policyholders_path = os.path.join(output_dir, 'new_policyholders.csv')
    hospitals_path = os.path.join(output_dir, 'new_hospitals.csv')
    claims_path = os.path.join(output_dir, 'new_claims.csv')

    # Save to CSV files
    new_policyholders.to_csv(policyholders_path, index=False)
    new_hospitals.to_csv(hospitals_path, index=False)
    new_claims.to_csv(claims_path, index=False)
    
    print(f"\nData generation complete!")
    print(f"Generated {len(new_claims)} new claims.")
    print(f"Fraudulent claims: {new_claims['is_fraud'].sum()}")
    print(f"New CSV files saved in the '{output_dir}/' directory:")
    print(f"- {policyholders_path}")
    print(f"- {hospitals_path}")
    print(f"- {claims_path}")
