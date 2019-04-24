#! python3
# auto_unsubscribe.py - Automatically scans email and searches for a link for unsubscribe
# Then opens up a web browser to each link
"""
NOTE ABOUT THIS CODE!! This will open all emails with and unsubscribe link found.
Some links will automatically unsubscribe once opened, without having to complete
additional steps. You may find yourself unsubscribing from places you don't want to
and you may not be able to figure out which one it is. Nontheless, here is the program.

Write a program that scans through your email account, finds all the unsubscribe
links in all your emails, and automatically opens them in a browser. This program
will have to log in to your email provider’s IMAP server and download all of your
emails. You can use BeautifulSoup (covered in Chapter 11) to check for any instance
where the word unsubscribe occurs within an HTML link tag.
"""
import webbrowser
import imapclient
import pyzmail
import bs4


# Email address and password - Edit here (or add as user inputs)
email_address = 'YOUR EMAIL'
password = 'YOUR PASSWORD'

# Log into IMAP
imap_obj = imapclient.IMAPClient('imap.mail.yahoo.com', ssl=True)
imap_obj.login(email_address, password)

# Open emails and search for 'unsubscribe'
imap_obj.select_folder('INBOX', readonly=True)
# I believe this syntax is different than the book shows.
# You can search multiple links but you need a comma to separate
# everything or it won't work
UDSs = imap_obj.search(['BODY', 'unsubscribe', 'SINCE', '01-Jun-2017'])
raw_messages = imap_obj.fetch(UDSs, ['BODY[]'])
for message in UDSs:
    message_list = []
    # You may need to add the b before 'BODY[]', it's not in the book either
    # but Google found me a solution that worked
    message = pyzmail.PyzMessage.factory(raw_messages[message][b'BODY[]'])
    try:
        html_obj = message.html_part.get_payload().decode(message.html_part.charset)
        soup = bs4.BeautifulSoup(html_obj, "html.parser")
        # We did this in link_verification.py, same idea here.
        elem = soup.select('a')
        for i in range(len(elem)):
            url = elem[i].get('href')
            if 'unsubscribe' in url:
                webbrowser.open(url)
    except:
        print('Could not parse email')
imap_obj.logout()
