#!/usr/bin/env python3

import json


class TreeStore:
    def __init__(self, items):
        self.tree = dict()
        for item in items:
            id = item['id']
            self.tree[id] = {
                'parent': item['parent'],
                'children': list()
            }
            if 'type' in item.keys():
                self.tree[id]['type'] = item['type']

        self.items = list({'id': 'root'})
        for item in items:
            self.items.append(item)
            id = item['id']
            pid = item['parent']
            if pid != 'root':
                self.tree[pid]['children'].append(item)

    def __str__(self):
        return json.dumps(self.tree)

    def getAll(self):
        return self.items

    def getItem(self, id):
        return self.items[id]

    def getChildren(self, id):
        return self.tree[id]['children']

    def getAllParents(self, id):
        pid = self.tree[id]['parent']
        parents = list()
        while pid != 'root':
            parent = self.items[pid]
            parents.append(parent)
            pid = self.tree[pid]['parent']
        return parents


items = [
    {'id': 1, 'parent': 'root'},
    {'id': 2, 'parent': 1, 'type': 'test'},
    {'id': 3, 'parent': 1, 'type': 'test'},
    {'id': 4, 'parent': 2, 'type': 'test'},
    {'id': 5, 'parent': 2, 'type': 'test'},
    {'id': 6, 'parent': 2, 'type': 'test'},
    {'id': 7, 'parent': 4, 'type': None},
    {'id': 8, 'parent': 4, 'type': None}
]

ts = TreeStore(items)
print('ts.getAll()')
print(ts.getAll())
print()
print('ts.getItem(7)')
print(ts.getItem(7))
print()
print('ts.getChildren(4)')
print(ts.getChildren(4))
print()
print('ts.getChildren(5)')
print(ts.getChildren(5))
print()
print('ts.getAllParents(7)')
print(ts.getAllParents(7))
print()
print('ts')
print(ts)
