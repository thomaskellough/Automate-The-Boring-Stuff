#! python 3
# 2048 - will launch the game of 2048 and play automatically
"""
2048 is a simple game where you combine tiles by sliding them up, down,
left, or right with the arrow keys. You can actually get a fairly high
score by repeatedly sliding in an up, right, down, and left pattern over
and over again. Write a program that will open the game at
https://gabrielecirulli.github.io/2048/ and keep sending up, right, down,
and left keystrokes to automatically play the game.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random


# Using selenium and your appropriate webdriver, open the game
# and maximize your window (optional)
browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')
browser.maximize_window()

# Remember, obtaining the html element will allow you to use your keys
# on the webpage without having to have anything specific click
html_elem = browser.find_element_by_tag_name('html')

# While true will keep this running continuously. I know the project said to
# create one pattern, but we have used the random module before so I figured
# it's good to throw it in here to. This allows a random key to be pressed so
# it's not the same pattern over and over. If you throw a try/except statement
# at the end of your keypress to try and click the retry-button after a game
# completes you can have the program automatically start a new game.
# Watch your highest score rake up!
while True:
    key = random.randint(1, 4)
    if key is 1:
        html_elem.send_keys(Keys.UP)
    elif key is 2:
        html_elem.send_keys(Keys.DOWN)
    elif key is 3:
        html_elem.send_keys(Keys.RIGHT)
    elif key is 4:
        html_elem.send_keys(Keys.LEFT)
    try:
        retry_elem = browser.find_element_by_class_name('retry-button')
        retry_elem.click()
        continue
    except:
        continue
