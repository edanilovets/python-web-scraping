import datetime
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re





# find all links
# for link in bs.find_all('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])


# find all links from body of Kevin Bacon wiki page
# for link in bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])


random.seed(datetime.datetime.now())


def get_links(article_url):
    html = urlopen('https://en.wikipedia.org{}'.format(article_url))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = get_links('/wiki/Kevin_Bacon')
# print(len(links))
while len(links) > 0:
    new_article = links[random.randint(0, len(links)-1)].attrs['href']
    print(new_article)
    links = get_links(new_article)
