#!/usr/bin/env python3

"""
Вася планирует карьеру и переезд. Для это составил таблицу, в которой
для каждого региона записал зарплаты для разных интересные ему профессий.
Таблица доступна по ссылке
https://stepik.org/media/attachments/lesson/245267/salaries.xlsx.
Выведите название региона с самой высокой медианной зарплатой и,
через пробел, название профессии с самой высокой средней зарплатой
по всем регионам.
"""

from statistics import mean, median

import requests
import xlrd

url = "https://stepik.org/media/attachments/lesson/245267/salaries.xlsx"
request = requests.get(url)
workbook = xlrd.open_workbook(file_contents=request.content)
sheet = workbook.sheet_by_index(0)

salary = 0
for row in range(1, sheet.nrows):
    medi_sal = median(sheet.row_values(row)[1:])
    if medi_sal > salary:
        salary = medi_sal
        region = sheet.cell(row, 0)

salary = 0
for col in range(1, sheet.ncols):
    mean_sal = mean(sheet.col_values(col)[1:])
    if mean_sal > salary:
        salary = mean_sal
        prof = sheet.cell(0, col)

print(region.value, prof.value)
