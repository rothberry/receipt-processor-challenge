from datetime import datetime


def validate_string(value):
    if not value or not isinstance(value, str):
        raise ValueError("Must be a non-empty string")
    return value.strip()


def validate_price(value):
    try:
        price = float(value)
        if price < 0:
            raise ValueError("Price cannot be negative")
        return price
    except (ValueError, TypeError):
        raise ValueError("Invalid price format")


def validate_date(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD")


def validate_time(value):
    try:
        return datetime.strptime(value, "%H:%M").time()
    except ValueError:
        raise ValueError("Invalid time format. Use HH:MM (24-hour format)")
