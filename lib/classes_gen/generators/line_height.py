from lib.classes_gen.helper.combined_config import combined_config, config, theme_colors
from lib.utils.round_with_unit import round_with_unit
from lib.classes_gen.compare_typography import compare_typography
from lib.utils.format_length import format_length
from lib.utils.convert_unit import  convert_unit


def get_line_height_class_from_line_height_value(line_height_value, font_size_value):
    font_size_keys = list(combined_config['theme']['fontSize'].keys())

    for font_size in font_size_keys:
        theme_font_size = combined_config['theme']['fontSize'][font_size][0]
        if round_with_unit(theme_font_size) == round_with_unit(font_size_value):
            if 'lineHeight' in combined_config['theme']['fontSize'][font_size][1]:
                theme_line_height = combined_config['theme']['fontSize'][font_size][1]['lineHeight']
                
                if round_with_unit(convert_unit(font_size_value, theme_line_height, 'px')) == round_with_unit(convert_unit(font_size_value, line_height_value, 'px')):
                    return ''
                else:
                    if theme_line_height and line_height_value in ['normal', 'none', 'inherit']:
                        return "leading-normal"
            elif line_height_value in ['normal', 'none']:
                return ''

    return f'leading-[{format_length(convert_unit(font_size_value, line_height_value, "em"), 3)}]'
