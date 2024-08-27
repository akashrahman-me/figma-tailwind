import re
import urllib.parse

def relevant_style():
   # Read the file content
   with open('tailwind.txt', 'r') as file:
      lines = file.readlines()

   tailwind_config = lines[0].strip()
   relevant = lines[1].strip()
   css_string = ''.join(lines[2:]).strip()

   # Regular expression to find any CSS property with var(...)
   # Replace the matched pattern with just the fallback hex color
   pattern = r'var\([^,]+,\s*(#[0-9A-Fa-f]{3,6})\)'
   css_string = re.sub(pattern, r'\1', css_string)

   css_string = urllib.parse.unquote(css_string)

   return (tailwind_config, relevant, css_string)