from lib.classes_gen.helper.combined_config import combined_config, config, theme_colors
from lib.utils.round_with_unit import round_with_unit

def get_font_size_class_from_font_size_value(font_size_value, letter_spacing, line_height):
    font_size_keys = list(combined_config['theme']['fontSize'].keys())

    for font_size in font_size_keys:
        theme_font_size = combined_config['theme']['fontSize'][font_size][0]
        if round_with_unit(theme_font_size) == round_with_unit(font_size_value):
            font_data = combined_config['theme']['fontSize'][font_size][1]
            if font_data is not None:
                theme_LS = font_data.get('letterSpacing', None)
                theme_LH = font_data.get('lineHeight', None)
            else:
                theme_LS = None
                theme_LH = None

            result = f'text-{font_size}'

            if theme_LS and theme_LS != 'normal' and not letter_spacing:
                result += ' tracking-normal'
            if theme_LH and theme_LH != '1.2em' and not line_height:
                result += ' leading-none'
            return result

    return f'text-[{round_with_unit(font_size_value)}]'
