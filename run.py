# This will not run on online IDE
import requests
import collections
from bs4 import BeautifulSoup

URL = "https://sfbay.craigslist.org/search/sss?query=herman+miller+aeron&sort=rel"
# URL = "https://sfbay.craigslist.org/contactinfo/sfo/fud/6997378730"

base_Url = "https://sfbay.craigslist.org"

search_Url = "/search/sss?query="
InputString = "herman miller aeron"
sort_by_rel = "&sort=rel"

email_Url = "/contactinfo/sfo/fud/"


def handle_requests(url):
    r = requests.get(base_Url+url)
    return BeautifulSoup(r.content, 'html5lib')


def lazy_go(inputString):
    emails = []
    q = collections.deque()

    formatted_input = inputString.replace(' ', '+')
    print(formatted_input)
    print(base_Url+search_Url+formatted_input+sort_by_rel)
    search_soup = handle_requests(search_Url+formatted_input+sort_by_rel)
    table = search_soup.find('ul', attrs={'class':'rows'})
    for row in table.findAll('li', attrs={'class':'result-row'}):
        q.append(row['data-pid'])
    for item_num in q:
        item = handle_requests(email_Url+item_num)
        email = item.find('a').text
        emails.append(email)

# t = soup.find('div', attrs={'class':'reply-info js-only'})
# email = soup.find('a')
# print(email.text)

# print(table)


def main():
    lazy_go(InputString)


if __name__ == "__main__":
    main()