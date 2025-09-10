-- schema.sql
-- This script drops existing tables to ensure a clean setup and then creates them.

-- Drop tables if they already exist to avoid errors on re-run
DROP TABLE IF EXISTS Claims;
DROP TABLE IF EXISTS Policyholders;
DROP TABLE IF EXISTS Hospitals;

-- Table to store information about policyholders
CREATE TABLE Policyholders (
    policyholder_id VARCHAR(20) PRIMARY KEY,
    age INT,
    gender VARCHAR(10),
    location VARCHAR(50)
);

-- Table to store information about network and non-network hospitals
CREATE TABLE Hospitals (
    hospital_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(50)
);

-- Central table to store all claim transactions
CREATE TABLE Claims (
    claim_id VARCHAR(20) PRIMARY KEY,
    policyholder_id VARCHAR(20) NOT NULL REFERENCES Policyholders(policyholder_id),
    hospital_id VARCHAR(20) NOT NULL REFERENCES Hospitals(hospital_id),
    claim_amount NUMERIC(10, 2) NOT NULL,
    diagnosis_code VARCHAR(10),
    procedure_code VARCHAR(10),
    claim_date DATE NOT NULL,
    is_fraud BOOLEAN NOT NULL
);