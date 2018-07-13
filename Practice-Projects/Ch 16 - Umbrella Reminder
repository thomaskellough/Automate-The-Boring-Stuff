#! python3
# umbrella_reminder.py - Checks the weather in the morning and reminds you
# to pack an umbrella if it is raining
"""
Chapter 11 showed you how to use the requests module to scrape data from http://weather.gov/.
Write a program that runs just before you wake up in the morning and checks whether it’s
raining that day. If so, have the program text you a reminder to pack an umbrella before
leaving the house.
"""
import requests
import bs4
import time
import datetime
# Notice the new way to import the Client module. It's changed
# from how the book is.
from twilio.rest import Client

# Enter Twililo account information here
account_SID = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
client = Client(account_SID, auth_token)
my_twilio_number = 'YOUR_TWILIO_NUMBER'
my_cell_phone = 'YOUR_CELL_NUMBER'

# Download the web page from www.weather.gov
# This website tracks by zip code. Type in any zip
# code and pull the url from there. There are MANY ways
# you can scrape data from this website. I chose to
# scrape the summaries in the 7 day forceast. Yours
# may differ.
start = datetime.datetime(2018, 7, 10, 6, 30)
# This while loop sleeps until 6:30 in the morning
while datetime.datetime.now() < start:
    time.sleep(1)
for i in range(31):
    # See cyanide_and_happiness.py to learn how to scrape
    res = requests.get('https://forecast.weather.gov/MapClick.php?lat=33.159100000000024&lon=-96.72382999999996')
    res.raise_for_status()
    weather_soup = bs4.BeautifulSoup(res.text, "html.parser")
    match = weather_soup.find('li', class_='forecast-tombstone')
    # (match.text).lower will match a specific string. I chose t-storm. Once again, yours
    # may differ. If you find a match, send the text. If not, do nothing but print a message.
    if 't-storm' in str(match.text).lower():
        text = str(match.text).strip()
        print(text)
        message = client.messages.create(
            body='Chance of rain today! Don\'t forget to pac an umbrella!',
            from_=my_twilio_number,
            to=my_cell_phone)
    else:
        print('No rain. No message needed')
    # Sleeps for one day, the function repeats for 31 days
    time.sleep(86400)
