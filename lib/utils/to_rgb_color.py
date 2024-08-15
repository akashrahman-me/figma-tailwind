from PIL import ImageColor

def to_rgb_color(color_value: str):
   if not isinstance(color_value, str):
        raise TypeError("color_value must be a string")
   try:
      return ImageColor.getcolor(color_value, "RGB")
   except ValueError:
      return None
