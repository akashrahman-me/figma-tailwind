import re
from sys import prefix
from lib.classes_gen.generators.color import color_class
from lib.classes_gen.theme_mixer import theme_mixer
from lib.utils.compare_pixel import compare_pixel

def border_class(border_value, theme_path):
    result = ""
    pattern = r"(?P<width>\d*\.?\d+px)\s*(?P<style>solid|outline|dashed|dotted)?\s*(?P<color>#[0-9A-Fa-f]{3,6})"

    try:
        match = re.search(pattern, border_value)

        if match:
            width = match.group("width")
            style = match.group("style")
            color = match.group("color")

            border_width = border_width_class(width, theme_path)
            border_style = f"border-{style}" if style is not None else ""
            border_color = border_color_class(color, theme_path)
            
            result = f"{border_width} {border_color}"
            if style and style != "solid":
                result += f" {border_style}"

        else:
            result =  f"border-[{border_value}]"
        return result
    except  IndexError:
        return ""

def border_width_class(border_width_value, theme_path):
    theme = theme_mixer(theme_path)
    set_border_width = [theme['theme']['extend'].get('borderWidth', {}), theme['theme']['borderWidth']]

    for border_widths in set_border_width:
        for border_width_key in border_widths:
            if compare_pixel(float(border_width_value.replace('px', '')), float(border_widths[border_width_key].replace('px', ''))):
                if border_width_key == "DEFAULT":
                    return "border"
                else:
                    return f"border-{border_width_key}"

    # If no matching border width is found, return an arbitrary border width class.
    return f"border-[{border_width_value}]"

def border_color_class(border_color_value, theme_path):
    return color_class(border_color_value, theme_path, 'border')
