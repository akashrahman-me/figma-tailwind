from collections import defaultdict
from collections import Counter
import re
from lib.utils.round_with_unit import round_with_unit
from lib.utils.format_length import format_length
from lib.utils.convert_unit import convert_unit
from lib.utils.filter_selected_keys import filter_selected_keys
from lib.utils.get_number import get_number
from lib.echo import echo
import json



def tailwind_typography(css_object):
    css_object = filter_selected_keys(css_object, ["fontSize", "letterSpacing", "lineHeight"])

    grouped = {}
    for obj in css_object:
        
        key = int(round(get_number(obj.get('fontSize', '0'))))
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(obj)

    unique_data = []
    seen_font_sizes = set()

    for group in grouped.values():
        line_height_counter = Counter()
        letter_spacing_counter = Counter()

        for obj in group:
            if 'lineHeight' in obj:
                lh_value = round_with_unit(obj['lineHeight'])
                line_height_counter[lh_value] += 1

            if 'letterSpacing' in obj:
                ls_value = format_length(obj['letterSpacing'])
                letter_spacing_counter[ls_value] += 1

        # print(line_height_counter)

        max_line_height = line_height_counter.most_common(1)[0][0] if line_height_counter else None
        max_letter_spacing = letter_spacing_counter.most_common(1)[0][0] if letter_spacing_counter else None

        for obj in group:
            is_line_height_valid = ('lineHeight' not in obj) or ('lineHeight' in obj and round_with_unit(obj['lineHeight']) == max_line_height)
            is_letter_spacing_valid = ('letterSpacing' not in obj) or (format_length(obj['letterSpacing']) == max_letter_spacing)

            if not (is_line_height_valid and is_letter_spacing_valid):
                continue

            font_size = int(round(get_number(obj.get('fontSize', '0'))))
            if font_size in seen_font_sizes:
                continue

            if max_line_height:
                obj['lineHeight'] = max_line_height

            if max_letter_spacing:
                obj['letterSpacing'] = max_letter_spacing

            unique_data.append(obj)
            seen_font_sizes.add(font_size)

    unique_data = sorted(unique_data, key=lambda x: float(x['fontSize'][:-2]))

    result = {}
    keys = ['xs', 'sm', 'md', 'base', 'lg', 'xl']
    for index, obj in enumerate(unique_data):
        key = keys[index] if index < len(keys) else f'{index - 3}xl'

        line_height = None
        if 'lineHeight' in obj: 
            line_height = obj['lineHeight']
        
        letter_spacing = None
        if 'letterSpacing' in obj:
            letter_spacing = obj['letterSpacing']

        second_arg = {}

        if line_height is not None:
            second_arg['lineHeight'] = format_length(convert_unit(obj["fontSize"], line_height, 'em'))
        if letter_spacing is not None:
            second_arg['letterSpacing'] = format_length(convert_unit(obj["fontSize"], letter_spacing, 'em'), 3)
        result[key] = [
            round_with_unit(obj['fontSize']),
            second_arg
        ]

    return result
