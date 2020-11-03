#!/usr/bin/env python3

# Васю назначили завхозом в туристической группе и он подошёл к подготовке
# ответственно, составив справочник продуктов с указанием калорийности
# на 100 грамм, а также содержание белков, жиров и углеводов на 100 грамм
# продукта. Ему не удалось найти всю информацию, поэтому некоторые ячейки
# остались незаполненными (можно считать их значение равным нулю).
# Также он использовал какой-то странный офисный пакет и разделял целую
# и дробную часть чисел запятой. Таблица доступна по ссылке
# https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx

# Вася хочет минимизировать вес продуктов и для этого брать самые
# калорийные продукты. Помогите ему и упорядочите продукты по убыванию
# калорийности. В случае, если продукты имеют одинаковую калорийность -
# упорядочите их по названию. В качестве ответа необходимо сдать названия
# продуктов, по одному в строке.


import xlrd
import requests


url = 'https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx'
request = requests.get(url)
workbook = xlrd.open_workbook(file_contents=request.content)
sheet = workbook.sheet_by_index(0)

prods = [sheet.row_values(row)[0:2] for row in range(1, sheet.nrows)]
sorted_prods = sorted(prods, key=lambda x: (-x[1], x[0]))
for prod in sorted_prods:
    print(prod[0])
