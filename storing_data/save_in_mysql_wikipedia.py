import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql


conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='wikipedia')
cur = conn.cursor()
cur.execute('USE wikipedia')


def insert_page_if_not_exists(url):
    cur.execute('SELECT * FROM pages WHERE url = %s', url)
    if cur.rowcount == 0:
        cur.execute('INSERT INTO pages (url) VALUES (%s)', url)
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]


def load_pages():
    cur.execute('SELECT * FROM pages')
    pages = [row[1] for row in cur.fetchall()]
    return pages


def insert_link(from_page_id, to_page_id):
    cur.execute('SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s', (int(from_page_id), int(to_page_id)))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)', (int(from_page_id), int(to_page_id)))
        conn.commit()


def get_links(page_url, recursion_level, pages):
    if recursion_level > 0:
        return 

    page_id = insert_page_if_not_exists(page_url)
    html = urlopen('https://en.wikipedia.org{}'.format(page_url))
    bs = BeautifulSoup(html, 'html.parser')
    links = bs.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    links = [link.attrs['href'] for link in links]

    for link in links:
        insert_link(page_id, insert_page_if_not_exists(link))
        if link not in pages:
            pages.append(link)
            get_links(link, recursion_level+1, pages)

    
get_links('/wiki/Kevin_Bacon', 0, load_pages())
cur.close()
conn.close()
