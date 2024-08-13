from lib.classes_gen.helper.combined_config import combined_config
import re

def font_family_class(font_family_value):
    font_families = combined_config['theme'].get('extend', {}).get('fontFamily', []) \
        or combined_config['theme'].get('fontFamily', [])

    # Remove non-alphanumeric characters from the start and end of the string
    font_family_value = re.sub(r'^[^\w]+|[^\w]+$', '', font_family_value)
    
    font_key = font_family_value.replace(' ', '-').lower()
    if font_key in font_families:
        return f"font-{font_key}"
        
        
    return f"font-[{font_family_value.replace(' ', '_')}]"
