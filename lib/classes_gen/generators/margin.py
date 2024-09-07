from lib.classes_gen.generators.spacing import spacing_class


def margin_class(margin_value, theme_path):
    return spacing_class(margin_value, 'm', threshold=20)
