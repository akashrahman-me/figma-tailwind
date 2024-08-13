def relevant_style():
    # Read the file content
   with open('tailwind.txt', 'r') as file:
      lines = file.readlines()

   # Split into trhee elements: 1st line for tailwind config, 2nd for relevant styles, 3rd for styles 
   return (lines[0].strip(), lines[1].strip(), ''.join(lines[2:]).strip())