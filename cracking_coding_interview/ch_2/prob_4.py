#!/usr/bin/env python3

"""
*Q2.4 You have two numbers represented by a linked list,where each node contains a single digit.
 *The digit are stored in reverse order,such that the 1's digit is at the head of the list.
 *Write a function that adds the two numbers thr sum as a linked list.
 *Example:
 *Input:(3->1->5),(5->9->2)
 *Output:8->0->8
 """

import unittest
from linkedlist import CustomLL, CustomLLNode


class LinkedListAdder:
	def __init__(self):
		self.output = CustomLL()
		self.output_sum = 0

	def add_lls(self, ll1, ll2):
		self.output_sum += self._ll_to_digit(ll1)
		self.output_sum += self._ll_to_digit(ll2)

		self._digit_to_ll(self.output_sum)
		return self.output

	def _ll_to_digit(self, ll):
		digits = ""
		
		end = False
		final_round = False
		current = None
		initial_head_check = True
		while not end:
			if final_round:
				end = True

			if initial_head_check:
				initial_head_check = False
				current = ll.head
			else:
				current = current.tail

			if current:
				digits = str(current.value) + digits

			if final_round and end:
				break

			if not current.tail.tail:
				final_round = True

		return int(digits)

	def _digit_to_ll(self, digit):
		digit = str(digit)
		for char in digit:
			self.output.add(int(char))


class TestLinkedListAdder(unittest.TestCase):
	def setUp(self):

		ll1_list = [3,1,5]
		self.ll1 = CustomLL()
		for node_val in ll1_list:	
			self.ll1.add(node_val)
		self.ll1_digit_val = int("".join([str(digit) for digit in ll1_list[::-1]]))

		ll2_list = [5,9,2]
		self.ll2 = CustomLL()
		for node_val in ll2_list:
			self.ll2.add(node_val)
		self.ll2_digit_val = int("".join([str(digit) for digit in ll2_list[::-1]]))

		self.expected_sum_values = self.ll1_digit_val + self.ll2_digit_val

	def test_LinkedListAdder_add_lls(self):
		lla = LinkedListAdder()
		final_ll = lla.add_lls(self.ll1, self.ll2)

		self.assertEqual(lla.output_sum, self.expected_sum_values, "failed to sum")

		self.assertEqual(final_ll.head.value, 8)
		self.assertEqual(final_ll.head.tail.value, 0)
		self.assertEqual(final_ll.head.tail.tail.value, 8)


if __name__ == "__main__":
	unittest.main()
