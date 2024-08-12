from lib.classes_gen.helper.combined_config import combined_config, config, theme_colors
from lib.utils.round_with_unit import round_with_unit
from lib.classes_gen.compare_typography import compare_typography
from lib.utils.format_length import format_length
from lib.utils.convert_unit import  convert_unit
from lib.classes_gen.convert_to_six_digit_hex_color import  convert_to_six_digit_hex_color

def get_background_color_class_from_background_color_value(background_color_value):
    color_configs = [theme_colors, combined_config['theme']['extend']['colors']]

    background_color_value = convert_to_six_digit_hex_color(background_color_value)

    for config in color_configs:
        for color in config:
            if isinstance(config[color], str):
                if convert_to_six_digit_hex_color(config[color]).lower() == background_color_value.lower():
                    return f"bg-{color}"  # Direct color match
            elif isinstance(config[color], dict):
                for variant in config[color]:
                    color_config = config[color][variant]
                    if isinstance(color_config, str) and convert_to_six_digit_hex_color(color_config).lower() == background_color_value.lower():
                        if variant == "DEFAULT":
                            # If it's the default variant, we only need the color key, not the variant.
                            return f"bg-{color}"
                        else:
                            # If it's not the default variant, we need both the color key and the variant.
                            return f"bg-{color}-{variant}"

    return f"bg-[{background_color_value.replace(' ', '_')}]"
