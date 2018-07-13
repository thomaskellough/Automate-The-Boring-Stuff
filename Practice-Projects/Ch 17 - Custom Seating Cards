
#! python3
# custom_seating_cards.py - Creates custom seating invitations
"""
Chapter 13 included a practice project to create custom invitations from
a list of guests in a plaintext file. As an additional project, use the
pillow module to create images for custom seating cards for your guests.
For each of the guests listed in the guests.txt file from the resources
at http://nostarch.com/automatestuff/, generate an image file with the
guest name and some flowery decoration. A public domain flower image is
available in the resources at http://nostarch.com/automatestuff/.

To ensure that each seating card is the same size, add a black rectangle
on the edges of the invitation image so that when the image is printed out,
there will be a guideline for cutting. The PNG files that Pillow produces
are set to 72 pixels per inch, so a 4×5-inch card would require a
288×360-pixel image.
"""
import os
from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont

"""
I made my invitations a Harry Potter style with guests names different characters
from Harry Potter. So I chose images that related to that as opposed to flowers
Your code and variable names may be different, but the idea can be the same.
Note: I'm no artist, if you use this code with my specific pictures don't judge me
on how bad they look :)
"""
os.makedirs('seating_invitations', exist_ok=True)
# Obtain guest names from a txt file
names = open('guests.txt')
names = names.read()
names = names.split('\n')

# Create image objects and obtain their sizes in variables
# It's easy and more readable to use the multiple assignment method for
# each pictures width and height. Resizing the image to fit on your card will
# be totally dependent on your specific image. I just tried a bunch of different
# numbers until they matched up how I liked it. The program runs really fast, and
# you can try it with a few images before doing a lot.
deathly_hallows = Image.open('deathlyhallows.jpg')
s_width, s_height = deathly_hallows.size
deathly_hallows = deathly_hallows.resize((int(s_width / 2.2), int(s_height / 2.2)))
owl = Image.open('owl.jpg')
o_width, o_height = owl.size
owl = owl.resize((int(o_width / 7), int(o_height / 7)))
hogwarts_im = Image.open('hogwarts.jpg')
hog_width, hog_height = hogwarts_im.size
# I am assuming the cards are meant to be folded like name tents, so I rotated one of
# my pictures 180 degrees so it wouldn't be upside down after folding.
hogwarts_im = hogwarts_im.rotate(180)
hogwarts_im = hogwarts_im.resize((int(hog_width/4), int(hog_height/4)))

# Create font folder with a font to use for the name
fonts_folder = 'C:\Windows\Fonts'
chiller = ImageFont.truetype(os.path.join(fonts_folder, 'chiller.ttf'), 32)

# For loop that adds all images and texts onto a design to have cut out and folded
# The for loop will run through each name in the list and add the images. So the
# text can be any length
for name in names:
    new_image = Image.new('RGBA', (400, 320), 'white')
    im_width, im_height = new_image.size
    new_image.paste(hogwarts_im, (150, 20))
    new_image.paste(deathly_hallows, (10, 190))
    new_image.paste(owl, (285, 190))
    draw = ImageDraw.Draw(new_image)
    draw.rectangle((4, 4, 396, 316), outline='black')
    width, height = draw.textsize(name)
    draw.text(((400 - width)/2 - 20, 220), name, fill='black', font=chiller)
    new_image.save(os.path.join('seating_invitations', name + '_Invite.png'))
