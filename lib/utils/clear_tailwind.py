def clear_tailwind(path):
   # Read the file content
   with open(path, "r") as file:
      lines = file.readlines()

   # Keep only the first two lines and add a blank line
   new_lines = lines[:2] + ["\n"] + ["\n"]

   # Write the updated content back to the file
   with open(path, "w") as file:
      file.writelines(new_lines)