import re
from lib.utils.round_with_unit import round_with_unit

def box_shadow_sizes(css_styles):
    # Initial size names
    sizes = ['sm', 'md', 'lg', 'xl']

    # Result object
    box_shadow_sizes = {}

    # Function to format the length values in the box-shadow string
    def format_box_shadow(box_shadow):
        if box_shadow is None:
            return None

        # Break down the box-shadow string into separate components
        components = re.split(r'([ ,])', box_shadow)

        # Format the length values
        for i in range(len(components)):
            # Format only if it's a length value
            if re.match(r'\d+(\.\d+)?px$', components[i]):
                components[i] = round_with_unit(components[i])

        # Put the box-shadow string back together
        return ''.join(components)

    # Iterate through each CSS style object
    for style in css_styles:
        # Format the box-shadow value
        box_shadow = format_box_shadow(style.get('boxShadow'))

        # Only add unique box shadows to the result
        if box_shadow not in box_shadow_sizes.values():
            # Generate size names after 'xl'
            if len(box_shadow_sizes) >= len(sizes):
                n = len(box_shadow_sizes) - len(sizes) + 2  # Starts at 2
                sizes.append(str(n) + 'xl')

            # Assign the box-shadow value to the corresponding size name
            box_shadow_sizes[sizes[len(box_shadow_sizes)]] = box_shadow

    return box_shadow_sizes
