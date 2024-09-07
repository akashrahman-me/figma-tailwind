import re
import urllib.parse

def remove_occurrences(css_string):
    # Regular expression to find all occurrences of var(...) and replace with the fallback value
    pattern = r'var\([^,]+,\s*([^\)]+)\)'
    css_string = re.sub(pattern, r'\1', css_string)
    return urllib.parse.unquote(css_string)

def parse_config(value: str):
    lines = value.splitlines()

    theme_path = lines[0].strip()
    ignore_class = lines[1].strip()
    css_string = ''.join(lines[2:]).strip()

    css_string = remove_occurrences(css_string)


    return theme_path, ignore_class, css_string

