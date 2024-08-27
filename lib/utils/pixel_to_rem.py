from lib.utils.round_with_unit import round_with_unit

def pixel_to_rem(pixel_value):

    if 'rem' in pixel_value:
        return f"{round(float(pixel_value.replace('rem', '')), 1)}rem"

    if 'px' not in pixel_value:
        return pixel_value
    
    
    numeric_value = float(pixel_value.replace("px", ""))

    # Convert pixel to rem (assuming 1rem = 16px)
    rem_value = numeric_value / 16

    return f"{round(rem_value, 1)}rem"
