from lib.classes_gen.helper.combined_config import combined_config

def font_weight_class(font_weight_value):
    weights = combined_config['theme'].get('fontWeight', {})

    for key, value in weights.items():
        if value == font_weight_value:
            return f'font-{key}'

    return f'font-[{font_weight_value}]'
