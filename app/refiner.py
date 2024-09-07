import re
from classname import css_to_tailwind, properties
import time

theme_path = "D:/Endeavors/e-service/tailwind.config.ts"
ignore_class = "text-left text-black font-normal items-start px-0 my-0 mx-0 m-0 p-0 gap-0 py-0"

inline_html = """
<div style="width: 189px; height: 68px; justify-content: center; align-items: center; gap: 28px; display: inline-flex">
  <div style="width: 113px; flex-direction: column; justify-content: flex-start; align-items: flex-start; gap: 12px; display: inline-flex">
    <div style="align-self: stretch; text-align: right; color: #334155; font-size: 18px; font-family: IBM Plex Sans; font-weight: 400; line-height: 36px; word-wrap: break-word">الفيديو التعريفي</div>
    <div style="align-self: stretch; justify-content: flex-end; align-items: center; gap: 4px; display: inline-flex">
      <div style="width: 16px; height: 16px; position: relative">
        <div style="width: 11.67px; height: 11.67px; left: 2.17px; top: 2.17px; position: absolute; background: #384250"></div>
      </div>
      <div style="text-align: right; color: #384250; font-size: 14px; font-family: IBM Plex Sans; font-weight: 400; line-height: 20px; word-wrap: break-word">مشاهدة الفيديو</div>
    </div>
  </div>
  <div style="padding: 12px; background: #F3FCF6; border-radius: 8px; justify-content: center; align-items: center; gap: 8px; display: flex">
    <div style="width: 24px; height: 24px; position: relative">
      <div style="width: 21.50px; height: 17.50px; left: 1.25px; top: 3.25px; position: absolute; background: #1B8354"></div>
    </div>
  </div>
</div>
"""

support_properties = [item[0] if isinstance(item[0], str) else item[0][0] for item in properties]

def replace_match(match):
    style_value = re.search(r'style="([^"]*)"', match.group(0)).group(1)
    class_names = css_to_tailwind(style_value, ignore_class, theme_path)
    style_properties = style_value.split(';')

    # Filter out the properties that should be removed
    filtered_properties = [
        prop.strip() for prop in style_properties
        if prop.strip() and not any(prop.strip().startswith(support_prop) for support_prop in support_properties)
    ]

    # Join the remaining properties back into a string
    new_style_value = '; '.join(filtered_properties)

    # Remove style attribute if empty, otherwise update it
    if not new_style_value:
        no_style_tag = re.sub(r'\sstyle="[^"]*"', '', match.group(0))
    else:
        no_style_tag = re.sub(r'style="[^"]*"', f'style="{new_style_value}"', match.group(0))

    # Add class names
    if 'class="' in no_style_tag:
        return re.sub(r'class="([^"]*)"', fr'class="\1 {class_names}"', no_style_tag)
    else:
        end_char = '/>' if not no_style_tag.endswith('>') else '>'
        return no_style_tag.replace(end_char, f' class="{class_names}"{end_char}')

pattern = r'<[^>]*\sstyle="[^"]*"[^>]*>'
new_html = re.sub(pattern, replace_match, inline_html)


print(new_html)
