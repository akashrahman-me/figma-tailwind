from lib.classes_gen.generators.spacing import spacing_class

def gap_class(gap_value, theme_path):
    return spacing_class(gap_value, top_prefix = 'gap', theme_path = theme_path, threshold=20, seperator='-')

