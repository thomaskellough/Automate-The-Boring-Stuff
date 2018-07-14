#! python3
# inserting_gaps.py - Will insert gaps into numbered files so you add another file later

import os
import re
import shutil

# Set working directy, obtain variable for your path, create regex to find the specific files you want
os.chdir(r'C:\Users\tomal\Desktop\gaps')
path = os.getcwd()
regex = re.compile('(Wallpaper)(\d{,3})')

# Give the user an option to choose where they want the gap at. Whatever number they type will be skipped
# with the new naming. Don't forget zfill!
replace = input('Where would you like to insert a gap at?\n')
replace = str(replace.zfill(3))

# This is very similar to filling_the_gaps.py, but there are two differences. The first difference is adding 1 to
# your iterator created IF it equals what the user replaces. That will skip that naming. The second thing is
# changing the prefix for the new name. If you keep it the same as what it's currently named, you will end up
# writing over your brand new created files and losing some. So you want to create a brand new name. For this
# project I just added and underscore at the end of wallpaper.
i = 1
for file in os.listdir():
    mo = regex.search(file)
    if mo:
        old_name = os.path.abspath(file)
        if mo.group(2) == replace:
            i += 1
        new_suffix = 'Wallpaper_' + str(i).zfill(3) + '.jpg'
        new_name = os.path.join(path, new_suffix)
        i += 1
        shutil.move(old_name, new_name)


# This last section is technically optional, but if you want to have the same name before,
# (Wallpaper\d\d\d vs Wallpaper_\d\d\d) then you need this loop. You just need to create another new_name
# and old name using the groups from the new regex. re.sub() takes three arguments:
# 1) what you want to replace
# 2) what you want to replace argument one with
# 3) the file you want to replace
# Having this will keep the same names as you get from filling_the_gaps.py, but with the specified file skipped

rename_regex = re.compile('(Wallpaper_)(\d{,3})')
i = 1
for file in os.listdir():
    mo = rename_regex.search(file)
    if mo:
        old_name = os.path.join(path, mo.group(1) + mo.group(2) + '.jpg')
        new_name = os.path.join(path, re.sub(mo.group(1), 'Wallpaper', file))
        print('Renaming: %s to %s' % (old_name, new_name))
        shutil.move(old_name, new_name)
