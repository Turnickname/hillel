import re

def validate_home_phone(phone_number):
    pattern = r'^\d{1,15}$'
    return bool(re.match(pattern, phone_number))
