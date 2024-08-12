def relevant_style():
    # Read the file content
   with open('tailwind.txt', 'r') as file:
      lines = file.readlines()

   # Split into two elements: first line and the rest
   return (lines[0].strip(), ''.join(lines[1:]).strip())