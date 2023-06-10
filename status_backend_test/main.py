#!/usr/bin/env python3

from TreeStore import TreeStore

items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None},
]
ts = TreeStore(items)

print("ts.getAll()")
print(ts.getAll())
print()
print("ts.getAll(to_json=True)")
print(ts.getAll(to_json=True))
print("\n" + "-" * 80 + "\n")
print("ts.getItem(7)")
print(ts.getItem(7))
print()
print(ts.getItem(7, to_json=True))
print("\n" + "-" * 80 + "\n")
print("ts.getChildren(4)")
print(ts.getChildren(4))
print()
print("ts.getChildren(4, to_json=True)")
print(ts.getChildren(4, to_json=True))
print("\n" + "-" * 80 + "\n")
print("ts.getChildren(5)")
print(ts.getChildren(5))
print()
print("ts.getChildren(5, to_json=True)")
print(ts.getChildren(5, to_json=True))
print("\n" + "-" * 80 + "\n")
print("ts.getAllParents(7)")
print(ts.getAllParents(7))
print()
print("ts.getAllParents(7, to_json=True)")
print(ts.getAllParents(7, to_json=True))
print("\n" + "-" * 80 + "\n")
print("ts")
print(ts)
print()
print("ts, to_json=True")
print(ts.__str__(to_json=True))
