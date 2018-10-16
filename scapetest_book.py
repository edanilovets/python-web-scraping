from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None

    try:
        bs = BeautifulSoup(html, 'html.parser')
        title = bs.body.h1
    except AttributeError:
        return None
    return title


page_title = get_title('http://pythonscraping.com/pages/page1.html')

if page_title is None:
    print('Title could not be found')
else:
    print(page_title)