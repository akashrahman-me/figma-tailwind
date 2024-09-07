from lib.classes_gen.generators.spacing import spacing_class

def padding_class(padding_value, theme_path):
    return spacing_class(padding_value, theme_path, 'p', threshold=20)
