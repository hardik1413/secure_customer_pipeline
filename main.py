
import logging
import json
from pathlib import Path

from pipeline_core import (
    ingest_customers,
    validate_customer,
    safe_output_path,
    calculate_sha256
)

# Project directories
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
OUTPUT_DIR = BASE_DIR / "output"

LOG_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# Logging configuration
logging.basicConfig(
    filename=LOG_DIR / "pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():

    input_file = BASE_DIR / "customers.csv"

    try:
        # Step 1: Ingest customer data
        customers = ingest_customers(input_file)

        logging.info("Customer data ingestion started")

        # Step 2: Validate customer records
        valid_records = []

        for customer in customers:
            try:
                valid_customer = validate_customer(customer)
                valid_records.append(valid_customer)

            except ValueError as error:
                logging.warning("Invalid record skipped: %s", error)

        # Step 3: Save validated records
        output_file = safe_output_path(
            "validated_customers.json",
            OUTPUT_DIR
        )

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(valid_records, file, indent=4)

        # Step 4: Calculate SHA-256 hash
        file_hash = calculate_sha256(output_file)

        logging.info("Customer data validation completed")
        logging.info("SHA-256: %s", file_hash)

        print("Customer Pipeline Executed Successfully!")
        print("Total Records:", len(customers))
        print("Valid Records:", len(valid_records))
        print("Output File:", output_file)
        print("SHA-256 Hash:", file_hash)

    except Exception as error:
        logging.error("Pipeline failed: %s", error)
        print("Pipeline Error:", error)


if __name__ == "__main__":
    main()
