# Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in the folder. Do the same for other formats. For example:
# * sssd.png --> 1.png
# * jarl.png --> 2.png
# ...and so on

import random
import string
import os
rand_name = [''.join(random.choices(string.ascii_lowercase,k=4)) for _ in range(0,10)]
os.chdir(os.path.dirname(os.path.abspath(__file__)))
png_files = [file for file in os.listdir("./") if file.endswith('.png')]


# Creating the clutter
if not png_files:
  for name in rand_name:
    if not os.path.exists(f"{name}.png"):
      with open(f"{name}.png", 'w') as f:
        f.write("")
    else:
      print(f"File {name} already exists")
      pass
else:
  print("Files are already there")
  
  
# Sorting the clutter
count = 1
for file in png_files:
  os.rename(file,f"{count}.{file.split('.')[1]}")
  count +=1