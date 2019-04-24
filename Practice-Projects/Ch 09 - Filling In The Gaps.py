#python 3
# filling_the_gaps.py

"""
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt,
and so on, in a single folder and locates any gaps in the numbering (such as if there is a
spam001.txt and spam003.txt but no spam002.txt). Have the program rename all the later files
to close this gap.

As an added challenge, write another program that can insert gaps into numbered files so that
a new file can be added. (see inserting_gaps.py)

A note for this program. I found the easiest way is to just rename all the files in the program.
Renaming every file takes nearly no time at all and it only takes a few lines.

A note about zfill():
This function is not taught in Automate The Boring Stuff, but it's very simple to use and makes
this program easy to run. It fills in extra zeroes to the left to a specific width. The first
step is converting your number to a string using str(). Then pass zfill() with an argument for how
many zeroes you want.

# >>> foo = str(3)
# >>> print	(foo)
# 3
# >>> print(foo.zfill(3))
# 003
"""

import os
import re
import shutil

os.chdir(r'C:\Users\tomal\Desktop\gaps')
path = os.getcwd()

# Create a regex expression to match the prefix you are looking for
prefix_regex = re.compile(r'(Wallpaper)(\d{,3})')

# Add an iterator to rename the end of each file. This will increase after each rename
# To rename files, you use shutil.move(old path, new path): Note: you need the full path! Not just the file name!
# The old name will be the absolute path the the file. This is easily achieved with os.path.abspath(filename)
# The new name is a bit tricker. You don't want to pull the file extension out because then .jpg will be repeated
# If you set your regex up with groups you can pull just the word you want. In this example. 'Wallpaper'
# So the suffix of ONLY the filname will be the regex group, plus your iterator (with zfill), and then you
# need to add the file extension back so the file is usable. In this example it's '.jpg'. Save this to a new variable.
# For full name you need to combine the absolute path with the path of the folder + the new variable created above.
# Remember don't use the absolute path for the filename here, just the folder you're saving it into.
# Then it's easy enough to call shutil.move(old_name, new_name) to rename all the files.
i = 1
for file in os.listdir():
    mo = prefix_regex.search(file)
    if mo:
        old_name = os.path.abspath(file)
        new_suffix = mo.group(1) + str(i).zfill(3) + '.jpg'
        new_name = os.path.join(path, new_suffix)
        i += 1
        print('Renaming: %s to %s' % (old_name, new_name))
        shutil.move(old_name, new_name)
