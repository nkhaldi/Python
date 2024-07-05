#!/usr/bin/env python3

"""
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A
есть ссылка на B, т. е. внутри A есть тег <a href="B">,
возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует
такой документ C, что из A в C можно перейти за один переход
и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки,
содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода,
иначе выведите No.

Обратите внимание на то, что не все ссылки внутри
HTML документа могут вести на существующие HTML документы.
"""

import re

import requests


def find_ref(link1, link2):
    pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')
    resp = requests.get(link1).text
    for url in pattern.findall(resp):
        curr = requests.get(url).text
        if link2 in pattern.findall(curr):
            return True
    return False


link1 = input()
link2 = input()
print("Yes" if find_ref(link1, link2) else "No")
