#!/usr/bin/env python3
"""
Васю назначили завхозом в туристической группе и он подошёл к подготовке
ответственно, составив справочник продуктов с указанием калорийности
на 100 грамм, а также содержание белков, жиров и углеводов на 100 грамм
продукта. Ему не удалось найти всю информацию, поэтому некоторые ячейки
остались незаполненными (можно считать их значение равным нулю).
Также он использовал какой-то странный офисный пакет и разделял целую
и дробную часть чисел запятой. Таблица доступна по ссылке
https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx
https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx

Вася составил раскладку по продуктам на один день (она на листе "Раскладка")
с указанием названия продукта и его количества в граммах. Посчитайте 4 числа:
суммарную калорийность и граммы белков, жиров и углеводов.
Числа округлите до целых вниз и введите через пробел.
"""

import requests
import xlrd

url = "https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx"
request = requests.get(url)
workbook = xlrd.open_workbook(file_contents=request.content)
directory = workbook.sheet_by_name(workbook.sheet_names()[0])
layout = workbook.sheet_by_name(workbook.sheet_names()[1])

res = [0, 0, 0, 0]
for i in range(1, layout.nrows):
    name, mass = layout.row_values(i)
    for j in range(1, directory.nrows):
        if name == directory.row_values(j)[0]:
            params = directory.row_values(j, 1)
            summ = [par * mass / 100 if par else 0 for par in params]
            res = [x + y for x, y in zip(res, summ)]
print(*map(int, res))
