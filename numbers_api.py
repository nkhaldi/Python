#!/usr/bin/env python3

"""
В этой задаче вам необходимо воспользоваться API
сайта numbersapi.com
Вам дается набор чисел. Для каждого из чисел
необходимо узнать, существует ли интересный
математический факт об этом числе.
Для каждого числа выведите Interesting, если
для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке,
в каком следуют числа во входном файле.

Примечание:
На данный момент для получения доступа на сайт numbersapi.com
необходимо использовать VPN.
"""

import requests

proxies = {"http": "socks5://127.0.0.1:9050", "https": "socks5://127.0.0.1:9050"}

with open("tests/numbers_api.txt") as fd:
    for number in fd:
        url = f"http://numbersapi.com/{number.strip()}/math?json=true"
        res = requests.get(url, proxies=proxies)
        res = res.json()
        if res["found"]:
            print("Interesting")
        else:
            print("Boring")
