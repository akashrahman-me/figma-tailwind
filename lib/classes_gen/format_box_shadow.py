import re
from lib.utils.round_with_unit import round_with_unit

def format_box_shadow(box_shadow):
    if box_shadow is None:
        return None

    # Break down the box-shadow string into separate components
    components = re.split(r'([ ,])', box_shadow)

    # Format the length values
    for i in range(len(components)):
        # Format only if it's a length value
        if re.match(r"^\d+(\.\d+)?px$", components[i]):
            # assuming round_with_unit is defined
            components[i] = round_with_unit(components[i])

    # Put the box-shadow string back together
    return "".join(components)
