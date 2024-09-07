from lib.classes_gen.generators.color import color_class
from lib.classes_gen.theme_mixer import theme_mixer

def background_class(value, theme_path):
   theme = theme_mixer(theme_path)
   class_name = color_class(value, theme_path, 'bg')

   if class_name == '' and value != '' :
      backgrounds = theme['theme'].get('backgroundImage', {})

      if value is None:
         return ""

      for backgrounds_key in backgrounds:
            if isinstance(backgrounds[backgrounds_key], str):
               if backgrounds[backgrounds_key] == value:
                  return f"bg-{backgrounds_key}"
               
      return f"bg-[{str(value).replace(' ', '_')}]"

   else:
      return class_name
    
