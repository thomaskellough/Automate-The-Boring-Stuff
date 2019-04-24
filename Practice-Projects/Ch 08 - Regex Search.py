#! python3
# regex_search.py

"""
Write a program that opens all .txt files in a folder and searches for any line that
matches a user-supplied regular expression. The result should be printed to the screen
"""
import os
import re
import pprint


# First, initiate an empty list to hold all text files. Then loop through the directory
# using os.listdir('.'). We actually don't need to use regex for something this simple.
# We can use .endswith(.'txt') and it will find any txt file. For each file that's found
# append it to the file listed.
files = []
for file in os.listdir('.'):
    if file.endswith('.txt'):
        files.append(file)


# Ask the user to input an expression to search all files for. I use re.I here
# so it will not be case-sensitive.
user_expression = input('What expression are you looking for?\n')
search_regex = re.compile(user_expression, re.I)

# Initiate another list of files, but this one will hold the files that include the
# regular expression typed in by the user
file_list = []
# Iterate through all txt files, find the expression, and display a list of txt files
# with the expression. You need to open teach text file and read it, then search through
# every line for the expression. If it's found, the filename is appended to the new
# list that was created. Once finished, print the list of files that contain
# the regular expression.
for filename in files:
    open_file = open(filename)
    read_file = open_file.read()
    if search_regex.search(read_file):
        file_list.append(filename)

pprint.pprint(file_list)
