#!/usr/bin/env python3

"""
Вася решил открыть АЗС (заправку). Чтобы оценить уровень конкуренции
он хочет изучить количество заправок в интересующем его районе.
Вася скачал интересующий его кусок карты OSM
https://stepik.org/media/attachments/lesson/245681/map2.osm
и хочет посчитать, сколько на нём отмечено точечных объектов (node),
являющихся заправкой.
В качестве ответа вам необходимо вывести одно число - количество АЗС.
"""

import os
import requests
import xml.etree.ElementTree as ET


osmfile = "tests/map2.osm"
url = "https://stepik.org/media/attachments/lesson/245681/map2.osm"
res = requests.get(url)

if not os.access(osmfile, os.F_OK):
    with open(osmfile, "wb") as f:
        f.write(res.content)

fuels = ET.parse(osmfile).getroot().findall("./node/tag[@v='fuel']")
print(len(fuels))
