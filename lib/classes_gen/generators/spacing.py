from lib.classes_gen.helper.combined_config import combined_config
from lib.utils.format_length import format_length
from lib.utils.convert_unit import  convert_unit
from lib.utils.round_with_unit import round_with_unit
from lib.utils.compare_pixel import compare_pixel
import re


def get_spacing_class(value, prefix, threshold = 0):
  if value == '0':
      value = '0px'

  value = round_with_unit(value)
  spacing_lists = combined_config['theme']['spacing']
  for spacing_key in spacing_lists:
    rem_value = convert_unit('16px', value, 'px')
    theme_value = convert_unit('16px', spacing_lists[spacing_key], 'px')
    if compare_pixel(float(rem_value.replace('px', '')), float(theme_value.replace('px', '')), threshold) :
        return f"{prefix}-{spacing_key}"

  return f"{prefix}-[{value}]"


def simplify_properties(padding_str):
    # Initialize the dictionary with default values
    padding_dict = {'pt': None, 'pr': None, 'pb': None, 'pl': None}

    # Function to parse and normalize the value, handling units
    def parse_value(value):
        match = re.match(r'(\d+)(.*)', value)
        if match:
            return int(match.group(1)), match.group(2)  # Return numeric part and unit
        return value, ''

    # Parse the input string into the dictionary
    for part in padding_str.split():
        key, value = part.split('-')
        padding_dict[key] = parse_value(value)

    # Simplify the padding values
    py = None
    px = None

    if padding_dict['pt'] and padding_dict['pb'] and padding_dict['pt'] == padding_dict['pb']:
        py = f"py-{padding_dict['pt'][0]}{padding_dict['pt'][1]}"
        padding_dict['pt'] = None
        padding_dict['pb'] = None
    
    if padding_dict['pl'] and padding_dict['pr'] and padding_dict['pl'] == padding_dict['pr']:
        px = f"px-{padding_dict['pl'][0]}{padding_dict['pl'][1]}"
        padding_dict['pl'] = None
        padding_dict['pr'] = None

    # Prepare the final simplified string
    simplified_parts = []
    if py:
        simplified_parts.append(py)
    if px:
        simplified_parts.append(px)
    for key, value in padding_dict.items():
        if value is not None:
            simplified_parts.append(f"{key}-{value[0]}{value[1]}")

    return ' '.join(simplified_parts)


def spacing_class(padding_value, top_prefix = 'p', threshold = 0):    
    result = ""
    padding_value = padding_value.split(' ')
    n = len(padding_value)
    
    prefixes = {0: f"{top_prefix}t", 1: f"{top_prefix}r", 2: f"{top_prefix}b", 3: f"{top_prefix}l"}
    for i in range(n):
        value = padding_value[i]
        prefix = prefixes[i]

        if n == 1:
            prefix = top_prefix

        elif n == 2:
            prefix = f"{top_prefix}y" if i == 0 else f"{top_prefix}x"

        elif n == 3:
            prefix = f"{top_prefix}x" if i == 1 else prefix
        spacing_class_name = get_spacing_class(value, prefix, threshold)

        result += f"{spacing_class_name} "
        
    result = result.strip()
    print(result)
    result = simplify_properties(result)

    return result
