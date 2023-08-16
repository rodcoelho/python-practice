#!/usr/bin/env python3


from structlinks.DataStructures import LinkedList

import unittest

from linkedlist import CustomLLNode, CustomLL


"""
Implement an algorithm to find thr Nth to last element of a singly linked list.
"""


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

