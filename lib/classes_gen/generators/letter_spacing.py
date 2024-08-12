from lib.classes_gen.helper.combined_config import combined_config, config, theme_colors
from lib.utils.round_with_unit import round_with_unit
from lib.classes_gen.compare_typography import compare_typography
from lib.utils.format_length import format_length
from lib.utils.convert_unit import  convert_unit

def get_letter_spacing_class_from_letter_spacing_value(letter_spacing_value, font_size_value):
    font_size_keys = list(combined_config['theme']['fontSize'].keys())

    for font_size in font_size_keys:
        theme_font_size = combined_config['theme']['fontSize'][font_size][0]
        if round_with_unit(theme_font_size) == round_with_unit(font_size_value):
            if 'letterSpacing' in combined_config['theme']['fontSize'][font_size][1]:
                theme_letter_spacing = combined_config['theme']['fontSize'][font_size][1]['letterSpacing']
                if convert_unit(font_size_value, theme_letter_spacing, 'px') == convert_unit(font_size_value, letter_spacing_value, 'px'):
                    return ''
                else:
                    if theme_letter_spacing and letter_spacing_value in ['normal', 'none', 'inherit']:
                        return "tracking-normal"
            elif letter_spacing_value in ['normal', 'none', 'inherit']:
                return ''
    return f'tracking-[{format_length(convert_unit(font_size_value, letter_spacing_value, "em"), 4)}]'
