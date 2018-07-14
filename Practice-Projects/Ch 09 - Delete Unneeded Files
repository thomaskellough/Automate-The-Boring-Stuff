#! python3
# large_file_search.py - Walks through a directory and finds large files.
"""
Write a program that walks through a folder tree and searches for exceptionally
large files or folders—say, ones that have a file size of more than 100MB. (
Remember, to get a file’s size, you can use os.path.getsize() from the os module.)
Print these files with their absolute path to the screen.
NOTE: This program does not delete the files. Just prints them onto a screen. You can
edit your program to delete them with send2trash, but you don't want to accidentally delete
a bunch of files you prefer to keep.
"""

import os

# Adding a user input for the directory is beneficial since you don't have to change
# the code itself to run the program for searching a different directory.
# Once again, wrap it in a try and except statement to allow the user to type
# in the directory again if they made a mistake
while True:
    try:
        dir_search = input('Please type in the path to a directory to search.\n')
        os.chdir(dir_search)
        dir_search = os.path.abspath('.')
        print('Searching ' + dir_search + '...')
        break
    except FileNotFoundError:
        print('Path not found. Please enter a complete path.')

# Search folder and subfolders and print out files greater than 100 mb
# Remember that size is measured in bytes, so 100 mb = 100000000
# Mega is equal to 10^6, so 100 + 6 zeroes. Brush up on this if you have problems converting.
# Create a full path to the filename by joining the folder_name (first argument for walk)
# with the filename itself. Then you can print out the absolute path to it IF it's greater
# than the size you're searching for.
# os.path.join() is a useful function that will be used later on as well. It joins two paths
# together. Ideally, you can get the foll path (in this example folder_name IS the full path) plus
# a filename. This will create a variable for that specific file. You can't grab a file just by
# the name itself since there could be multiple files with the same name in different directories
# You always need that full path!
for folder_name, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        filename = os.path.join(folder_name, filename)
        size = os.path.getsize(filename)
        if size > 100000000:
            print(os.path.abspath(filename) + ' - ' + str(size))

print('Done.')
