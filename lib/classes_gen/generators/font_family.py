import re
from lib.classes_gen.theme_mixer import theme_mixer

def font_family_class(font_family_value, theme_path):
    theme = theme_mixer(theme_path)

    theme = [theme['theme']['extend'].get('fontFamily', {}), theme['theme']['fontFamily']]

    for font_families in theme:
        # Remove non-alphanumeric characters from the start and end of the string
        font_family_value = re.sub(r'^[^\w]+|[^\w]+$', '', font_family_value)
        font_key = font_family_value.replace(' ', '-').lower()
        
        if font_key in font_families:
            return f"font-{font_key}"
        
        
    return f"font-[{font_family_value.replace(' ', '_')}]"
