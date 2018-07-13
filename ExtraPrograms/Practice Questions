#! python3
# Removes the Q: from Automate the Boring Stuff Practice Questions


import pyperclip
import re


text = pyperclip.paste()
lines = text.split('Q:')
reg = re.compile('\d\.')

string = ''
for line in lines:
    line = line.strip()
    if reg.search(line):
        string = string + '#' + str(line) + '\n\n'

pyperclip.copy(string)
