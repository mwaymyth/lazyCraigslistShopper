# This will not run on online IDE
import requests
from bs4 import BeautifulSoup

URL = "https://sfbay.craigslist.org/search/sss?query=herman+miller+aeron&sort=rel"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

emails = []  # A list of emails that I'm going to scrape from my seach query

table = soup.find('ul', attrs={'class':'rows'})
for row in table.findAll('li', attrs={'class':'result-row'}):
    print(row.a['href'])
    # print(row.prettify())

# print(table)