#!/usr/bin/env python3

# Структура данных граф и взвешенный граф
# Graph & Weight Graph


from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, source, target):
        self.graph[source].append(target)


class WeightGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, source, target, weight):
        self.graph[source].append([target, weight])
