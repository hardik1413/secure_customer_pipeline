import hashlib
from pathlib import Path


def safe_output_path(filename, base_dir):
    """Prevent files from being created outside the output directory."""

    base = Path(base_dir).resolve()
    candidate = (base / filename).resolve()

    if candidate.parent != base:
        raise ValueError("Path traversal detected")

    return candidate


def calculate_sha256(file_path):
    """Calculate SHA-256 hash of a file."""

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()