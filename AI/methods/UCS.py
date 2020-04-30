# Взвеенный поиск
# Uniform Cost Search


from graph import *


def UCS(Graph, source, target):
    visited = set()
    queue = [(0, source)]
    while queue:
        queue.sort()
        [price_parent, vertex] = queue.pop(0)
        print(vertex, end=" ")
        if vertex not in visited:
            visited.add(vertex)
            for [vertex_child, price] in Graph.graph[vertex]:
                queue.extend([(price + price_parent, vertex_child)])
        if vertex == target:
            return "success"


def UCS_paths(Graph, source, target):
    visited = set()
    queue = [(0, source, [source])]
    while queue:
        queue.sort()
        [price_parent, vertex, path] = queue.pop(0)
        if vertex == target:
            return path
        for [vertex_child, price] in Graph.graph[vertex]:
            if vertex_child not in path:
                    queue.extend([(
                        price + price_parent,
                        vertex_child, path + [vertex_child])])
