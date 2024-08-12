def pixel_to_rem(pixel_value):
    # Remove 'px' from the value and convert to number
    numeric_value = int(pixel_value.replace("px", ""))

    # Convert pixel to rem (assuming 1rem = 16px)
    rem_value = numeric_value / 16

    return f"{rem_value}rem"
