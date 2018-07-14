#! python3
# py copy - copies your .py file into MyPythonScripts

import shutil

# User input for which file to move and from where
pyfile = input('Which .py file would you like to copy?\n')
location = input('Where is the .py located?\n')

# Creates paths for copying the file to the new directory
old_location = location + '\\' + pyfile + '.py'
new_location = 'C:\MyPythonScripts' + '\\' + pyfile + '.py'

# Copies the .py file to the new directory
print('Copying file...')
shutil.copy(old_location, new_location)
print('Successfully copied ' + pyfile + ' .py to MyPythonScripts.')

# Creates a .bat file so program can be run from win+R
print('Creating ' + pyfile + '.bat...')
text = '@py.exe C:\MyPythonScripts\\' + pyfile + '.py %*\n@pause'
bat_file = open('C:\MyPythonScripts\\' + pyfile + '.txt', 'w')
bat_file.write(text)
bat_file.close()
# Convert .txt to .bat file
old_suffix = pyfile + '.txt'
new_suffix = pyfile + '.bat'
shutil.move('C:\MyPythonScripts\\' + old_suffix, 'C:\MyPythonScripts\\' + new_suffix)
print('Successfully created ' + pyfile + ' .bat to MyPythonScripts')
