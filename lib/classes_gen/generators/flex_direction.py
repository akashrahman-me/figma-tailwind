def flex_direction_class(param, theme_path):
    params = [
        ['row', 'flex-row'],
        ['row-reverse', 'flex-row-reverse'],
        ['column', 'flex-col'],
        ['column-reverse', 'flex-col-reverse'],
    ]

    for pair in params:
        value, key = pair
        if param == value:
            return key

    return ""
