import json
from lib.theme_gen.extract_inline_css import extract_inline_css
from lib.theme_gen.filter_style_groups import filter_style_groups
from lib.theme_gen.css_object import css_object
from lib.theme_gen.tailwind_typography import tailwind_typography
from lib.theme_gen.font_families import font_families
from lib.theme_gen.format_font_families import format_font_families
from lib.theme_gen.generate_font_imports import generate_font_imports
from lib.theme_gen.box_shadow_sizes import box_shadow_sizes
from intelligence.colors.classify_and_rank_colors import classify_and_rank_colors
from intelligence.colors.serialize_colors import serialize_colors
from lib.echo import echo
from lib.utils.remove_text_content import remove_text_content


# Read the HTML file
with open("assemble/html.txt", "r", encoding="utf-8") as file:
    html_content = "<body>" + file.read() + "</body>"
html_content =  remove_text_content(html_content)

# Extract inline CSS from the HTML
styles_str = extract_inline_css(html_content)

color_groups = filter_style_groups(styles_str, ['color'])
colors = classify_and_rank_colors(css_object(color_groups))
colors = serialize_colors(colors)

# Filter style groups for box shadow
shadow_groups = filter_style_groups(styles_str, ["box-shadow"])
shadows = ""
if(shadow_groups):
    shadows = box_shadow_sizes(css_object(shadow_groups))

# Filter style groups for font size
typography_groups = filter_style_groups(styles_str, ["font-size"])
properties = css_object(typography_groups)

# Get the tailwind typography, font families, and formatted font families
font_sizes = tailwind_typography(properties)

font_weights = font_families(properties)
font_family = format_font_families(font_weights)

# Prepare the theme dictionary
themeing = {
    "colors": colors,
    "fontSize": font_sizes,
    "shadows": shadows,
    "fontFamily": font_family,
    "fontWeights": font_weights,
}

# Write the theme dictionary to a JSON file
with open("assemble/_theme.json", "w") as file:
    try:
        file.write(json.dumps(themeing))
        print("Theme creation successful !")
    except Exception as e:
        print(e)

