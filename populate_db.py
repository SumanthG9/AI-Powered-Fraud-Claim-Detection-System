# populate_db.py

import pandas as pd
from sqlalchemy import create_engine
import os

# --- Database Connection Configuration ---
# IMPORTANT: Replace 'your_password' with your actual PostgreSQL password.
DB_USER = 'postgres'
DB_PASSWORD = '123456789' 
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'starhealth_fraud'

# Create the database connection string
DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URI)

# --- Data Loading Configuration ---
DATA_DIR = 'data'
FILES_TO_TABLES = {
    'policyholders.csv': 'policyholders',
    'hospitals.csv': 'hospitals',
    'claims.csv': 'claims'
}

# The order matters due to foreign key constraints in the 'claims' table.
# We must populate 'policyholders' and 'hospitals' before 'claims'.
INSERTION_ORDER = ['policyholders.csv', 'hospitals.csv', 'claims.csv']

# --- Main Execution ---
if __name__ == "__main__":
    print("Starting database population...")
    
    try:
        for filename in INSERTION_ORDER:
            table_name = FILES_TO_TABLES[filename]
            file_path = os.path.join(DATA_DIR, filename)
            
            print(f"Reading {filename}...")
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(file_path)
            
            print(f"Populating '{table_name}' table...")
            # Use pandas' to_sql() function to write the DataFrame to the SQL table
            # if_exists='append': adds the data to the table. Does not create or drop it.
            # index=False: prevents writing the DataFrame's index as a column.
            df.to_sql(table_name, engine, if_exists='append', index=False)
            
            print(f"Successfully populated '{table_name}'.")

        print("\nDatabase population complete!")

    except Exception as e:
        print(f"\nAn error occurred: {e}")