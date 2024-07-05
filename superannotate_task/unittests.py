#!/usr/bin/env python3

import unittest

import task1 as t1
import task2 as t2
import task3 as t3


class SuperAnnotateTests(unittest.TestCase):
    def test_task1(self):
        tests = {
            "qwe": 0,
            "q1w2e3": 6,
            "11-22+33": 22,
            "100-100": 0,
            "qwe0qwe": 0,
            "-100#^sdfkj8902w3ir021@swf-20": 8806,
            "": 0,
        }
        for key in tests.keys():
            print(f"{key} = {tests[key]}")
            self.assertEqual(t1.get_numbers_sum(key), tests[key])

    def test_task2(self):
        tests = {
            "the lazy dog jumped over the quick brown fox": "vjg ncba fqi lworgf qxgt vjg swkem dtqyp hqz",
            "Narek": "Pctgm",
            "0123456789": "0123456789",
            "qWeRtY123": "sYgTvA123",
            "": "",
        }
        for key in tests.keys():
            self.assertEqual(t2.caesar_encpypt(key, 2), tests[key])

    def test_task3(self):
        graph = {
            "A": ["B", "C"],
            "B": ["C", "D"],
            "C": ["D"],
            "D": ["C"],
            "E": ["F"],
            "F": ["C"],
        }
        self.assertEqual(t3.find_shortest_path(graph, "A", "B"), ["A", "B"])
        self.assertEqual(t3.find_shortest_path(graph, "A", "D"), ["A", "B", "D"])
        self.assertEqual(t3.find_shortest_path(graph, "F", "D"), ["F", "C", "D"])
        self.assertEqual(t3.find_shortest_path(graph, "A", "E"), [])
        self.assertEqual(t3.find_shortest_path(graph, "A", "A"), ["A"])
        self.assertEqual(t3.find_shortest_path(graph, "G", "H"), [])


if __name__ == "__main__":
    unittest.main()
