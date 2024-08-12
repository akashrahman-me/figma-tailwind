import urllib.parse
import requests
import json

with open('./storage/google_webfonts.json') as f:
    google_webfonts = json.load(f)

def check_google_fonts_availability(font_name):
    # It's currently disalbed as we don't need freequently update of what font are comes in new cause we've already cloned and locally stored
    """
    GOOGLE_API_KEY = "AIzaSyDo5jvJTelZomK__xr1wcQ5Z9V13NprnDg"
    response = requests.get('https://www.googleapis.com/webfonts/v1/webfonts', params={'key': GOOGLE_API_KEY})
    fonts_data = response.json()['items']
    """

    fonts_data = google_webfonts['items']

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
        "font_imports": "\n".join(font_imports),
        "not_available": not_available
    }

    return result
