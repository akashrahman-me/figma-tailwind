def font_style_class(font_style_value, theme_path):
    if font_style_value == 'normal':
        return 'font-normal'
    elif font_style_value == 'italic':
        return 'font-italic'
    else:
        return ''
