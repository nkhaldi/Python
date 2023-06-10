#!/usr/bin/env python3

"""
В OpenStreetMap XML встречаются теги node, которые соответствуют
некоторым точкам на карте. Ноды могут не только обозначать какой-то
точечный объект, но и входить в состав way (некоторой линии,
возможно замкнутой) и не иметь собственных тегов.
Для доступного по ссылке фрагмента карты посчитайте, сколько node имеет
хотя бы один вложенный тэг tag, а сколько - не имеют.
В качестве ответа введите два числа, разделённых пробелом.
https://stepik.org/media/attachments/lesson/245678/map1.osm
"""

import os
import wget
import xml.etree.ElementTree as ET


osmfile = "tests/map1.osm"
url = "https://stepik.org/media/attachments/lesson/245678/map1.osm"

if not os.access(osmfile, os.F_OK):
    wget.download(url, out="tests/")
    print()

taged = 0
empty = 0
root = ET.parse(osmfile).getroot()
for child in root.findall("node"):
    if child.find("tag") is None:
        empty += 1
    else:
        taged += 1
print(taged, empty)
