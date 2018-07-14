#! python3
# link_verification
"""
Write a program that, given the URL of a web page, will attempt to download
every linked page on the page. The program should flag any pages that have
a 404 “Not Found” status code and print them out as broken links.
"""
import requests
import bs4

# Replae url with any link you desire
url = 'https://www.yahoo.com/news/'
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
# To select links, first pull elements from 'a'
print(soup)
# Selecting the 'a' element will identify any possible links
# that have an href attribute. Then you can separate each link by searching
# for the 'href attribute for each element. Try and open each link with requests.get then
# check the status code. If res.status_code returns 404, it's a broken link.
links = soup.select('a')
for link in links:
    link = link.get('href')
    try:
        res = requests.get(link)
        if res.status_code == 404:
            print('404 for: ' + link)
        else:
            print('Working link: ' + link)
            continue
    except requests.exceptions.MissingSchema:
        continue
