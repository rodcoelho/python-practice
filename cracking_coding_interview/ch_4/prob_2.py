#!/usr/bin/env python3

import unittest
from collections import deque

"""
Given a graph, design a function to find out whether there is a route between two nodes.

VISUAL OF TEST GRAPH

# A -- B
# |    |
# C -- D
# |
# E -- F -- G -- H
#      | \
#      O   I -- J -- K
#               |
#               L

# P -- Q
# |  /
# R
"""


class MyGraph:
    def __init__(self, graph):
        self.graph = graph

    def is_route(self, start, end, visited=None):
        if visited == None:
            visited = set()
        
        for node in self.graph[start]:
            
            if node not in visited:
                visited.add(node)

                # recurse into the node by making the node as the new start
                if node == end or self.is_route(node, end, visited):
                    return True
        return False


class TestMyGraph(unittest.TestCase):
    def setUp(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["D", "E"],
            "D": ["B", "C"],
            "E": ["C", "F"],
            "F": ["E", "O", "I", "G"],
            "G": ["F", "H"],
            "H": ["G"],
            "I": ["F", "J"],
            "O": ["F"],
            "J": ["K", "L", "I"],
            "K": ["J"],
            "L": ["J"],
            "P": ["Q", "R"],
            "Q": ["P", "R"],
            "R": ["P", "Q"],
        }

        self.test_cases = [
            ("A", "L", True),
            ("A", "B", True),
            ("H", "K", True),
            ("L", "D", True),
            ("P", "Q", True),
            ("Q", "P", True),
            ("Q", "G", False),
            ("R", "A", False),
            ("P", "B", False),
        ]

    def test_is_route(self):
        mg = MyGraph(self.graph)

        for [start, end, expected] in self.test_cases:
            actual = mg.is_route(start, end)
            
            self.assertEqual(actual, expected, (actual, expected))


if __name__ == "__main__":
    unittest.main()