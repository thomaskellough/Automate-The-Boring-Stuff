#! python3
# random_chore.py - will randomly assign a chore to a set of individuals and email them
# once a day for a week
"""
Write a program that takes a list of people’s email addresses and a list of chores that
need to be done and randomly assigns chores to people. Email each person their assigned
chores. If you’re feeling ambitious, keep a record of each person’s previously assigned
chores so that you can make sure the program avoids assigning anyone the same chore they
did last time. For another possible feature, schedule the program to run once a week
automatically.
"""
import smtplib
import random
import time


# User information. Change your email and password here.
# It is recommended you add at least your password as an input.
user_email = 'youremailaddress@email.com'
user_pw = 'yourpassword'

# List of email addresses - Edit your email address from here
emails = ['email1@yahoo.com',
          'email2@yahoo.com',
          'email3@gmail.com',
          'email4@gmail.com']


# Function to assign chores and email them to email addresses in the list
# If you're doing this in a function, put the list inside the function itself. So it resets
# every time the function is called. Then create a for loop that assigns a random chore to
# the individual. You'll create a dictionary and assign the email as the key and
# chore as the value. Don't forget to remove the random chore from the list.
# Then send the email using smtp and your variables
def assignment():
    chores = ['Wash the dishes',
              'Mop the floor',
              'Walk the dog',
              'Feed the cat',
              'Clean toilet',
              'Mow the lawn',
              'Clean the kitchen']
    for email in emails:
        random_chore = random.choice(chores)
        email_dict[email] = random_chore
        chores.remove(random_chore)
    for email in email_dict:
        message = str('Subject: Your random chore is....\n' + email_dict[email])
        print(email.ljust(27) + ' is assigned: ' + email_dict[email].rjust(23))
        smtp_obj.sendmail(user_email, email, message)


# Empty dictionary to collect emails with chores
email_dict = {}
# Logging into the SMTP server - Note: your settings
# may be different depending on the email you use
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(user_email, user_pw)
# Calling the function to send the email every week
# The program will sleep for 24 hours and run through
# a loop for seven days.
for i in range(7):
    assignment()
    time.sleep(86400)
# Logging out of SMTP server
smtp_obj.quit()

