import numpy as np
from sklearn.metrics import pairwise_distances
import webcolors
import json

with open("../intelligence/colors/training_colors.json", "r") as f:
  colors = json.load(f)

def hex_to_rgb(color_hex):
    return webcolors.hex_to_rgb(color_hex)

def closest_color_keys(color_data, target_hexs):
    keys = []
    colors_rgb = []

    for key, color_hex in color_data.items():
        keys.append(key)
        colors_rgb.append(hex_to_rgb(color_hex))

    colors_rgb = np.array(colors_rgb)

    result = {}
    for target_hex in target_hexs:
        target_rgb = np.array(hex_to_rgb(target_hex))
        if len(colors_rgb) != 0:
            distances = pairwise_distances([target_rgb], colors_rgb, metric='euclidean')
            min_index = np.argmin(distances)

            # Add the closest key and original color to the result and remove it from the dataset
            result[keys[min_index]] = target_hex
            keys.pop(min_index)
            colors_rgb = np.delete(colors_rgb, min_index, axis=0)

    return result

def extract_keys_and_values(data):
    keys = list(data.keys())
    values = list(data.values())
    return keys, values

def serialize_colors(un_serialize_colors):
  result = {}

  for name, values in colors.items():
    un_serialize_values = un_serialize_colors.get(name)
    if un_serialize_values:
      serialized_values = closest_color_keys(values, list(un_serialize_values.values()))
      result[name] = serialized_values
      
  return result
