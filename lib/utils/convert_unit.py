import re

def calc_line_height(value, base_font_size):
    match = re.search(r"(-?[0-9.]+)([a-zA-Z%]+)?", value)

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


def convert_to_unit(px_value, unit, base_font_size_px):
    root_font_size = 16  # assumed root font size for rem

    if unit == "em":
        return str(px_value / base_font_size_px) + "em"
    elif unit == "rem":
        return str(px_value / root_font_size) + "rem"
    elif unit == "px":
        return str(px_value) + "px"
    elif unit == "%":
        return str((px_value / base_font_size_px) * 100) + "%"
    elif unit == "pt":
        return str(px_value * 0.75) + "pt"  # 1pt = 0.75px
    elif unit == "pc":
        return str(px_value / 16) + "pc"  # 1pc = 12pt = 16px
    elif unit == "ex":
        # 1ex is approximately half of 1em
        return str(px_value / (base_font_size_px * 0.5)) + "ex"
    elif unit == "ch":
        # 1ch is approximately half of 1em
        return str(px_value / (base_font_size_px * 0.5)) + "ch"
    else:
        return None  # or raise error, depending on your requirements


def convert_unit(font_size_with_unit, target_size_with_unit, target_unit):
    ignored = ["normal", "inherit", "none"]
    if target_size_with_unit in ignored:
        return target_size_with_unit

    # Convert the base font size to px
    base_font_size_px = calc_line_height(font_size_with_unit, 1)

    # Convert the target size to px
    target_size_px = calc_line_height(target_size_with_unit, base_font_size_px)

    # Convert the target size from px to the target unit
    return convert_to_unit(target_size_px, target_unit, base_font_size_px)