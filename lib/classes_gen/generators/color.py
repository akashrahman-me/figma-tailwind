from lib.classes_gen.helper.combined_config import combined_config, config, theme_colors
from lib.classes_gen.convert_to_six_digit_hex_color import convert_to_six_digit_hex_color

def get_color_class_from_color_value(color_value):
    # check in both theme.colors and theme.extend.colors
    color_configs = [theme_colors, combined_config['theme']['extend']['colors']]

    # convert the input color value to a six digit hex color
    color_value = convert_to_six_digit_hex_color(color_value)

    for config in color_configs:
        for color in config:
            if isinstance(config[color], str):
                if convert_to_six_digit_hex_color(config[color]).lower() == color_value.lower():
                    return f"text-{color}"  # Direct color match
            elif isinstance(config[color], dict):
                for variant in config[color]:
                    color_config = config[color][variant]
                    if isinstance(color_config, str) and convert_to_six_digit_hex_color(color_config).lower() == color_value.lower():
                        if variant == "DEFAULT":
                            # If it's the default variant, we only need the color key, not the variant.
                            return f"text-{color}"
                        else:
                            # If it's not the default variant, we need both the color key and the variant.
                            return f"text-{color}-{variant}"

    # If no matching color is found, return an arbitrary color class.
    # This means the color value isn't defined in the Tailwind config and you want to use an arbitrary color.
    return f"text-[{color_value.replace(' ', '_')}]"
