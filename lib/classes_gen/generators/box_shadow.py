from lib.classes_gen.helper.combined_config import combined_config
from lib.classes_gen.format_box_shadow import format_box_shadow
import cssutils

def parse_box_shadow(css_text):
    sheet = cssutils.parseStyle(f"box-shadow: {css_text};")
    box_shadow = sheet.getPropertyValue("box-shadow")
    return box_shadow

def compare_box_shadows(shadow1, shadow2):
    parsed_shadow1 = parse_box_shadow(shadow1)
    parsed_shadow2 = parse_box_shadow(shadow2)
    return parsed_shadow1 == parsed_shadow2

def box_shadow_class(box_shadow_value):
    for box_shadow_key in combined_config['theme']['boxShadow']:
        theme_shadow = combined_config['theme']['boxShadow'][box_shadow_key]
        if compare_box_shadows(box_shadow_value, theme_shadow):
            return f"shadow-{box_shadow_key}"  # Direct match

    # If no matching box shadow is found, return an arbitrary box shadow class.
    # Replace spaces with underscores
    return f"shadow-[{format_box_shadow(box_shadow_value).replace(' ', '_')}]"
