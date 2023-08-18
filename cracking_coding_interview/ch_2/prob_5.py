#!/usr/bin/env python3

import unittest

from linkedlist import CustomLL

"""Given a circular linked list, implement an algorithm which returns node at the beginning of the loop."""

class LLLoopDetector:
	def __init__(self):
		pass


	def detect(self, ll):
		one_step, two_step = ll.head, ll.head

		while two_step and two_step.tail:
			two_step = two_step.tail.tail
			one_step = one_step.tail

			if one_step is two_step:
				break

		one_step = ll.head

		while two_step is not one_step:
			two_step = two_step.tail
			one_step = one_step.tail

		return two_step.value


class TestLLLoopDetector(unittest.TestCase):
	def setUp(self):
		ll_list = [12,13,14,15,16,17,18]
		self.ll = CustomLL()
		for node_val in ll_list:	
			self.ll.add(node_val)

		self.ll.head.head =	self.ll.tail
		self.ll.tail.tail = self.ll.head


	def test_LLoopDetector_detect(self):
		llld = LLLoopDetector()
		self.assertEqual(llld.detect(self.ll), 12)


if __name__ == "__main__":
	unittest.main()