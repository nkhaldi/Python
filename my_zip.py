#!/usr/bin/env python3

"""
Реализовать built-in функцию zip(), принимающую набор iterable объектов (I1, I2, ..., In)
и возвращающую кортежи из соответствующих друг другу элементов каждой коллекции:
(I1[0], ..., In[0]), (I1[1], ..., In[1]), ...
Количество кортежей на выходе ограничено длиной самого короткого iterable-аргумента.
"""


def my_zip(*objects):
    iterators = [iter(obj) for obj in objects]

    while True:
        try:
            current_tuple = tuple([next(it) for it in iterators])
            yield current_tuple
        except StopIteration:
            break


l1 = [1, 2, 3, 4, 5]
l2 = [2, 3, 4, 5]
l3 = [3, 4, 5]

result = my_zip(l1, l2, l3)

print(*result)
