import re

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\\.[^@]+", email) is not None

def validate_phone(phone):
    return re.match(r"^[0-9\\-\\+\\(\\) ]{7,15}$", phone) is not None