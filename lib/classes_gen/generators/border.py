from lib.classes_gen.helper.combined_config import combined_config, theme_colors
from lib.utils.round_with_unit import round_with_unit
from lib.classes_gen.compare_typography import compare_typography
from lib.utils.format_length import format_length
from lib.utils.convert_unit import  convert_unit
from lib.classes_gen.convert_to_six_digit_hex_color import  convert_to_six_digit_hex_color
import re

def border_class(border_value):
    result = ""
    try:
        border_match = re.match(r"(\d+\.?\d+px) (solid|outline|dashed|dotted) (\#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)", border_value)

        if border_match:
            border_width_value = border_match.group(1)
            border_style_value = border_match.group(2)
            border_color_value = border_match.group(3)
            border_width = get_border_width_class_from_border_width_value(
                border_width_value
            )
            border_style = f"border-{border_style_value}"
            border_color = get_border_color_class_from_border_color_value(
                border_color_value
            )
            result = f"{border_width} {border_color}"
            if(border_style_value !='solid'):
                result += f" {border_style}"

        else:
            result =  f"border-[{border_value}]"
        return result
    except  IndexError:
        return ""

def get_border_width_class_from_border_width_value(border_width_value):

    border_width_keys = list(combined_config['theme']['borderWidth'].keys())

    for border_width in border_width_keys:
        if combined_config['theme']['borderWidth'][border_width] == border_width_value:
            if border_width == "DEFAULT":
                return "border"
            else:
                return f"border-{border_width}"

    # If no matching border width is found, return an arbitrary border width class.
    return f"border-[{border_width_value}]"

def get_border_color_class_from_border_color_value(border_color_value):
    color_configs = [theme_colors,
                     combined_config['theme']['extend']['colors']]
    border_color_value = convert_to_six_digit_hex_color(border_color_value)

    for config in color_configs:
        for color in config:
            if isinstance(config[color], str):
                if convert_to_six_digit_hex_color(config[color]).lower() == border_color_value.lower():
                    return f'border-{color}'
            elif isinstance(config[color], dict):
                for variant in config[color]:
                    color_config = config[color][variant]
                    if (isinstance(color_config, str) and
                            convert_to_six_digit_hex_color(color_config).lower() == border_color_value.lower()):
                        if variant == 'DEFAULT':
                            return f'border-{color}'
                        else:
                            return f'border-{color}-{variant}'
    return f'border-[{border_color_value}]'
