"""
Script saves all images with internal link in folder "images"
"""


import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

download_dir = 'images'
base_url = 'https://w3schools.com'


def get_absolute_url(base, source):
    if source.startswith('https://www.'):
        url = 'https://{}'.format(source[12:])
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = 'https://{}'.format(source[5:])
    else:
        url = '{}/{}'.format(base, source)
    if base not in url:
        return None
    return url


def get_download_path(base, absolute_url, download_directory):
    path = absolute_url.replace('www.', '')
    path = path.replace(base, '')
    path = download_directory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    return path


html = urlopen(base_url)
bs = BeautifulSoup(html, 'html.parser')
download_list = bs.findAll('img', src=True)

for download in download_list:
    file_url = get_absolute_url(base_url, download['src'])
    if file_url is not None:
        print(file_url)

    urlretrieve(file_url, get_download_path(base_url, file_url, download_dir))
