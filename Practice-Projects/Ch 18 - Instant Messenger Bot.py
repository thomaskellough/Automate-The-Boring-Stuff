#! python3
# instant_message_bot.py - opens gmail then sends a message with a select user in your friends list
"""
The Google Talk application has a search bar that lets you enter a username on your friend
list and open a messaging window when you press ENTER. The keyboard focus automatically
moves to the new window. Other instant messenger applications have similar ways to open
new message windows. Write a program that will automatically send out a notification
message to a select group of people on your friend list. Your program may have to deal
with exceptional cases, such as friends being offline, the chat window appearing at
different coordinates on the screen, or confirmation boxes that interrupt your messaging.
Your program will have to take screen-shots to guide its GUI interaction and adopt ways
of detecting when its virtual keystrokes aren’t being sent

Note, this program will be different depending on your specific case. I have mine automatically
logged in so I don't need to enter my email information. Edit your program accordingly.
"""
import webbrowser
import pyautogui
import time
import sys
import os


# Change to WD with your picture available
os.chdir(r'C:\Users\tomal\Desktop\Python\Automate the Boring Stuff\18 - Controlling The Keyboard And Mouse With GUI Automation')
pyautogui.PAUSE = 0.5
# Message and emails to add as arguments. Can be unlimited email addresses, but one message
message = sys.argv[1]
emails_addresses = list(sys.argv[2:])

# Open the browser for google hangouts
webbrowser.open('https://hangouts.google.com/')
# I choose to maximize the window so the screen will always look the same. We aren't using
# selenium so we need another way. In chrome, there is a keyboard shortcut to do this
# PyAutoGUI makes it easy because we don't even need to select anything!
pyautogui.hotkey('alt', 'space', 'x')

time.sleep(5)  # wait for the page to load up
# If it takes a bit longer to load than normal, this loop will prevent the program
# from messing up or crashing. If it can't late the picture of the New Conversation, it
# will sleep for another 5 seconds
while pyautogui.locateOnScreen('New Conversation.png') is None:
    time.sleep(5)


# Function that starts a new conversation and send a message
# My computer resolution is probably different than yours. I'm
# only at 1366 x 768. :(
# So edit these numbers to match your specific text computer
# Create a function that sends the message.
def send_message(email):
    pyautogui.moveTo(251, 209)
    pyautogui.click()
    pyautogui.typewrite(email)
    pyautogui.moveTo(252, 336)
    pyautogui.click()
    pyautogui.typewrite('Hello. Test message.')
    pyautogui.press('enter')

# Your emails are taken from arguments in the command line, so create
# a for loop that runs through each email and calls the function with
# each email as the argument
for email_address in emails_addresses:
    send_message(email_address)
