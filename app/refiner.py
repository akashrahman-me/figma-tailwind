import re
from classname import css_to_tailwind, properties
import time

theme_path = "D:/Endeavors/e-service/tailwind.config.ts"
ignore_class = "text-left text-black font-normal items-start px-0 my-0 mx-0 m-0 p-0 gap-0 py-0"
ignore_styles = ['word-wrap']

inline_html = """
<div style="width: 1920px; height: 800px; position: relative">
  <div style="width: 1780px; height: 800px; left: 70px; top: 0px; position: absolute; background: #282021; border-radius: 16px"></div>
  <div style="width: 1780px; height: 800px; left: 70px; top: 0px; position: absolute">
    <div style="width: 1780px; height: 800px; left: 0px; top: 0px; position: absolute; background: #282021"></div>
    <img style="width: 1649.01px; height: 1144.34px; left: 708.03px; top: -411px; position: absolute; transform: rotate(115.16deg); transform-origin: 0 0; opacity: 0.10; border-radius: 16px" src="https://via.placeholder.com/1649x1144" />
  </div>
  <div style="left: 220px; top: 174px; position: absolute; justify-content: flex-start; align-items: center; gap: 87px; display: inline-flex">
    <div style="width: 730px; height: 443px; position: relative">
      <div style="width: 730px; height: 322px; left: 0px; top: 0px; position: absolute; flex-direction: column; justify-content: flex-start; align-items: flex-start; gap: 60px; display: inline-flex">
        <div style="align-self: stretch"><span style="color: white; font-size: 40px; font-family: Hanken Grotesk; font-weight: 300; line-height: 52px; word-wrap: break-word">Acadian Supply is the EXCLUSIVE U.S. wholesale distributor of</span><span style="color: white; font-size: 40px; font-family: Hanken Grotesk; font-weight: 600; line-height: 52px; word-wrap: break-word"> premium <br/>New Zealand sphagnum moss, orchid bark, and tree fern fiber.</span></div>
        <div style="align-self: stretch; color: white; font-size: 20px; font-family: Hanken Grotesk; font-weight: 400; line-height: 32px; word-wrap: break-word">Our premium sphagnum moss, orchid bark, and tree fern fiber is used for a wide variety of applications from growing orchids and canivorous plants to amphibian and reptile bedding to specialty applications for aroids, topiaries, and more.</div>
      </div>
      <div style="width: 519px; height: 61px; left: 0px; top: 382px; position: absolute; justify-content: flex-start; align-items: center; gap: 20px; display: inline-flex">
        <div style="padding-left: 32px; padding-right: 32px; padding-top: 16px; padding-bottom: 16px; background: #E774B1; border-radius: 4px; justify-content: center; align-items: center; gap: 10px; display: flex">
          <div style="color: white; font-size: 18px; font-family: Hanken Grotesk; font-weight: 400; line-height: 28.80px; word-wrap: break-word">Where to Buy</div>
        </div>
        <div style="padding-left: 32px; padding-right: 32px; padding-top: 16px; padding-bottom: 16px; border-radius: 4px; border: 1px #3BAF49 solid; justify-content: center; align-items: center; gap: 10px; display: flex">
          <div style="color: #3BAF49; font-size: 18px; font-family: Hanken Grotesk; font-weight: 400; line-height: 28.80px; word-wrap: break-word">Buying in bulk? Get our price list</div>
        </div>
      </div>
    </div>
    <div style="width: 745px; height: 521px; position: relative">
      <div style="width: 316px; height: 108px; left: 29px; top: 385px; position: absolute; background: #141111; box-shadow: 24px 24px 24px; filter: blur(24px)"></div>
      <img style="width: 529px; height: 399px; left: 67px; top: 0px; position: absolute" src="https://via.placeholder.com/529x399" />
      <img style="width: 532.40px; height: 399px; left: 64.60px; top: 1px; position: absolute" src="https://via.placeholder.com/532x399" />
      <img style="width: 368px; height: 195px; left: 0px; top: 311px; position: absolute" src="https://via.placeholder.com/368x195" />
      <div style="width: 86px; height: 209px; left: 401px; top: 180px; position: absolute; background: rgba(13, 13, 15, 0.50); box-shadow: 34px 34px 34px; filter: blur(34px)"></div>
      <img style="width: 451px; height: 387px; left: 294px; top: 134px; position: absolute" src="https://via.placeholder.com/451x387" />
    </div>
  </div>
  <div style="height: 51px; left: 0px; top: 24px; position: absolute; flex-direction: column; justify-content: flex-start; align-items: center; gap: 25px; display: inline-flex">
    <div style="align-self: stretch; text-align: center; color: #3BAF49; font-size: 20px; font-family: Hanken Grotesk; font-weight: 400; word-wrap: break-word">We’re known for dependability, service, and the best sphagnum moss, orchid bark, and tree fern fiber on the market!</div>
    <div style="align-self: stretch; height: 0px; border: 1px rgba(255, 255, 255, 0.10) solid"></div>
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
        if prop.strip() and not any(prop.strip().startswith(support_prop) for support_prop in [*support_properties, *ignore_styles])
    ]

    # Join the remaining properties back into a string
    new_style_value = '; '.join(filtered_properties)

    # Remove style attribute if empty, otherwise update it
    if not new_style_value:
        no_style_tag = re.sub(r'\sstyle="[^"]*"', '', match.group(0))
    else:
        no_style_tag = re.sub(r'style="[^"]*"', f'style="{new_style_value}"', match.group(0))
        print(new_style_value)

    # Add class names
    if 'class="' in no_style_tag:
        return re.sub(r'class="([^"]*)"', fr'class="\1 {class_names}"', no_style_tag)
    else:
        end_char = '/>' if not no_style_tag.endswith('>') else '>'
        return no_style_tag.replace(end_char, f' class="{class_names}"{end_char}')

pattern = r'<[^>]*\sstyle="[^"]*"[^>]*>'
new_html = re.sub(pattern, replace_match, inline_html)

print(new_html)
