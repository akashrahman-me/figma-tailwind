def convert_to_six_digit_hex_color(color):
    isHex = ""
        
    if color[0] == "#":
        isHex = "#"
        color = color[1:]

    if len(color) == 3:
        color = color[0]*2 + color[1]*2 + color[2]*2

    return isHex + color
