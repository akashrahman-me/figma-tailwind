from lib.classes_gen.generators.backdrop_filter import backdrop_filter_class


def filter_class(value, theme_path):
    return backdrop_filter_class(value, theme_path, '')[1:]