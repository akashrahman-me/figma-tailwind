def compare_pixel(pixel1, pixel2, threshold=20):
   if threshold == 0:
      return pixel1 == pixel2
   
   if pixel1 == pixel2:
      return True

   if pixel1 == 0 and pixel2 != 0:
      return False
   if pixel2 == 0 and pixel1 != 0:
      return False

   if pixel1 >= 4 or pixel2 >= 4:
      return abs(pixel1 - pixel2) <= ((pixel1 / threshold) + ((384 - pixel1) / 384))
   else:
      return round(pixel1) == round(pixel2)