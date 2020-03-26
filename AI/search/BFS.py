# Поиск в ширину
# Breadth-First Search


from graph import *


def BFS(Graph, source, target):
    visited = set()
    queue = [source]
    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(Graph.graph[vertex]) - visited)
        if vertex == target:
            return "success"


def BFS_paths(Graph, source, target):
    queue = [(source, [source])]
    while queue:
        (vertex, path) = queue.pop(0)
        for vertex_next in set(Graph.graph[vertex]) - set(path):
            if vertex_next == target:
                yield path + [vertex_next]
            else:
                queue.append((vertex_next, path + [vertex_next]))
