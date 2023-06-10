#!/usr/bin/env python3

"""
Дан упорядоченный массив arr и число X, нужно найти индекс
максимального элемента arr, не превосходящего X.
Если такого элемента не существует, вернуть -1.
"""


def max_lower_or_equal(array, value):
    if not array or array[0] > value:
        return -1

    left, right = 0, len(array)
    while left + 1 < right:
        mid = (left + right) // 2
        if array[mid] <= value:
            left = mid
        else:
            right = mid
    return left


if __name__ == "__main__":
    value = int(input())
    array = list(map(int, input().split()))
    print(max_lower_or_equal(array, value))
