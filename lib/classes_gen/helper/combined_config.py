from lib.classes_gen.tailwind_config_serialize import tailwind_config_serialize
from lib.utils.extract_valid_property import extract_valid_property
import json
import css_parser
from lib.utils.relevant_styles import relevant_style
from lib.echo import echo

config_path, relevant, css_string = relevant_style()

with open(config_path, 'r') as file:
    tailwind_config = tailwind_config_serialize(file.read())

with open('storage/tailwind_default_theme.json', 'r') as file:
    default_theme = json.load(file)

with open('storage/theme_colors.json', 'r') as file:
    theme_colors = json.load(file)

css_string = extract_valid_property(css_string)

combined_config = {
    **tailwind_config,
    "theme": {
        **default_theme,
        **tailwind_config.get("theme", {}),
        "extend": {
            **tailwind_config.get("theme", {}).get("extend", {}),
        },
    },
}

echo(combined_config, "json")


style = css_parser.css.CSSStyleDeclaration()
