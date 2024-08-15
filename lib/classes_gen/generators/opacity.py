from lib.classes_gen.helper.combined_config import combined_config

def opacity_class(opacity_value):
    theme = [combined_config['theme']['extend'].get('opacity', {}), combined_config['theme']['opacity']]

    for opacities in theme:
        for key, value in opacities.items():
            if value == opacity_value:
                return f'opacity-{key}'
 
    return f'opacity-[{opacity_value}]'
