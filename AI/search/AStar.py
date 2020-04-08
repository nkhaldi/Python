#!/usr/bin/env python3

# Алгоритм A*
# A* search


from graph import *


def A_star(Graph, source, target):
    visited = set()
    queue = [(0 + heurisric[source], 0, source)]
    while queue:
        queue.sort()
        print(queue)
        (hprice_parent, price_parent, vertex) = queue.pop(0)
        if vertex == target:
            print("lowest price = ", price_parent)
            return "success!"
        if (vertex, price_parent) not in visited:
            visited.add((vertex, price_parent))
            for [vertex_child, price] in Graph.graph[vertex]:
                queue.extend([(
                    price + price_parent + heurisric[vertex_child],
                    price + price_parent, vertex_child
                )])


def A_star_paths(Graph, source, target):
    queue = [(0 + heurisric[source], 0, source, [source])]
    while queue:
        queue.sort()
        (hprice_parent, price_parent, vertex, path) = queue.pop(0)
        for (vertex_child, price_child) in Graph.graph[vertex]:
            if vertex_child not in path:
                if vertex_child == target:
                    yield (path + [vertex_child], price_parent + price_child)
                else:
                    queue.append((
                        price_child + price_parent + heurisric[vertex_child],
                        price_child + price_parent,
                        vertex_child,
                        path + [vertex_child]
                    ))
