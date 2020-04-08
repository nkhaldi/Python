#!/usr/bin/env python3

# Поиск в глубину
# Depth-First Search


from graph import *


def DFS(Graph, source, target, depth=0):
    print(source, end=" ")
    for vertex in Graph.graph[source]:
        if vertex == target:
            print(vertex)
            return "success"
        elif depth > 10:
            return "failed"
        elif len(Graph.graph[vertex]) > 0:
            depth += 1
            return DFS(Graph, vertex, target, depth)
        else:
            return "failed"


def DFS_paths(Graph, source, target, path=None):
    if path is None:
        path = [source]
    if source == target:
        yield path
    for vertex in set(Graph.graph[source]) - set(path):
        yield from DFS_paths(Graph, vertex, target, path + [vertex])
