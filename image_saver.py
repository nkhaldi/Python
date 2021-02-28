#!/usr/bin/env python3

# Скрипт для сохранения изображений по url


import requests


img_url = input()
res = requests.get(img_url)
with open("img.png", "wb") as f:
    f.write(res.content)
