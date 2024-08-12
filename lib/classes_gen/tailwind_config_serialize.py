import re
import json

def js_to_json(js_string):
    pattern = r'([\{\s,])(\w+)(:)'
    json_string = re.sub(pattern, r'\1"\2"\3', js_string)
    json_string = re.sub(r',\s*\.\.\.[\w\.]*', '', json_string)
    json_string = json_string.replace("`", "\"")
    json_string = re.sub(r',\s*([\}\]])', r'\1', json_string)
    return json_string

# For the TypeScript Project
# const config: Config

# For the JavaScript Project
# module\.exports

def tailwind_config_serialize(tailwind_config):
    match = re.search(
        r"const config: Config\s=\s({.*?});", tailwind_config, re.DOTALL)
    if match:
        js_object_literal = match.group(1)
        our_json_data = js_to_json(js_object_literal)
        return json.loads(our_json_data)
