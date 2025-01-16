# Write a program to clear the clutter inside a folder on your computer.
# You should use os module to rename all the png images from 1.png all the way till n.png where n is the
# number of png files in that folder. Do the same for other file formats

import os
files =os.listdir("clutterFolder")
i=1
for file in files:
    print(f"{i}", file)
    if file.endswith(".jpg"):
        os.rename(f"clutterFolder/{file}",f"clutterFolder/{i}.png")
        # os.rename(f"clutterFolder/{file}",f"clutterFolder/this_is_png_picture.png")
    i=i+1




