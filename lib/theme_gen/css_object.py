import re

def css_object(plaintext):
    text = plaintext
    text = re.sub(r'^//styleName.*$', "", text, flags=re.MULTILINE)

    blocks = text.strip().split('\n\n')

    css_object = []
    for block in blocks:
        lines = block.split('\n')

        typography = {}
        for line in lines:
            property, value = re.split(r':\s*', line)
            property = re.sub(r'-([a-z])', lambda m: m.group(1).upper(), property)
            value = value.replace(';', '')
            typography[property] = value

        css_object.append(typography)

    return css_object
