import re
from lib.utils.format_length import format_length 

def calc_typo(value, base_font_size):
    match = re.search(r"([0-9.]+)([a-zA-Z%]+)?", value)
    if not match:
        return None

    number = float(match.group(1))
    unit = match.group(2) or "px"  # default to px if no unit is given

    root_font_size = 16  # assumed root font size for rem

    if unit == "em":
        return number * base_font_size
    elif unit == "rem":
        return number * root_font_size
    elif unit == "px":
        return number
    elif unit == "%":
        return (number / 100) * base_font_size
    elif unit == "pt":
        return number * (1 / 0.75)  # 1pt = 1.333px
    elif unit == "pc":
        return number * 16  # 1pc = 12pt = 16px
    elif unit == "ex":
        return number * base_font_size * 0.5  # 1ex is approximately half of 1em
    elif unit == "ch":
        return number * base_font_size * 0.5  # 1ch is approximately half of 1em
    else:
        return None  # or raise error, depending on your requirements


def compare_typography(font_size_with_unit, typography, callback=None):
    ignored = ["normal", "inherit", "none"]
    if typography[0] or typography[1] in ignored:
        return typography[0] == typography[1]

    font_size_match = re.search(r"([0-9.]+)([a-zA-Z%]+)?", font_size_with_unit)
    if not font_size_match:
        return None

    font_size = float(font_size_match.group(1))
    font_size_unit = font_size_match.group(
        2) or "px"  # default to px if no unit is given
    # second argument is ignored
    base_font_size = calc_typo(f"{font_size}{font_size_unit}", 1)

    typo1 = calc_typo(typography[0], base_font_size)
    typo2 = calc_typo(typography[1], base_font_size)

    # Compare and return in pixel
    if callback:
        return callback(typo1, typo2)
    else:
        # Assuming 'format_length' function exists in Python
        return format_length(f"{typo1}px") == format_length(f"{typo2}px")
