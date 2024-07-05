#!/usr/bin/env python3

"""
Вам дана в архиве (ссылка) файловая структура, состоящая
из директорий и файлов.
Вам необходимо распаковать этот архив, и затем найти в данной
файловой структуре все директории, в которых есть хотя бы один файл
с расширением ".py".
Ответом на данную задачу будет являться файл со списком
таких директорий, отсортированных в лексикографическом порядке.
"""

import os


def find_dirs(fname):
    res = list()
    for curr, dirs, files in os.walk(fname):
        if list(filter(lambda x: x.endswith(".py"), files)):
            res.append("{}".format(curr))
    res.sort()
    return res


dirs = find_dirs("tests/main")
for dr in dirs:
    print(dr)
