#!/usr/bin/env python3

"""
Дан упорядоченный массив arr и число X, нужно найти индекс
максимального элемента arr, не превосходящего X.
Если такого элемента не существует, вернуть -1.
"""

from termcolor import colored


def max_lower_or_equal(array, value):
    if not array or array[0] > value:
        return -1
    i = 0
    left, right = 0, len(array)
    while left + 1 < right:
        mid = (left + right) // 2
        print(left, mid, right, ':', array[mid])
        if array[mid] <= value:
            left = mid
            print(colored('---', 'green'))
        else:
            right = mid
            print(colored('---', 'red'))
    return left


if __name__ == '__main__':
    array = [0, 1, 3, 4, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
    value = 1
    print(max_lower_or_equal(array, value))
