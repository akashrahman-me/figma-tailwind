from lib.classes_gen.theme_mixer import theme_mixer

def opacity_class(opacity_value, theme_path):
    theme = theme_mixer(theme_path)
    theme = [theme['theme']['extend'].get('opacity', {}), theme['theme']['opacity']]

    for opacities in theme:
        for key, value in opacities.items():
            if value == opacity_value:
                return f'opacity-{key}'
 
    return f'opacity-[{opacity_value}]'
