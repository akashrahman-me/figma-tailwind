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