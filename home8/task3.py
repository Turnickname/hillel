import re

def validate_full_name(full_name):
    pattern = r'^[A-Za-zА-Яа-яЁё]{2,20}( [A-Za-zА-Яа-яЁё]{2,20}){2}$'
    return bool(re.match(pattern, full_name))
