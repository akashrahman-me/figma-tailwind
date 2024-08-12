# Import the re module
import re

# Define the regex pattern
# pattern = r"(#[0-9a-fA-F]{3,6}|rgba?\(\s*(\d{1,3}%?|\d{1,3}%?\s+\d{1,3}%?\s+\d{1,3}%?\s*\/\s*\d{1,3}%?)\s*,?\s*(\d{1,3}%?|\d{1,3}%?\s+\d{1,3}%?\s+\d{1,3}%?\s*\/\s*\d{1,3}%?)\s*,?\s*(\d{1,3}%?|\d{1,3}%?\s+\d{1,3}%?\s+\d{1,3}%?\s*\/\s*\d{1,3}%?)\s*,?\s*(\d?\.?\d+)?\)|hsla?\(\s*(\d{1,3}deg?|\d{1,3}deg?\s+\/?\s*\d{1,3}%?\s+\/?\s*\d{1,3}%?\s*\/\s*\d{1,3}%?)\s*,?\s*(\d{1,3}%?|\d{1,3}%?\s+\/?\s*\d{1,3}%?\s+\/?\s*\d{1,3}%?\s*\/\s*\d{1,3}%?)\s*,?\s*(\d{1,3}%?|\d{1,3}%?\s+\/?\s*\d{1,3}%?\s+\/?\s*\d{1,3}%?\s*\/\s*\d{1,3}%?)\s*,?\s*(\d?\.?\d+)?\))"


def is_valid_color(string):
    color_regex = r"(#(?:[0-9a-fA-F]{3}){1,2})|((?:rgb|hsl)a?\([^)]*\))"
    matches = re.findall(color_regex, string)

    result = ""
    try:
        result = list(matches[0])[0]
        if result == "":
            result = list(matches[0])[1]

        if result == "":
            result = None
    except IndexError:
        result = None

    return result
