from lib.classes_gen.helper.combined_config import config
from lib.classes_gen.helper.combined_config import style
from lib.utils.relevant_styles import relevant_style

def releven_valid(t_class):
    result = ""
    relevant, _ = relevant_style()
    if t_class not in relevant:
        result = f" {t_class}"
    return result

def value_pass(property, get_class, value_validation = None):   
    result = ""
    if(style.getProperty(property)):
        value = style.getPropertyValue(property)
        if value_validation is not None:
            if not value_validation(value):
                return result
            else:
                result = releven_valid(get_class(value_validation(value)))
        else:
            result = releven_valid(get_class(value))

    return result