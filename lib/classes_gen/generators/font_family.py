from lib.classes_gen.helper.combined_config import combined_config
def get_font_family_class_from_font_family_value(font_family_value):
    if 'fontFamily' in  combined_config['theme']:
        path = combined_config['theme']['fontFamily']
    elif 'fontFamily' in  combined_config['theme']['extend']:
        path = combined_config['theme']['extend']['fontFamily']

    font_family_keys = list(path.keys())
    
    for font_family in font_family_keys:

        if f"'{font_family_value}'" in path[font_family]:
            return f'font-{font_family}'

    return f"font-{font_family_value.replace(' ', '_')}"
