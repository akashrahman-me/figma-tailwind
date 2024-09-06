import re
import urllib.parse
import pyperclip

def relevant_style(path='../tailwind.txt'):
    # Read the file content
    with open(path, 'r') as file:
        lines = file.readlines()

    tailwind_config = lines[0].strip()
    relevant = lines[1].strip()
    css_string = ''.join(lines[2:]).strip()

    if len(css_string) < 1:
        clipboard_content = pyperclip.paste()
        if len(clipboard_content.strip()) >= 1:
            css_string = clipboard_content

    # Regular expression to find all occurrences of var(...) and replace with the fallback value
    pattern = r'var\([^,]+,\s*([^\)]+)\)'
    css_string = re.sub(pattern, r'\1', css_string)
    css_string = urllib.parse.unquote(css_string)

    return tailwind_config, relevant, css_string

