#!/usr/bin/env python3

import unittest

from linkedlist import CustomLL


class IntersectionHandler:
    def __init__(self):
        pass

    def _get_len(self, ll):
        ll_len = 0
        current_node = ll.head
        while current_node and current_node.node_tail:
            ll_len += 1
            current_node = current_node.node_tail
        return ll_len


    def handle(self, ll1, ll2):
        ll1_len, ll2_len = self._get_len(ll1), self._get_len(ll2)

        shorter, longer = ll1, ll2
        if ll1_len > ll2_len:
            shorter, longer = ll2, ll1

        diff = abs(ll1_len - ll2_len)

        current_shorter, current_longer = shorter.head, longer.head

        for _ in range(diff):
            current_longer = current_longer.node_tail

        while current_longer.value != current_shorter.value:
            current_longer = current_longer.node_tail
            current_shorter= current_shorter.node_tail
        
        return current_shorter


class TestIntersectionHandler(unittest.TestCase):
    def setUp(self):
        self.shared_ll = CustomLL()
        self.ll1 = CustomLL()
        self.ll2 = CustomLL()

        for node in [2, 3, 4, 5]:
            self.shared_ll.add(node)

        for node in [10, 11, 12, 13, 14, 15]:
            self.ll1.add(node)

        for node in [20, 21, 22]:
            self.ll2.add(node)

        self.ll1.tail.node_tail = self.shared_ll.head
        self.ll1.tail = self.shared_ll.tail

        self.ll2.tail.node_tail = self.shared_ll.head
        self.ll2.tail = self.shared_ll.tail
    
    def test_IntersectionHandler_handle(self):
        ih = IntersectionHandler()
        node = ih.handle(self.ll1, self.ll2)
        self.assertEqual(node.value, 2)
        

if __name__ == "__main__":
    unittest.main()
