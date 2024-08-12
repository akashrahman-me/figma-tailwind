import re

def get_number(string):
    pattern = r'\d+'

    matches = re.findall(pattern, string)
    result = int(''.join(matches))

    return result