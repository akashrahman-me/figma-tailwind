import re
from lib.classes_gen.theme_mixer import theme_mixer

def parse_object(value):
    pattern = r'(\w+)\(([^)]+)\)'
    matches = re.findall(pattern, value)
    return {key: value for key, value in matches}

def backdrop_filter_class(backdrop_filter_value, theme_path):
    theme = theme_mixer(theme_path)

    # Define a mapping of CSS filter functions to their respective theme configurations
    filter_keys = ['blur', 'brightness', 'opacity', 'contrast', 'grayscale', 'hue-rotate', 'invert', 'saturate', 'sepia']

    filter_config_map = {key: [theme['theme']['extend'].get(key, {}), theme['theme'].get(key, {})] for key in filter_keys}

    # Parse the input value
    styles = parse_object(backdrop_filter_value)

    result = ""

    # Loop through parsed styles and map them to corresponding config
    for key, value in styles.items():
        nf = True  # flag for "not found", used to decide whether to apply custom values in []

        # Check if the key (filter) exists in the config map
        if key in filter_config_map:
            # Get the corresponding configuration for the filter
            theme_values_list = filter_config_map[key]

            # Check through the theme values
            for theme_values in theme_values_list:
                for k, v in theme_values.items():
                    if value == v:
                        result += f"backdrop-{key}-{k} "
                        nf = False
                        break
                if not nf:  # Exit outer loop if a match is found
                    break

            # If no match is found, use the custom format
            if nf:
                result += f"backdrop-{key}-[{value}] "

    return result.strip()  # Remove any trailing spaces
