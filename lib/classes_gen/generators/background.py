from lib.classes_gen.generators.color import color_class
from lib.classes_gen.helper.combined_config import combined_config

def background_class(value):
   class_name = color_class(value, 'bg')

   if class_name == '' and value != '' :
      backgrounds = combined_config['theme'].get('backgroundImage', {})

      if value is None:
         return ""

      for backgrounds_key in backgrounds:
            if isinstance(backgrounds[backgrounds_key], str):
               if backgrounds[backgrounds_key] == value:
                  return f"bg-{backgrounds_key}"
               
      return f"bg-[{str(value).replace(' ', '_')}]"

   else:
      return class_name
    
