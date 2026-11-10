
"""
Secure Customer Pipeline Package
"""

from .ingest import ingest_customers
from .validation import validate_customer
from .security import safe_output_path, calculate_sha256

__version__ = "1.0.0"
