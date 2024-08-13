from lib.classes_gen.helper.combined_config import style
from lib.utils.relevant_styles import relevant_style

def relevant_valid(class_name):
    result = ""
    _, relevant, _ = relevant_style()
    if class_name not in relevant:
        result = f" {class_name}"
    return result

def value_pass(property, get_class, value_validation = None):   
    result = ""
    if(style.getProperty(property)):
        value = style.getPropertyValue(property)
        if value_validation is not None:
            if not value_validation(value):
                return result
            else:
                result = relevant_valid(get_class(value_validation(value)))
        else:
            result = relevant_valid(get_class(value))

    return result