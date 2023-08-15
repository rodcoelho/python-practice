#!/usr/bin/env python3

import unittest

from structlinks.DataStructures import LinkedList


"""
Implement an algorithm to find thr Nth to last element of a singly linked list.
"""


class CustomLLNode:
	def __init__(self, value):
		self.value = value
		self.head = None
		self.tail = None


class CustomLL:
	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, value):
		if self.head:
			n = CustomLLNode(value)
			old_n = self.tail
			old_n.tail=n
			n.head=old_n
			self.tail = n
		else:
			n = CustomLLNode(value)
			self.head = n
			self.tail = n

	def pop(self):
		ret_val = None
		if self.tail == self.head:
			ret_val = self.head
			self.tail, self.head = None, None
		if self.tail:
			ret_val = self.tail
			new_t = self.tail.head
			new_t.tail = None
			self.tail = new_t
		return ret_val.value

	def get_kth_node(self, k):
		current = None
		for i in range(k):
			if i == 0:
				current = self.head
				last_val = self.head.value
			else:
				current = current.tail
				
		return current.value

	def get_kth_node_rev(self, k):
		current = None
		for i in range(k):
			if i == 0:
				current = self.tail
				last_val = self.tail.value
			else:
				current = current.head
				
		return current.value


class LinkedListFinder:
	def find_using_structlinks(self, ll, k):
		self.linkedlist = LinkedList(ll)
		return self.linkedlist[-k]


class TestLinkedListFinder(unittest.TestCase):
	def setUp(self):
		self.test_cases = (
			# list, k, expected
			((10, 20, 30, 40, 50), 1, 50),
			((10, 20, 30, 40, 50), 5, 10),
		)

	def test_find_using_structlinks(self):
		for test_case in self.test_cases:

			ll, k, expected = test_case

			llf = LinkedListFinder()

			self.assertEqual(llf.find_using_structlinks(ll, k), expected, "failed {} {} {}".format(ll, k, expected))

	def test_find_using_custom_linked_list(self):
		for test_case in self.test_cases:

			ll, k, expected = test_case

			cll = CustomLL()

			for l in ll:
				cll.add(l)

			self.assertEqual(cll.get_kth_node_rev(k), expected, "failed {} {} {}".format(ll, k, expected))



if __name__ == "__main__":
	unittest.main()

