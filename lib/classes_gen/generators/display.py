from lib.classes_gen.generators.spacing import spacing_class

def display_class(display_value):

    if display_value == 'none':
        return 'hidden'

    return display_value.lower().replace(' ', '-')
