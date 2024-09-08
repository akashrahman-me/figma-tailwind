import urllib.parse
import os
import time
import requests
import json


GOOGLE_API_KEY = "AIzaSyDo5jvJTelZomK__xr1wcQ5Z9V13NprnDg"
GOOGLE_WEBFONTS = '../storage/google_webfonts.json'

def check_google_fonts_availability(font_name):
    current_time = time.time()
    modification_time = os.path.getmtime(GOOGLE_WEBFONTS)
    time_different = current_time - modification_time

    with open(GOOGLE_WEBFONTS) as f:
        fonts_data = json.load(f)

    if time_different >= (86400 * 7): # More than 7 day
        response = requests.get('https://www.googleapis.com/webfonts/v1/webfonts', params={'key': GOOGLE_API_KEY})
        fonts_data = response.json()['items']

        with open(GOOGLE_WEBFONTS, 'w') as fx:
            fx.write(json.dumps(fonts_data, indent=4))

    font_names = [font['family'] for font in fonts_data]
    return font_name in font_names

def generate_font_imports(font_data):
    base_url = "https://fonts.googleapis.com/css2?family="
    font_imports = []
    not_available = []

    for font in font_data:
        name = font["name"]
        weights = font["weight"]

        if check_google_fonts_availability(name):
            name_encoded = urllib.parse.quote_plus(name.replace(" ", "+"))
            weights_str = ";".join(weights)
            import_url = f"{base_url}{name_encoded}:wght@{weights_str}&display=swap"
            font_imports.append(f"@import url('{import_url}');")
        else:
            not_available.append(font)

    result = {
        "font_imports_string": "\n".join(font_imports),
        "font_not_available": not_available
    }

    return result
