#!/usr/bin/env python3

# Найти все гиперссылки на текущей странице

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://ru.wikipedia.org/wiki/Python"
html = str(urlopen(url).read().decode('utf-8'))
soup = BeautifulSoup(html, 'html.parser')
for a in soup.find_all('a', href=True):
    print(a['href'])
