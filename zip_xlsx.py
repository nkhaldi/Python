#!/usr/bin/env python3

"""
Главный бухгалтер компании "Рога и копыта" случайно удалил ведомость
с начисленной зарплатой. К счастью, у него сохранились расчётные листки
всех сотрудников. Помогите по этим расчётным листкам восстановить
зарплатную ведомость. Архив с расчётными листками доступен по ссылке
https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip
Ведомость должна содержать 1000 строк, в каждой строке должно быть
указано ФИО сотрудника и, через пробел, его зарплата.
Сотрудники должны быть упорядочены по алфавиту.
"""

import os
import xlrd
import zipfile


payroll = {}
zipdir = 'tests/xlsx_files'
zipname = 'tests/rogaikopyta.zip'

if zipdir not in os.listdir():
    zipfile = zipfile.ZipFile(zipname)
    zipfile.extractall(zipdir)
    zipfile.close()
path = f"{os.getcwd()}/{zipdir}/"

for zfile in os.listdir(zipdir):
    wb = xlrd.open_workbook(path + zfile)
    sh = wb.sheet_by_name(wb.sheet_names()[0])
    payroll[sh.row_values(1)[1]] = int(sh.row_values(1)[3])

with open("tests/zip_xlsx.txt", 'w', encoding='utf-8') as fd:
    for row in sorted(payroll.items(), key=lambda item: item[0]):
        fd.write(f"{row[0]} {str(row[1])}\n")
