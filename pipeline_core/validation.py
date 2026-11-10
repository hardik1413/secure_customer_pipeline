
import re
import html


def validate_customer(record):
    """Validate and sanitize customer information."""

    cid = str(record.get("cid", "")).strip().upper()
    name = str(record.get("name", "")).strip()
    email = str(record.get("email", "")).strip().lower()
    pin = str(record.get("pin", "")).strip()
    spend = str(record.get("spend", "")).strip()

    if not re.fullmatch(r"C[0-9]{3}", cid):
        raise ValueError("Invalid Customer ID")

    if not re.fullmatch(r"[0-9]{6}", pin):
        raise ValueError("Invalid Pincode")

    if not name:
        raise ValueError("Customer name is required")

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        raise ValueError("Invalid Email")

    try:
        spend = float(spend)
    except ValueError:
        raise ValueError("Spend must be numeric")

    if spend < 0:
        raise ValueError("Negative spend is not allowed")

    return {
        "cid": cid,
        "name": html.escape(name),
        "email": email,
        "pin": pin,
        "spend": spend
    }
