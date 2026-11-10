
import csv
import json
from pathlib import Path


def ingest_customers(file_path):
    """Read customer records from a CSV or JSON file."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() == ".csv":
        with open(path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)

    elif path.suffix.lower() == ".json":
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    else:
        raise ValueError("Only CSV and JSON files are supported.")
