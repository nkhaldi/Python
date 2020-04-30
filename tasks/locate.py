#!/usr/bin/env python3

# Скрипт для определения координат и местоположения по MAC-адресу
# Для определения MAC-адресов можно воспользоваться следующими командами:
# ifconfig | grep -E '(\w\w:){5}\w\w' | awk -F ' ' '{print $2}'
# arp -a | grep -E '(\w\w:){5}\w\w' | awk -F ' ' '{print $4}'

import json
from urllib.request import urlopen

macs = list()
while True:
    try:
        inp = input()
        macs.append(inp)
    except:
        break

for mac in macs:
    url = "https://api.mylnikov.org/geolocation/wifi?v=1.2&bssid=" + mac
    html = str(urlopen(url).read().decode('utf-8'))
    res = json.loads(html)
    if res['result'] == 200:
        print('lat:', res['data']['lat'])
        print('lon:', res['data']['lon'])
        print('location:', res['data']['location'])
    else:
        print(res['result'])
