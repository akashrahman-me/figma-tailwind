def align_self_class(param, theme_path):
    params = [
        ['auto', 'self-auto'],
        ['flex-start', 'self-start'],
        ['flex-end', 'self-end'],
        ['center', 'self-center'],
        ['baseline', 'self-baseline'],
        ['stretch', 'self-stretch']
    ]

    for pair in params:
        value, key = pair
        if param == value:
            return key

    return ""
