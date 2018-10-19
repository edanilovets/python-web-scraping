#  https://jobs.dou.ua/vacancies/?category=QA

from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('https://jobs.dou.ua/vacancies/?category=QA')
bs = BeautifulSoup(html, 'html.parser')
cities = bs.find('ul', {'class': 'other'}).find_all('a')

# for city in cities:
#     print(city)

new_vacancies = bs.find('div', id='vacancyListId').find_all('a')

for vacancy in new_vacancies:
    print(vacancy)
