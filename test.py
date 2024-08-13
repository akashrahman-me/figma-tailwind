import re

# Input string
css_string = """color: var(--black, #000000);
font-family: Roboto;
font-size: 18px;
font-style: normal;
font-weight: 500;
line-height: 26px; /* 144.444% */
background-color: var(--background, #FFF);
border-color: var(--border, #CCC);"""

pattern = r'var\([^,]+,\s*(#[0-9A-Fa-f]{3,6})\)'
updated_css_string = re.sub(pattern, r'\1', css_string)

print(updated_css_string)
