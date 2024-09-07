def justify_content_class(param, theme_path):
    params = [
        ['normal', 'justify-normal'],
        ['flex-start', 'justify-start'],
        ['flex-end', 'justify-end'],
        ['center', 'justify-center'],
        ['space-between', 'justify-between'],
        ['space-around', 'justify-around'],
        ['space-evenly', 'justify-evenly'],
        ['stretch', 'justify-stretch'],
    ]

    for pair in params:
        value, key = pair
        if param == value:
            return key

    return ""
