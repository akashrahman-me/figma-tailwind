from lib.classes_gen.helper.combined_config import combined_config, theme_colors
from lib.utils.round_with_unit import round_with_unit
from lib.classes_gen.compare_typography import compare_typography
from lib.utils.format_length import format_length
from lib.utils.convert_unit import  convert_unit
from lib.classes_gen.format_box_shadow import format_box_shadow


def box_shadow_class(box_shadow_value):
    # Check the box shadow value against combinedConfig.theme.boxShadow
    for box_shadow in combined_config['theme']['boxShadow']:
        formatedThemeShadow = format_box_shadow(combined_config['theme']['boxShadow'][box_shadow])
        if format_box_shadow(box_shadow_value) == formatedThemeShadow:
            return f"shadow-{box_shadow}"  # Direct match

    # If no matching box shadow is found, return an arbitrary box shadow class.
    # Replace spaces with underscores
    return f"shadow-[{format_box_shadow(box_shadow_value).replace(' ', '_')}]"
