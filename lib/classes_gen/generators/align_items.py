def align_items_class(param, theme_path):
    params = [
        ['flex-start', 'items-start'],
        ['flex-end', 'items-end'],
        ['center', 'items-center'],
        ['baseline', 'items-baseline'],
        ['stretch', 'items-stretch']
    ]

    for pair in params:
        value, key = pair
        if param == value:
            return key

    return ""
