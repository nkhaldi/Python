#!/usr/bin/env python3

"""
Релизвовать класс MaxStack, который будет представлять из себя
стек с константным поиском максимального элемента.
push, pop, max должны работать за O(1).
"""


class MaxStack:

    def __init__(self):
        self.stack = list()
        self.maxValues = [None]

    def push(self, elem):
        self.stack.append(elem)
        if self.maxValues[-1] is None or elem >= self.maxValues[-1]:
            self.maxValues.append(elem)

    def pop(self):
        elem = self.stack.pop(elem)
        if elem == self.maxValues[-1]:
            self.maxValues.pop()
        return elem

    def maximum(self):
        return self.maxValues[-1]
