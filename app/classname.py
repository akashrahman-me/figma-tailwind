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
from lib.classes_gen.generators.display import display_class
from lib.classes_gen.generators.gap import gap_class
from lib.classes_gen.generators.text_align import text_align_class
from lib.classes_gen.generators.padding import padding_class
from lib.classes_gen.generators.align_items import align_items_class
from lib.classes_gen.generators.opacity import opacity_class
from lib.classes_gen.generators.margin import margin_class
from lib.classes_gen.generators.text_transform import text_transform_class
from lib.utils.css_string_to_properties import css_string_to_properties

from lib.utils.relevant_styles import relevant_style
from lib.utils.clear_tailwind import clear_tailwind

def relevant_valid(class_name):
    _, relevant, _ = relevant_style()
    return f" {class_name}" if class_name not in relevant else ""


def generate_property_class(styles, property, property_class):
    if isinstance(property, str):
        return relevant_valid(property_class(styles[property])) if property in styles else ""

    elif isinstance(property, list):
        values = [styles[prop] for prop in property if prop in styles]
        return relevant_valid(property_class(*values)) if len(values) == len(property) else ""

    return ""

def css_to_tailwind(css):
    """Converts CSS styles to Tailwind CSS classes."""
    styles = css_string_to_properties(css)
    tailwind_classes = ""

    properties = [
        # Typography
        ('font-weight', font_weight_class),
        ('font-family', font_family_class),
        ('font-style', font_style_class),
        ('text-align', text_align_class),
        ('font-size', font_size_class),
        (['line-height', 'font-size'], line_height_class),
        (['letter-spacing', 'font-size'], letter_spacing_class),
        ('text-transform', text_transform_class),
        ('color', color_class),

        # Color
        ('background-color', background_class),

        # Styles
        ('border-radius', border_radius_class),
        ('background', background_class),
        ('box-shadow', box_shadow_class),
        ('border', border_class),
        ('opacity', opacity_class),

        # Layout
        ('padding', padding_class),
        ('margin', margin_class),
        ('display', display_class),
        ('gap', gap_class),
        ('align-items', align_items_class),
    ]

    for property_n, property_class in properties:
        tailwind_classes += generate_property_class(styles, property_n, property_class)

    return tailwind_classes.strip()

def class_generate(refer="txt_file"):
    """Generates and copies Tailwind CSS classes to the clipboard."""
    _, _, css_string = relevant_style()
    tailwind_classes = css_to_tailwind(css_string)

    if refer != 'dev':
        pyperclip.copy(tailwind_classes)

    if refer == "txt_file" and refer != 'dev':
        clear_tailwind('../tailwind.txt')

    print(tailwind_classes)


if __name__ == '__main__':
    class_generate(refer="dev")