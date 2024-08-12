def get_font_style_class_from_font_style_value(font_style_value):
    if font_style_value == 'normal':
        return 'font-normal'
    elif font_style_value == 'italic':
        return 'font-italic'
    else:
        return ''
