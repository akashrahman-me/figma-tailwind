from lib.classes_gen.generators.spacing import get_spacing_class

def gap_class(gap_value): 
    return get_spacing_class(gap_value, 'gap', threshold=20)   
    