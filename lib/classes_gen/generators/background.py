from lib.classes_gen.helper.combined_config import combined_config, theme_colors
from PIL import ImageColor

def background_class(color_value):
    # Check in both theme.colors and theme.extend.colors
    theme = [theme_colors, combined_config['theme']['extend'].get('colors', {})]

    color_value = ImageColor.getcolor(color_value, "RGB")

    for colors in theme:
        for color_key in colors:
            if color_key in ['inherit', 'current', 'transparent']:
                continue

            if isinstance(colors[color_key], str):
                if ImageColor.getcolor(colors[color_key], "RGB") == color_value:
                    return f"bg-{color_key}" # Direct color match
                
            elif isinstance(colors[color_key], dict):
                for variant in colors[color_key]:
                    color_config = colors[color_key][variant]
                    if ImageColor.getcolor(color_config, "RGB") == color_value:
                        if variant == "DEFAULT":
                            return f"bg-{color_key}"
                        else:
                            return f"bg-{color_key}-{variant}"

    # If no matching color is found, return an arbitrary color class.
    return f"bg-[rgb{str(color_value).replace(' ', '_')}]"
