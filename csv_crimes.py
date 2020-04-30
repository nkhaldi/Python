#!/usr/bin/env python3

# Вам дана частичная выборка из датасета зафиксированных преступлений,
# совершенных в городе Чикаго с 2001 года по настоящее время.
# Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано
# максимальное число раз в 2015 году.


import csv


def find_max_crime(fname):
    crimes = dict()
    with open(fname) as fd:
        reader = csv.reader(fd)
        for row in reader:
            crime_type = row[5]
            if crime_type in crimes:
                crimes[crime_type] += 1
            else:
                crimes[crime_type] = 1
    return crimes


crimes = find_max_crime("tests/Crimes.csv")
for key in crimes:
    print(key, "->", crimes[key])
print("\nMax is", max(crimes, key=crimes.get))
