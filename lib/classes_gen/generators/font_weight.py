from lib.classes_gen.helper.combined_config import combined_config, config, theme_colors
from lib.utils.round_with_unit import round_with_unit
from lib.classes_gen.compare_typography import compare_typography
from lib.utils.format_length import format_length
from lib.utils.convert_unit import  convert_unit

def get_font_weight_class_from_font_weight_value(font_weight_value):
    weights = combined_config['theme'].get('fontWeight', {})

    for key, value in weights.items():
        if value == font_weight_value:
            return f'font-{key}'

    return f'font-[{font_weight_value}]'
