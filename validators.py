import re
from datetime import datetime

def validate_field(value):
    if validate_date(value):
        return "date"
    elif validate_phone(value):
        return "phone"
    elif validate_email(value):
        return "email"
    else:
        return "text"

def validate_date(value):
    date_formats = ["%d.%m.%Y", "%Y-%m-%d"]
    for fmt in date_formats:
        try:
            datetime.strptime(value, fmt)
            return True
        except ValueError:
            pass
    return False

def validate_phone(value):
    return bool(re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', value))

def validate_email(value):
    return bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value))