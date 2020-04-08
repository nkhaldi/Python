#!/usr/bin/env python3

# Разработать программу, которая будет как "магический" шар
# выдавать случайный результат:
# Да, Нет, Скорее всего да, Скорее всего нет
# Возможно, Имеются перспективы, Вопрос задан неверно.


from random import randint

answers = [
        'Да',
        'Нет',
        'Скорее всего да',
        'Скорее всего нет',
        'Возможно',
        'Имеются перспективы',
        'Вопрос задан неверно'
]

print("Что вы хотите узнать?")
question = input()
index = int(randint(0, 7))
print(answers[index])
