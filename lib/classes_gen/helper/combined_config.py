from lib.classes_gen.tailwind_config_serialize import tailwind_config_serialize
from lib.utils.extract_valid_property import extract_valid_property
import json
import css_parser

with open('config.json', 'r') as file:
    config = json.load(file)

with open(config['tailwind_config'], 'r') as file:
    tailwind_config = tailwind_config_serialize(file.read())

with open('storage/tailwind_default_theme.json', 'r') as file:
    default_theme = json.load(file)

with open('storage/theme_colors.json', 'r') as file:
    theme_colors = json.load(file)

with open(config['css_parser_URI'], 'r') as file:
    css_string = file.read()
    css_string = extract_valid_property(css_string)

combined_config = {
    **tailwind_config,
    "theme": {
        **default_theme,
        **tailwind_config.get("theme", {}),
        "extend": {
            **default_theme.get("extend", {}),
            **tailwind_config.get("theme", {}).get("extend", {}),
        },
    },
}


style = css_parser.css.CSSStyleDeclaration()
