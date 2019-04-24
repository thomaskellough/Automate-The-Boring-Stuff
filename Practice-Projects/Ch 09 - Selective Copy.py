#! python3
# selective copy.py
"""
Write a program that walks through a folder tree and searches for files with a
certain file extension. Copy these files from whatever location they are in to a new folder.
"""

import os
import re
import shutil

# This is actually a useful program that I have used numerous time. With that being said, I wanted
# to make it a bit more polished. I started off with an entry statement explaining what the
# program does.
print('This program is designed to pull all user-specified files from a single extension\n'
      'from one directory (including the directories within) into a new folder.\n\n')

# This is designed to create a folder on your desktop. You will need to change the path for
# your specific location. Tell the user what the program does and allow them an option to
# create a new folder. Wrap this up in a try and except statement in case the folder exists.
# If it does, continue the program anyway and save the files to that folder. This will keep
# the program from crashing. The del_folder = 0 will be used later. If the folder exists, add
# 1 to it. If not, it MAY be deleted later depending on if we find files or not.
os.chdir(r'C:\Users\tomal\Desktop')
new_folder = input('Let\'s create a new folder on the desktop.\n'
                   'What do you want the name of your folder to be?\n')
del_folder = 0
try:
    os.makedirs(new_folder)
except FileExistsError:
    print('This directory already exists.\n'
          'Your files will be placed in ' + new_folder)
    del_folder += 1

# You will use this technique for many other programs in this book. Create a file path for
# the folder you want to save it. Make it a variable name that you will easily understand later.
new_file_path = os.path.abspath(new_folder)

# Select the directory you wish to pull files from. Wrap it up in a while True statement
# so it repeats until the user enters a correct directory. Place it in another try and except
# statement so if the user enters a path that is invalid, it repeats the question and doesn't
# crash the program. Once you enter a valid directory, create another path variable to be used later.
while True:
    try:
        pull_directory = input('Where do you want to extract your files from?\n')
        os.chdir(pull_directory)
        path = os.getcwd()
        break
    except FileNotFoundError:
        print('Please type in a full path to the directory')

# Write a regex for selection of a certain type of files (case-insensitive)
# Allow the user to input the type of file. The user only needs to type the extension letters,
# not the period since it's added in the regex. You also want to pass re.I to make the search
# case-insensitive, since could be the same files with uppercase/lowercase letters.
type_of_file = input('What type of files do you want to copy?\n')
pdf_regex = re.compile(('.' + type_of_file + '$'), re.I)

# Walk through a directory and search for the specific files using os.walk. Set an iterator to 0 before
# this for loop starts. If you find one file, add 1 to it. It doesn't matter what it is, as long as it's
# either 0 or > 0. The print() is optional in this loop, but it helps to see what files you have and
# where they are. You will search the filename with the regex created. If it's found copy it to the new
# directory. REMEMBER: To move a file, you need the FULL path, not JUST the filename. This is why we created
# variables earlier. When creating the file path, don't forget to add the \ with an escape \.
i = 0
for folder_name, subfolders, filenames in os.walk(path):
    for filename in filenames:
        if pdf_regex.search(filename):
            print('FILE INSIDE ' + folder_name + ': ' + filename)
            file_path = folder_name + '\\' + filename
            shutil.copy(file_path, new_file_path)
            i += 1

# This is the outro. If i is > 1 that means at least one file was copied. Print a message telling the users
# where they were copied to. If i = 0 , no files were copied. So now two more options can happen. If we created
# a new folder, it will be deleted. However, if the folder already exists, we do not want to delete it because
# it may contain other files you want to keep. This is why we set del_folder to 0 earlier, then added 1 to it
# if a folder was created.
if i > 1:
    print('Files were successfully copied into %s ' % new_folder)
else:
    if del_folder == 0:
        print('There were no files to copy\n' +
              new_folder + ' has been deleted')
        path = os.path.abspath(new_folder)
        os.rmdir(path)
    else:
        print('There were no files to copy')
