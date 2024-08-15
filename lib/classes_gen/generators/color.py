from lib.classes_gen.helper.combined_config import combined_config, theme_colors
from lib.utils.to_rgb_color import to_rgb_color

def color_class(color_value, prefix = 'text'):
    # Check in both theme.colors and theme.extend.colors
    theme = [theme_colors, combined_config['theme']['extend'].get('colors', {})]

    color_value = to_rgb_color(color_value)

    if color_value is None:
        return ""

    for colors in theme:
        for color_key in colors:
            if color_key in ['inherit', 'current', 'transparent']:
                continue

            if isinstance(colors[color_key], str):
                if to_rgb_color(colors[color_key]) == color_value:
                    return f"{prefix}-{color_key}" # Direct color match
                
            elif isinstance(colors[color_key], dict):
                for variant in colors[color_key]:
                    color_config = colors[color_key][variant]
                    if to_rgb_color(color_config) == color_value:
                        if variant == "DEFAULT":
                            return f"{prefix}-{color_key}"
                        else:
                            return f"{prefix}-{color_key}-{variant}"

    # If no matching color is found, return an arbitrary color class.
    return f"{prefix}-[rgb{str(color_value).replace(' ', '_')}]"
