from lib.classes_gen.helper.combined_config import combined_config
from lib.utils.format_length import format_length
from lib.utils.convert_unit import convert_unit
from lib.classes_gen.generators.font_size import font_size_class

def letter_spacing_class(letter_spacing_value, font_size_value):
    font_size_key = font_size_class(font_size_value, only_key = True)
    if not font_size_key:
        return ""
    
    font_variants = combined_config['theme']['fontSize'][font_size_key][1]
    
    if 'letterSpacing' in font_variants:
        theme_letter_spacing = font_variants['letterSpacing']

        theme_letter_spacing_px = convert_unit(font_size_value, theme_letter_spacing, 'px')
        letter_spacing_px = convert_unit(font_size_value, letter_spacing_value, 'px')

        if theme_letter_spacing_px == letter_spacing_px:
            return ''
        else:
            if letter_spacing_value in ['normal', 'none', 'inherit']:
                return "tracking-normal"
    elif letter_spacing_value in ['normal', 'none', 'inherit']:
        return ''
    
    return f'tracking-[{format_length(convert_unit(font_size_value, letter_spacing_value, "em"), 4)}]'
