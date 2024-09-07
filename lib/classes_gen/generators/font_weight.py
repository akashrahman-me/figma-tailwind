from lib.classes_gen.theme_mixer import theme_mixer


def font_weight_class(font_weight_value, theme_path):
    theme = theme_mixer(theme_path)
    theme = [theme['theme']['extend'].get('fontWeight', {}), theme['theme']['fontWeight']]

    for weights in theme:
        for key, value in weights.items():
            if value == font_weight_value:
                return f'font-{key}'

    return f'font-[{font_weight_value}]'
