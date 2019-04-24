#! python3
# identify_photo_folders.py - Searches the hard drive for any folders that have more than half
# their contents as a picture greater than 500x500 pixels
"""
Write a program that goes through every folder on your hard drive and finds potential photo folders.
Of course, first you’ll have to define what you consider a “photo folder” to be; let’s say that it’s
any folder where more than half of the files are photos. And how do you define what files are photos?

First, a photo file must have the file extension .png or .jpg. Also, photos are large images; a
photo file’s width and height must both be larger than 500 pixels. This is a safe bet, since most
digital camera photos are several thousand pixels in width and height.
"""
import os
from PIL import Image

"""
Compared to the walking we did in previous programs, this one is very simple!
Do a normal walk using os.walk. Set two variables, one for num of photos and
one for num of non photos
If a filename does NOT end with a photo extenstion, add one to non photos and
then continue. If it does end with the correct extension, try opening the photo
and obtaining the size. If it's greater than 500 x 500 add one to num_photos.
Otherwise, add one to non-photos. Some files with have issues opening, handle
this with a try/except.
After each folder is searched, print out the folder name if num_photos > num_non_photos
"""
print('Scanning your hard drive to look for photo folders...')
for foldername, subfolders, filenames in os.walk('C:\\'):
    num_photos = 0
    num_non_photos = 0
    for filename in filenames:
        if not filename.endswith(('.jpg', '.JPG', '.png', '.PNG')):
            num_non_photos += 1
            continue
        else:
            try:
                photo = Image.open(os.path.join(foldername, filename))
                height, width = photo.size
                if height and width > 500:
                    num_photos += 1
                else:
                    num_non_photos += 1
            except OSError:
                num_non_photos += 1
    if num_photos > num_non_photos:
        print(foldername)
