from lib.classes_gen.helper.combined_config import combined_config, config, theme_colors
from lib.utils.round_with_unit import round_with_unit
from lib.classes_gen.compare_typography import compare_typography
from lib.utils.format_length import format_length
from lib.utils.convert_unit import  convert_unit
from lib.utils.pixel_to_rem import pixel_to_rem

def get_border_radius_class_from_border_radius_value(border_radius_value):
    border_radius_keys = list(combined_config['theme']['borderRadius'].keys())

    # Convert pixel to rem for matching
    border_radius_value_rem = pixel_to_rem(border_radius_value)

    for border_radius in border_radius_keys:
        # Convert both to string to prevent type issues
        if str(combined_config['theme']['borderRadius'][border_radius]) == str(border_radius_value_rem):
            # if borderRadius is 'DEFAULT', just return 'rounded'
            if border_radius == "DEFAULT":
                return "rounded"
            else:
                return f"rounded-{border_radius}"

    return f"rounded-[{border_radius_value.replace(' ', '_')}]"
