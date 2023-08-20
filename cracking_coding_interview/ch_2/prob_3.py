#!/usr/bin/env python3

import unittest

from linkedlist import CustomLLNode, CustomLL

"""Implement an algorithm to delete a node in the middle of a single linked list, given only access to that node."""


class NodeDeleter:
	def __init__(self):
		pass

	def delete(self, node):
		head = node.node_head
		tail = node.node_tail
		head.node_tail = tail
		tail.node_head = head


class TestNodeDeleter(unittest.TestCase):
	def setUp(self):
		self.cll = CustomLL()
		for l in [1, 2, 3, 4]:
			self.cll.add(l)

		self.middle_node = self.cll.add(5)
		self.middle_node_value = self.middle_node.value

		for l in [6, 7, 8, 9]:
			self.cll.add(l)


	def test_NodeDeleter_delete(self):
		node_deleter = NodeDeleter()
		node_deleter.delete(self.middle_node)

		end = False
		found_values = []
		current = None
		initial_head_check = True
		while not end:
			if initial_head_check:
				initial_head_check = False
				current = self.cll.head
			else:
				current = current.node_tail

			self.assertNotEqual(current.value, self.middle_node_value, "failed, we found the deleted node!")
			found_values.append(current.value)

			if not current.node_tail.node_tail:
				end = True

		self.assertNotIn(5, found_values)


if __name__ == "__main__":
	unittest.main()
