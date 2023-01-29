#!/usr/bin/env python3

"""
Функця бинарного поиска
"""


def binary_search(array, target):
    left, right = 0, len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid
    return False
