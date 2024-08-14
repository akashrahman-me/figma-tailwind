import cssutils

def expand_padding(padding_value):
    values = padding_value.split()

    if len(values) == 1:
        return values[0], values[0], values[0], values[0]
    elif len(values) == 2:
        return values[0], values[1], values[0], values[1]
    elif len(values) == 3:
        return values[0], values[1], values[2], values[1]
    elif len(values) == 4:
        return values[0], values[1], values[2], values[3]
    else:
        raise ValueError("Invalid padding shorthand")


padding_top, padding_right, padding_bottom, padding_left = expand_padding('10px 20px 12px')

from PIL import ImageColor
color = ImageColor.getcolor("rgb(255, 200, 255)", "RGB")
print(color)


# print("Padding top:", padding_top)
# print("Padding right:", padding_right)
# print("Padding bottom:", padding_bottom)
# print("Padding left:", padding_left)


