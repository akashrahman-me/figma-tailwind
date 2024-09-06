def format_font_families(fonts):
    formatted_fonts = {}
    for font in fonts:
        name = font['name'].replace(' ', '-')
        name = name.lower()
        formatted_fonts[name.lower()] = [f"var(--{name})", "'...fontFamily.sans'"]

    return formatted_fonts


