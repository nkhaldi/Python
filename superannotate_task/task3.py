#!/usr/bin/env python3


def find_shortest_path(graph, start, end):
    if start == end:
        return [start]

    paths = [[start]]
    visited = {start}

    index = 0
    while index < len(paths):
        path = paths[index]
        current = path[-1]
        vertices = graph[current]

        if end in vertices:
            path.append(end)
            return path

        for vertex in vertices:
            if vertex not in visited:
                new_path = path.copy()
                new_path.append(vertex)
                paths.append(new_path)
                visited.add(vertex)

        index += 1

    return []


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']
    }

    start, end = 'A', 'D'
    shortest_path = find_shortest_path(graph, start, end)
    print(f"The shortest path from {start} to {end}:")
    if shortest_path:
        print(' -> '.join(shortest_path))
        print("Path lingth:", len(shortest_path))
    else:
        print("None")
