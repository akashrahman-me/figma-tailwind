from lib.utils.is_valid_color import is_valid_color
from lib.classes_gen.helper.combined_config import config,  css_string
from lib.classes_gen.helper.value_pass import value_pass
from lib.classes_gen.helper.combined_config import style
import pyperclip

# Generators
from lib.classes_gen.generators.color import get_color_class_from_color_value
from lib.classes_gen.generators.background import get_background_color_class_from_background_color_value
from lib.classes_gen.generators.border import get_border_class_from_border_value
from lib.classes_gen.generators.border_radius import get_border_radius_class_from_border_radius_value
from lib.classes_gen.generators.box_shadow import get_box_shadow_class_from_box_shadow_value
from lib.classes_gen.generators.font_family import get_font_family_class_from_font_family_value
from lib.classes_gen.generators.font_size import get_font_size_class_from_font_size_value
from lib.classes_gen.generators.font_style import get_font_style_class_from_font_style_value
from lib.classes_gen.generators.font_weight import get_font_weight_class_from_font_weight_value
from lib.classes_gen.generators.letter_spacing import get_letter_spacing_class_from_letter_spacing_value
from lib.classes_gen.generators.line_height import get_line_height_class_from_line_height_value
from lib.classes_gen.generators.text_align import get_text_align_class_from_text_align_value
from lib.classes_gen.generators.padding import get_padding_class_from_line_padding_value
from lib.classes_gen.generators.text_transform import get_text_transform


def css_to_tailwind(css):
    tailwind_classes = ""
    style._setCssText(css)

    properties = [
        ['color', get_color_class_from_color_value],
        ['border-radius', get_border_radius_class_from_border_radius_value],
        ['text-align', get_text_align_class_from_text_align_value],
        ['font-style', get_font_style_class_from_font_style_value],
        ['background-color', get_background_color_class_from_background_color_value],
        ['border', get_border_class_from_border_value],
        ['font-weight', get_font_weight_class_from_font_weight_value],
        ['font-family', get_font_family_class_from_font_family_value],
        ['box-shadow', get_box_shadow_class_from_box_shadow_value],
        ['padding', get_padding_class_from_line_padding_value],
        ['text-transform', get_text_transform],
    ]

    for property, get_class in properties:
        tailwind_classes += value_pass(property, get_class)

    tailwind_classes += value_pass('background', get_background_color_class_from_background_color_value,
                                   lambda value: is_valid_color(value))

    if style.getProperty('font-size'):
        font_size_value = style.getPropertyValue('font-size')
        line_height_value = style.getPropertyValue('line-height')
        letter_spacing_value = style.getPropertyValue('letter-spacing')

        tailwind_font_size = get_font_size_class_from_font_size_value(font_size_value,
                                                                      letter_spacing_value,
                                                                      line_height_value
                                                                      )
        if tailwind_font_size not in config["releven_class"]:
            tailwind_classes += f" {tailwind_font_size}"

        if style.getProperty('line-height'):
            tailwind_line_height = get_line_height_class_from_line_height_value(
                line_height_value, font_size_value)

            if tailwind_line_height not in config["releven_class"]:
                tailwind_classes += f" {tailwind_line_height}"

        if style.getProperty('letter-spacing'):
            tailwind_letter_spacing = get_letter_spacing_class_from_letter_spacing_value(
                letter_spacing_value, font_size_value)
            if tailwind_letter_spacing not in config["releven_class"]:
                tailwind_classes += f" {tailwind_letter_spacing}"

    return tailwind_classes.strip()


classes = css_to_tailwind(css_string)
pyperclip.copy(classes)  # Copy the result
print(classes)
