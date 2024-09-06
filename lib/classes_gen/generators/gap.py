from lib.classes_gen.generators.spacing import get_spacing_class, spacing_class

def gap_class(gap_value):
    return spacing_class(gap_value, 'gap', threshold=20, seperator='-')
