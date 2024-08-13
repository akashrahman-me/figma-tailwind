from lib.utils.is_valid_color import is_valid_color
from lib.classes_gen.helper.value_pass import value_pass
from lib.classes_gen.helper.combined_config import style
import pyperclip

# Generators
from lib.classes_gen.generators.color import color_class
from lib.classes_gen.generators.background import background_class
from lib.classes_gen.generators.border import border_class
from lib.classes_gen.generators.border_radius import border_radius_class
from lib.classes_gen.generators.box_shadow import box_shadow_class
from lib.classes_gen.generators.font_family import font_family_class
from lib.classes_gen.generators.font_size import font_size_class
from lib.classes_gen.generators.font_style import font_style_class
from lib.classes_gen.generators.font_weight import font_weight_class
from lib.classes_gen.generators.letter_spacing import letter_spacing_class
from lib.classes_gen.generators.line_height import line_height_class
from lib.classes_gen.generators.text_align import text_align_class
from lib.classes_gen.generators.padding import padding_class
from lib.classes_gen.generators.text_transform import text_transform_class

from lib.utils.relevant_styles import relevant_style
from lib.utils.clear_tailwind import clear_tailwind
config_path, relevant, css_string = relevant_style()


def css_to_tailwind(css):
    tailwind_classes = ""
    style._setCssText(css)

    properties = [
        # Typography
        ['font-weight', font_weight_class],
        ['font-family', font_family_class],
        ['font-style', font_style_class],
        ['text-align', text_align_class],
        ['text-transform', text_transform_class],
        ['font-size', font_size_class],
        [['line-height', 'font-size'], line_height_class],
        [['letter-spacing', 'font-size'], letter_spacing_class],

        # Color
        ['color', color_class],
        ['background-color', background_class],
        ['box-shadow', box_shadow_class],

        # Layout
        ['border-radius', border_radius_class],
        ['border', border_class],
        # ['padding', padding_class],
    ]

    def relevant_valid(class_name):
        result = ""
        _, relevant, _ = relevant_style()
        if class_name not in relevant:
            result = f" {class_name}"
        return result

    for property, property_class in properties:
        result = ""
        # if property is string
        if isinstance(property, str):
            if(style.getProperty(property)):
                value = style.getPropertyValue(property)
                result = relevant_valid(property_class(value))

        # if property is list
        elif isinstance(property, list):
            values = []
            for prop in property:
                if(style.getProperty(prop)):
                    value = style.getPropertyValue(prop)
                    values.append(value)
                else:
                    break
            if len(values) == len(property):
                result += relevant_valid(property_class(*values))

        tailwind_classes += result

    # tailwind_classes += value_pass('background', background_class, lambda value: is_valid_color(value))

    return tailwind_classes.strip()


classes = css_to_tailwind(css_string)
pyperclip.copy(classes)  # Copy the result
# clear_tailwind('tailwind.txt')
print(classes)