def format_font_families(fonts):
    formatted_fonts = {}
    for font in fonts:
        name = font['name'].replace(' ', '-')
        font_name = name.replace('-', ' ')
        formatted_fonts[name.lower()] = [f"'{font_name}'", "...fontFamily.sans"]

    return formatted_fonts
