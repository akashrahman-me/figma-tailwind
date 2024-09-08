from lib.classes_gen.generators.spacing import get_spacing_class

def position_class(position_value, theme_path):
    return position_value.lower().replace(' ', '-')

def top_class(value, theme_path):
    return get_spacing_class(value, 'top', theme_path, threshold=20)

def bottom_class(value, theme_path):
    return get_spacing_class(value, 'bottom', theme_path, threshold=20)

def left_class(value, theme_path):
    return get_spacing_class(value, 'left', theme_path, threshold=20)

def right_class(value, theme_path):
    return get_spacing_class(value, 'right', theme_path, threshold=20)
