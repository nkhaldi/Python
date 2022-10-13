#!/usr/bin/env python3

"""
Целое положительное число называется простым,
если оно имеет ровно два различных делителя,
то есть делится только на единицу и на само себя.

Реализуйте функцию-генератор primes,
которая будет генерировать простые числа
в порядке возрастания, начиная с числа 2.
"""


def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for el in range(3, num // 2, 2):
        if num % el == 0:
            return False
    return True


def primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1
