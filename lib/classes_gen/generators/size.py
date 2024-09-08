from lib.classes_gen.generators.spacing import spacing_class, get_spacing_class

def width_class(width_value, theme_path):
    width_value = width_value.split(' ')[0]
    return get_spacing_class(width_value, 'w', theme_path, threshold=20)

def height_class(height_value, theme_path):
    height_value = height_value.split(' ')[0]
    return get_spacing_class(height_value, 'w', theme_path, threshold=20)