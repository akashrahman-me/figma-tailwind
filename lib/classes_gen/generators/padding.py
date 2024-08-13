from lib.classes_gen.helper.combined_config import combined_config, theme_colors
from lib.utils.round_with_unit import round_with_unit
from lib.classes_gen.compare_typography import compare_typography
from lib.utils.format_length import format_length
from lib.utils.convert_unit import  convert_unit
from lib.utils.pixel_to_rem import pixel_to_rem


def get_spacing_class(value, prefix):
  spacing_lists = list(combined_config['theme']['spacing'].keys())
  for spacing in spacing_lists:
    rem_value = format_length(convert_unit('16px', value, 'rem'), 3)
    if str(combined_config['theme']['spacing'][spacing]) == (rem_value):
        return f"{prefix}-{spacing}"

  return f"{prefix}-[{value}]"

def padding_class(padding_value):
    result = ""
    padding_value = padding_value.split(' ')
    n = len(padding_value)
    prefixes = {0: "pt", 1: "pr", 2: "pb", 3: "pl"}
    for i in range(n):

        value = padding_value[i]
        prefix = prefixes[i]

        if n == 1:
            prefix = "p"

        elif n == 2:
            prefix = "px" if i == 0 else "py"

        elif n == 3:
            prefix = "px" if i == 1 else prefix
        spacing_class = get_spacing_class(value, prefix)

        result += f"{spacing_class} "
    result = result.strip()

    return result.replace(' ', '_')
