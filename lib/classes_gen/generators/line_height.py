from lib.classes_gen.helper.combined_config import combined_config
from lib.utils.round_with_unit import round_with_unit
from lib.utils.format_length import format_length
from lib.utils.convert_unit import  convert_unit
from lib.classes_gen.generators.font_size import font_size_class

def line_height_class(line_height_value, font_size_value):
    font_size_key = font_size_class(font_size_value, only_key = True)
    if not font_size_key:
        return ""
    
    font_variants = combined_config['theme']['fontSize'][font_size_key][1]

    if 'lineHeight' in font_variants:
        theme_line_height = font_variants['lineHeight']
        
        theme_line_height_px = convert_unit(font_size_value, theme_line_height, 'px')
        line_height_px = convert_unit(font_size_value, line_height_value, 'px')

        if round_with_unit(theme_line_height_px) == round_with_unit(line_height_px):
            return ''
        else:
            if line_height_value in ['normal', 'none', 'inherit']:
                return "leading-normal"
    elif line_height_value in ['normal', 'none', 'inherit']:
        return ''

    return f'leading-[{format_length(convert_unit(font_size_value, line_height_value, "em"), 3)}]'
