from lib.classes_gen.helper.combined_config import combined_config
from lib.utils.pixel_to_rem import pixel_to_rem

def border_radius_class(border_radius_value):
    theme = [combined_config['theme']['borderRadius'], \
            combined_config['theme']['extend'].get('borderRadius', {})]

    if border_radius_value == '0':
        border_radius_value = '0px'

    # Convert pixel to rem for matching
    border_radius_value_rem = pixel_to_rem(border_radius_value)
    for border_radiuses in theme:
        for border_redius_key in border_radiuses:
            if (pixel_to_rem(border_radiuses[border_redius_key])) == (border_radius_value_rem):
                if border_redius_key == "DEFAULT":
                    return "rounded"
                else:
                    return f"rounded-{border_redius_key}"

    return f"rounded-[{border_radius_value.replace(' ', '_')}]"
