
# Secure Customer Data Pipeline

## Project Overview

This project is developed using Python to create a secure customer data processing pipeline.

It reads customer records from CSV or JSON files, validates customer information, sanitizes input data, and saves valid records into a JSON output file.

## Project Features

1. CSV and JSON data ingestion.
2. Customer ID validation.
3. Email validation.
4. Pincode validation.
5. Customer name sanitization.
6. Spend validation.
7. Secure output file path handling.
8. SHA-256 file integrity verification.
9. Error logging.

## Project Structure

secure_customer_pipeline/
│
├── logs/
│   └── pipeline.log
│
├── output/
│
├── pipeline_core/
│   ├── __init__.py
│   ├── ingest.py
│   ├── validation.py
│   └── security.py
│
├── customers.csv
├── main.py
└── README.md

## Requirements

- Python 3.x
- No external libraries required.

## Input File Format

The CSV file should contain these columns:

cid,name,email,pin,spend

Example:

C001, Rahul, rahul@gmail.com, 285001, 1500

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

python main.py

## Output

The pipeline generates:

- output/validated_customers.json
- logs/pipeline.log

It also displays the total records, valid records, output file path, and SHA-256 hash.

## Security

The project uses input validation, HTML escaping, safe output paths, and SHA-256 hashing to improve data security and file integrity.

## Version

1.0.0
