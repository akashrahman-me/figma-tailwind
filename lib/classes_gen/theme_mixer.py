from lib.classes_gen.tailwind_config_serialize import tailwind_config_serialize
import json

def theme_mixer(theme_path):
    with open(theme_path, 'r') as file:
        tailwind_config = tailwind_config_serialize(file.read())

    with open('../storage/tailwind_default_theme.json', 'r') as file:
        default_theme = json.load(file)

    return {
        **tailwind_config,
        "theme": {
            **default_theme,
            **tailwind_config.get("theme", {}),
            "extend": {
                **tailwind_config.get("theme", {}).get("extend", {}),
            },
        },
    }
