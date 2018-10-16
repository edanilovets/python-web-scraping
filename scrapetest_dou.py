#  https://jobs.dou.ua/vacancies/?category=QA

from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('https://jobs.dou.ua/vacancies/?category=QA')
bs = BeautifulSoup(html, 'html.parser')

for city in bs.find('ul', {'class': 'other'}).find_all('a'):
    print(city)

# print(bs.head)
