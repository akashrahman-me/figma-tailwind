def display_class(display_value, theme_path):

    if display_value == 'none':
        return 'hidden'

    return display_value.lower().replace(' ', '-')
