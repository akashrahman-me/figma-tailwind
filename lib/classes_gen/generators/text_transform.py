def text_transform_class(text_transform_value, theme_path):
    text_transform_values = [
        ['uppercase', 'uppercase'],
        ['lowercase', 'lowercase'],
        ['capitalize', 'capitalize'],
        ['none', 'normal-case']
    ]

    for pair in text_transform_values:
        if text_transform_value == pair[0]:
            return f'text-{pair[1]}'

    return f"text-{text_transform_value.replace(' ', '_')}"
