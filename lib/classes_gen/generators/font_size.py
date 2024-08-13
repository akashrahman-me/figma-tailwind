from lib.classes_gen.helper.combined_config import combined_config
from lib.utils.round_with_unit import round_with_unit

def font_size_class(font_size_value, only_key = False):
    font_size_keys = list(combined_config['theme']['fontSize'].keys())

    for font_size_key in font_size_keys:
        theme_font_size = combined_config['theme']['fontSize'][font_size_key][0]
        if round_with_unit(theme_font_size) == round_with_unit(font_size_value):
            if only_key:
                return font_size_key
            return f'text-{font_size_key}'

    if only_key:
        return None
    return f'text-[{round_with_unit(font_size_value)}]'
