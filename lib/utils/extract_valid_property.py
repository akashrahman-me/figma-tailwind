import re

def extract_valid_property(string):
    # Define a regular expression pattern to match the color property
    pattern = r'var\(.*?,\s*(#(?:[0-9a-fA-F]{3}){1,2})\s*\);'

    # Use re.sub to replace the matched pattern with the hex color value
    updated_string = re.sub(pattern, r'\1;', string)

    return updated_string
