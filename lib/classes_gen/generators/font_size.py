from lib.classes_gen.helper.combined_config import combined_config
from lib.utils.round_with_unit import round_with_unit
from lib.utils.convert_unit import convert_unit

def font_size_class(font_size_value, only_key = False):
    theme = [combined_config['theme']['extend'].get('fontSize', {}), combined_config['theme']['fontSize']]

    for font_sizes in theme:
        for key, value in font_sizes.items():
            theme_font_size = value[0]
            theme_font_size = round_with_unit(convert_unit('16px', theme_font_size, 'px'))
            font_size_value = round_with_unit(convert_unit('16px', font_size_value, 'px'))
            if theme_font_size == font_size_value:
                if only_key:
                    return key
                return f'text-{key}'

    if only_key:
        return None
    return f'text-[{round_with_unit(font_size_value)}]'
