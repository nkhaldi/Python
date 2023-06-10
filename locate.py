#!/usr/bin/env python3

"""
Скрипт для определения координат и местоположения по MAC-адресу
"""

import json
from http.client import responses
from urllib.request import urlopen


macs = list()
while True:
    try:
        inp = input()
        macs.append(inp.upper())
    except Exception:
        break

for mac in macs:
    url = "https://api.mylnikov.org/geolocation/wifi?v=1.2&bssid=" + mac
    html = str(urlopen(url).read().decode("utf-8"))
    res = json.loads(html)
    print(responses[res["result"]])
    if res["result"] == 200:
        print("lat:", res["data"]["lat"])
        print("lon:", res["data"]["lon"])
        print("location:", res["data"]["location"])
