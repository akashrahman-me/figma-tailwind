from lib.classes_gen.theme_mixer import theme_mixer
from lib.utils.convert_unit import  convert_unit
from lib.utils.round_with_unit import round_with_unit
from lib.utils.compare_pixel import compare_pixel
import re

def get_spacing_class(value, prefix, theme_path, threshold = 0):
    if value == '0':
        value = '0px'

    theme = theme_mixer(theme_path)

    value = round_with_unit(value)
    spacing_lists = theme['theme']['spacing']
    for spacing_key in spacing_lists:
        rem_value = convert_unit('16px', value, 'px')
        theme_value = convert_unit('16px', spacing_lists[spacing_key], 'px')
        if compare_pixel(float(rem_value.replace('px', '')), float(theme_value.replace('px', '')), threshold) :
            return f"{prefix}-{spacing_key}"

    return f"{prefix}-[{value}]"

def simplify_value(x):
    if all(y == x[0] for y in x):
        x = [x[0]]

    elif len(x) == 4:
        if x[0] == x[2] and x[1] == x[3]:
            x = [x[0], x[1]]
        elif x[1] == x[3]:
            x = [x[0], x[1], x[2]]

    return x


def spacing_class(padding_value, theme_path, top_prefix = 'p', threshold = 0, seperator = ""):
    result = ""
    padding_value = padding_value.split(' ')
    padding_value = simplify_value(padding_value)
    n = len(padding_value)
    
    prefixes = {0: f"{top_prefix}{seperator}t", 1: f"{top_prefix}{seperator}r", 2: f"{top_prefix}{seperator}b", 3: f"{top_prefix}{seperator}l"}
    for i in range(n):
        value = padding_value[i]
        prefix = prefixes[i]

        if n == 1:
            prefix = top_prefix

        elif n == 2:
            prefix = f"{top_prefix}{seperator}y" if i == 0 else f"{top_prefix}{seperator}x"

        elif n == 3:
            prefix = f"{top_prefix}{seperator}x" if i == 1 else prefix
        spacing_class_name = get_spacing_class(value, prefix, theme_path, threshold)

        result += f"{spacing_class_name} "
        
    result = result.strip()
    return result
