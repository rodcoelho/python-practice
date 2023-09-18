#!/usr/bin/env python3

"""
Implement a function to check if a tree is balanced (i.e. no two leaf nodes differ in distance to the root by more than 1)
"""

import unittest

class Node:
    def __init__(self, val, parent, rnode, lnode):
        self.parent = parent
        self.rnode = rnode
        self.lnode = lnode
        self.val = val


class MyTree:
    def __init__(self, root_val):
        self.root = Node(root_val, None, None, None)
        self.root.level = 1

    def add(self, val):
        done = False
        current_node = None
        while not done:
            if not current_node:
                current_node = self.root
            # determine if keep going
            if current_node.rnode and val > current_node.val:
                current_node = current_node.rnode
                continue
            elif current_node.lnode and val < current_node.val:
                current_node = current_node.lnode
                continue

            # determine if at end of tree
            if val > current_node.val and not current_node.rnode:
                # add node to right
                current_node.rnode = Node(val, current_node, None, None)
            elif val < current_node.val and not current_node.lnode:
                # add node to left
                current_node.lnode = Node(val, current_node, None, None)
            done = True

    def find(self, val):
        done = False
        current_node = None
        while not done:
            if not current_node:
                current_node = self.root
            
            if current_node.val == val:
                return True
            
            # determine if keep going
            if current_node.rnode and val > current_node.val:
                current_node = current_node.rnode
                continue
            elif current_node.lnode and val < current_node.val:
                current_node = current_node.lnode
                continue

            return False

    def is_balanced(self):

        def height(node):
            if node is None:
                return 0
            # traverse left w/recursive
            left_height = height(node.lnode)

            # traverse right w/recursive
            right_height = height(node.rnode)

            # find unbalance subtree and return
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1

        # start off traversal with root
        return height(self.root) != -1


class TestMyTree(unittest.TestCase):
    def test_mytree(self):
        """
        10
    3       19
  1  5     17  21
                100
                  101
        
        """

        mt = MyTree(10)
        mt.add(3)
        mt.add(5)
        mt.add(19)
        mt.add(17)
        mt.add(21)
        mt.add(1)

        self.assertEqual(mt.root.val, 10)
        
        current_node = mt.root.rnode
        self.assertEqual(current_node.val, 19)
        self.assertEqual(current_node.rnode.val, 21)
        self.assertEqual(current_node.lnode.val, 17)

        current_node = mt.root.lnode
        self.assertEqual(current_node.val, 3)
        self.assertEqual(current_node.rnode.val, 5)
        self.assertEqual(current_node.lnode.val, 1)

        self.assertEqual(mt.find(3), True)
        self.assertEqual(mt.find(1), True)
        self.assertEqual(mt.find(10), True)
        self.assertEqual(mt.find(19), True)
        self.assertEqual(mt.find(21), True)
        self.assertEqual(mt.find(17), True)
        self.assertEqual(mt.find(100), False)

        mt.add(100)
        self.assertEqual(mt.find(100), True)
        self.assertEqual(mt.is_balanced(), True)

        mt.add(101)
        self.assertEqual(mt.find(101), True)
        self.assertEqual(mt.is_balanced(), False)


if __name__ == "__main__":
    unittest.main()
