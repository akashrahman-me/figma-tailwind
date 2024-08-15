from lib.classes_gen.helper.combined_config import combined_config
from lib.utils.format_length import format_length
from lib.utils.convert_unit import  convert_unit


def get_spacing_class(value, prefix):
  if value == '0':
      value = '0px'

  spacing_lists = combined_config['theme']['spacing']
  for spacing_key in spacing_lists:
    rem_value = format_length(convert_unit('16px', value, 'rem'), 3)
    theme_value = format_length(convert_unit('16px', spacing_lists[spacing_key], 'rem'), 3)
    if theme_value == rem_value:
        return f"{prefix}-{spacing_key}"

  return f"{prefix}-[{value}]"

def spacing_class(padding_value, top_prefix = 'p'):    
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
            prefix = f"{top_prefix}x" if i == 0 else f"{top_prefix}y"

        elif n == 3:
            prefix = f"{top_prefix}x" if i == 1 else prefix
        spacing_class_name = get_spacing_class(value, prefix)

        result += f"{spacing_class_name} "
    result = result.strip()

    return result
