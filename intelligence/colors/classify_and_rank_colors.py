import json
import webcolors
from collections import defaultdict
from intelligence.colors.color_group_name import color_group_name

def sort_hex(hex_array):
    hex_array.sort(
        key=lambda color: (int(color[1:3], 16) * 299 + int(color[3:5], 16) * 587 + int(color[5:7], 16) * 114) / 1000,
        reverse=True)
    return hex_array

def remove_duplicate_properties(dict_list, props):
    # Convert list of dictionaries to list of tuples
    tuple_list = [tuple((prop, d[prop]) for prop in props) for d in dict_list]

    # Convert list of tuples to set (removes duplicates) and back to list
    unique_tuples = list(set(tuple_list))

    # Convert back to list of dictionaries
    unique_dicts = [{prop: val for prop, val in tup} for tup in unique_tuples]

    return unique_dicts


def classify_and_rank_colors(colors):
    colors = remove_duplicate_properties(colors, ['color'])
    color_map = defaultdict(list)
    for color_obj in colors:
        color = color_obj['color']
        if not color.startswith('#'):
            try:
                color = webcolors.name_to_hex(color)
            except ValueError:
                continue
        color_map[color_group_name(color)].append(color)

    for color_group, hex_colors in color_map.items():
        color_map[color_group] = sort_hex(hex_colors)

    # Format the output
    output = {}
    for color_group, hex_colors in color_map.items():
        output[color_group] = {
            ((i + 1) * 50 if i == 0 else i * 100): hex_colors[i]
            for i in range(len(hex_colors))
        }

    return output
