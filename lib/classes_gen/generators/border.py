from lib.classes_gen.helper.combined_config import combined_config
import re
from lib.classes_gen.generators.color import color_class

def border_class(border_value):
    result = ""
    pattern = r"(?P<width>\d+px)\s*(?P<style>solid|outline|dashed|dotted)?\s*(?P<color>#[0-9A-Fa-f]{3,6})"

    try:
        match = re.search(pattern, border_value)

        if match:
            width = match.group("width")
            style = match.group("style")
            color = match.group("color")

            border_width = border_width_class(width)
            border_style = f"border-{style}" if style is not None else ""
            border_color = border_color_class(color)
            
            result = f"{border_width} {border_color}"
            if(style and style != "solid"):
                result += f" {border_style}"

        else:
            result =  f"border-[{border_value}]"
        return result
    except  IndexError:
        return ""

def border_width_class(border_width_value):
    theme = [combined_config['theme']['extend'].get('borderWidth', {}), combined_config['theme']['borderWidth']]

    for border_widths in theme:
        for border_width_key in border_widths:
            if border_widths[border_width_key] == border_width_value:
                if border_width_key == "DEFAULT":
                    return "border"
                else:
                    return f"border-{border_width_key}"

    # If no matching border width is found, return an arbitrary border width class.
    return f"border-[{border_width_value}]"

def border_color_class(border_color_value):
    return color_class(border_color_value, 'border')
