import cssutils
from lib.utils.to_rgb_color import to_rgb_color

def expand_padding(padding_value):
    values = padding_value.split()

    if len(values) == 1:
        return values[0], values[0], values[0], values[0]
    elif len(values) == 2:
        return values[0], values[1], values[0], values[1]
    elif len(values) == 3:
        return values[0], values[1], values[2], values[1]
    elif len(values) == 4:
        return values[0], values[1], values[2], values[3]
    else:
        raise ValueError("Invalid padding shorthand")


padding_top, padding_right, padding_bottom, padding_left = expand_padding('10px 20px 12px')


import tinycss2

def css_string_to_properties(css_string):
    parsed = tinycss2.parse_declaration_list(css_string)

    styles = {}
    for decl in parsed:
        if decl.type == 'declaration' and not decl.name.startswith('--'):
            # Reconstruct the value from the component list
            value = ''.join([token.serialize() for token in decl.value])
            styles = {**styles, decl.name: value.strip()}

    return styles

x = css_string_to_properties('padding: 10px 20px;')
print(x)

