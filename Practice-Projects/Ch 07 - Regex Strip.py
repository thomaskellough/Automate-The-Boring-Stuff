#! python3
# regex_strip.py

""" Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to strip,
then whitespace characters will be removed from the beginning and end of the
string. Otherwise, the characters specified in the second argument to the
function will be removed from the string. """

import re

test_string = input('Please enter a string to strip: ')
char_rm = input('What characters do you want to remove? (Press enter for whitepsace)')


# This function takes in two argument. A string to strip and optional second argument to
# strip a removing character.
# The first if statement is run if the user does input a second argument. It strips the char/string provided.
# Your re.compile will use your second argument as its argument (or whitespace if none) and sub the
# whitespace. The whitespace will need to be removed from the beginning and end, so it will take
# two regexes. As always, ensure your characters are in the right order! To check that all white
# spaces are removed print out the length of the new string.
def white_strip(string, remove):
    if remove != '':
        strip_regex = re.compile(remove)
        new_string = strip_regex.sub('', string)
        return new_string
    else:
        strip_regex = re.compile('^\s*')
        new_string = strip_regex.sub('', string)
        strip_regex = re.compile('\s*$')
        new_string = strip_regex.sub('', new_string)
        return new_string


new_string = white_strip(test_string, char_rm)
print(new_string)
