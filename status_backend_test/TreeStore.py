#!/usr/bin/env python3

import json


class TreeStore:
    def __init__(self, items):
        self.tree = dict()
        for item in items:
            id = item["id"]
            self.tree[id] = {"parent": item["parent"], "children": list()}
            if "type" in item.keys():
                self.tree[id]["type"] = item["type"]

        self.items = [{"id": "root"}]
        for item in items:
            self.items.append(item)
            id = item["id"]
            pid = item["parent"]
            if pid != "root":
                self.tree[pid]["children"].append(item)

    def __str__(self, to_json=False):
        if to_json:
            return json.dumps(self.tree)
        return str(self.tree)

    def getAll(self, to_json=False):
        if to_json:
            return json.dumps(self.items[1:])
        return self.items[1:]

    def getItem(self, id, to_json=False):
        if to_json:
            return json.dumps(self.items[id])
        return self.items[id]

    def getChildren(self, id, to_json=False):
        if to_json:
            return json.dumps(self.tree[id]["children"])
        return self.tree[id]["children"]

    def getAllParents(self, id, to_json=False):
        pid = self.tree[id]["parent"]
        parents = list()
        while pid != "root":
            parent = self.items[pid]
            parents.append(parent)
            pid = self.tree[pid]["parent"]

        if to_json:
            return json.dumps(parents)
        return parents
