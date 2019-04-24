#! python3
# cyanide_and_happiness.py
"""
Write a program that goes to a photo-sharing site like Flickr or Imgur,
searches for a category of photos, and then downloads all the resulting images.
You could write a program that works with any photo site that has a search feature.

For this project, I decided to download Cyanide & Happiness comics.
"""

import requests
import os
import bs4

# I did this a little bit differently than th Xkcd comics. I first found my comic archive,
# which turned out to be 'http://explosm.net/comics/(comic#)'
# I found it easier to set a variable with that max image number that is currently out for the comics.
# Then you can create a for loop that's range is the length of the maximum comic.
# Just don't forget to add the last comic number to the end of your url.
url_image_num = 4982  # this will be different since the max number is now higher
url = 'http://explosm.net/comics/' + str(url_image_num) + '/'

# Make sure you wrap it up in a try/except statement. Some comics won't be able to download. If you don't
# use a try/except statement your program will crash
for comic in range(url_image_num):
    try:
        # Make a new directory on the desktop
        os.chdir(r'c:\users\tomal\desktop')
        os.makedirs('cyanide_and_happiness', exist_ok=True)
        # This first request is for the initial url, or the last comic image. Don't forget to
        # res.raise_for_status()
        res = requests.get(url)
        res.raise_for_status()
        # The url for the comic image is inside an <img> tag with an id of 'main-comic'. You can
        # use BeautifulSoup to obtain this tag and get the src for the url. But you will have to add http:
        # to the beginning of the comic url.
        # Then change your res to the new comic url and res.raise_for_status() again!
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        match = soup.find('img', id='main-comic')
        comic_url = 'http:' + match.get('src')
        res = requests.get(comic_url)
        res.raise_for_status()

        # If the request is successful, we will download the content. Create a new file, Cyanide and Happiness
        # doesn't have captions like Xkcd, so we have to create new names. We can use the same method as the
        # last chapter with zfill, just don't forget to add the .jpg extension file name and open it in
        # 'wb', since it's in image and not just text. Use your res.iter_content to write each chunk and
        # close the file. Once finished, we will add 1 to the comic name while also subtracting the url comic
        # number by 1. This will allow us to open the previous url comic.
        print('Downloading C&H' + str(comic + 1).zfill(4) + '...')
        image_file = open(os.path.join('cyanide_and_happiness', 'C&H' + str(comic + 1).zfill(4)) + '.jpg', 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
        comic += 1
        url_image_num -= 1
        url = 'http://explosm.net/comics/' + str(url_image_num - 1) + '/'
        print(url)
    except requests.exceptions.HTTPError:
        # If a comic cannot download, we still want to change the url comic number so we can try the next one.
        # So decrease it by one, then set the url to a new one.
        print('Could not find comic. ')
        url_image_num -= 1
        url = 'http://explosm.net/comics/' + str(url_image_num - 1) + '/'
        print(url)


print('Finished.')
