#!/usr/bin/env python3

# В файле https://stepik.org/media/attachments/lesson/209723/3.html
# находится одна таблица. Просуммируйте все числа в ней и введите
# в качестве ответа одно число - эту сумму.
# Для доступа к ячейкам используйте возможности BeautifulSoup.


from bs4 import BeautifulSoup
from urllib.request import urlopen


url = "https://stepik.org/media/attachments/lesson/209723/5.html"
html = str(urlopen(url).read().decode('utf-8'))
soup = BeautifulSoup(html, 'html.parser')

numbers = list()
for line in soup.find_all('td'):
    numbers.append(int(line.text))
print(sum(numbers))
