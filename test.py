import cssutils

def simplify_css_value(value):
    properties = f"padding: {value};"
    sheet = cssutils.parseStyle(properties)
    simplified_value = sheet['padding']
    return simplified_value

print(simplify_css_value('12px 12px 12px 12px'))  # Outputs: '10px'
