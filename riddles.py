#!/usr/bin/env python3

"""
Разработать программу, которая будет задавать вам загадки,
а вы должны будете угадать правильный ответ.
"""


def parse(file_name):
    riddles = dict()
    with open(file_name) as fd:
        for line in fd:
            temp = line.split('#')
            riddles[temp[0]] = temp[1][0:-1]
    return riddles


if __name__ == "__main__":
    riddles = parse("tests/riddles.txt")
    for riddle in riddles.keys():
        print('~' * 50)
        print(riddle)
        ans = input().lower()
        if ans == riddles[riddle].lower():
            print("Верно!")
        else:
            print("Неверно")
            print("Ответ:", riddles[riddle])
