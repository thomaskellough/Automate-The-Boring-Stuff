#! python3
# scheduled_web_comic_downloader.py
"""
To see how most of this was written see cyanide_and_happiness.py
This will only go over the scheduling portion
"""

import requests
import os
import bs4
import time

os.chdir(r'c:\users\tomal\desktop')

# There is something you learned in Chapter 3 that you may not have used yet.
# It's setting a variable in global. If we want to run this function over and over,
# we need to make sure that each time the function starts it doesn't replace our
# variables with the same value. So we need to put the variables OUTSIDE the function.
# But now the function can't use them! If you forget how to do this, just add
# global (variable_name) right after the function. Then it's a global variable and can
# be used inside the function itself.
comic = 1
url_image_num = 4980

# In cyanide_and_happiness.py, we decreased the url with every download. However, this program
# looks for new downloads. So we will increment it if we have a successful download
def download_comic():
    global comic
    global url_image_num
    url = 'http://explosm.net/comics/' + str(url_image_num) + '/'
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        match = soup.find('img', id='main-comic')
        comic_url = 'http:' + match.get('src')
        res = requests.get(comic_url)
        res.raise_for_status()
        print('Downloading C&H' + str(comic).zfill(4) + '...')
        image_file = open('C&H' + str(comic).zfill(4) + '.jpg', 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
        comic += 1
        url_image_num += 1
        url = 'http://explosm.net/comics/' + str(url_image_num + 1) + '/'
        print(url)
    except requests.exceptions.HTTPError:
        print('No comic was found. Will try again in 8 hours')
    # I found the easiest way to make this program is to use time.sleep(1)
    # Put it in a for loop for however many seconds you want (28800 is 8 hours) and it will
    # complete after that time
    for second in range(28800):
        time.sleep(1)

# Another for loop controls the function itself. Since there are three 8-hour blocks in a day,
# 21 for loops will run for a week straight. You can set these numbers to whatever you want.
for hour_block in range(21):
    print('Searching for a new comic')
    download_comic()
