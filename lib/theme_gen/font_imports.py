from lib.theme_gen.generate_font_imports import check_google_fonts_availability

def to_camel_case(snake_str):
    # Convert the string to camelCase
    components = snake_str.split(' ')
    return components[0].lower() + ''.join(x.title() for x in components[1:])

def font_imports(font_families):
    font_families = [item for item in font_families if check_google_fonts_availability(item['name'])]
    output = 'import {' + ', '.join(  name.replace(" ", "_") for name in [item['name'] for item in font_families]) + '} from "next/font/google";\n\n'

    camel_case_names = []

    for item in font_families:
        font_name = item['name'].replace(" ", "_")
        camel_case_name = to_camel_case(item['name'])
        camel_case_names.append(camel_case_name)
        weights = ', '.join(f'"{weight}"' for weight in item['weight'])
        variable_name = f'--font-{font_name.lower()}'

        output += f"const {camel_case_name} = {font_name}({{\n"
        output += f'   subsets: ["latin"],\n'
        output += f'   weight: [{weights}],\n'
        output += f'   variable: "{variable_name}",\n'
        output += "});\n\n"

    output += f"const fonts = [{', '.join(camel_case_names)}];\n"

    return output