from urllib.request import urlopen
from urllib.parse import quote
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('https://ru.wikipedia.org/wiki/{}'.format(quote('Питоны')))
    # html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could be found!')
else:
    print('It worked!')

    bs = BeautifulSoup(html.read(), 'html.parser')
    content = bs.find('div', id='mw-content-text').get_text()
    # content = bytes(content, 'UTF-8')
    # content = content.decode('UTF-8')
    print(content)
