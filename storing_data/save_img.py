from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
image_location = bs.find('a', {'id': 'logo'}).find('img')['src']
print(image_location)
urlretrieve(image_location, 'logo.jpg')
