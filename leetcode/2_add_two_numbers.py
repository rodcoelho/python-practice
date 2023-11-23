"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from typing import Optional, List
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbersPythonic(self, l1: Optional[List], l2: Optional[List]) -> Optional[List]:
        stringified_l1 = [str(char) for char in l1]
        stringified_l2 = [str(char) for char in l2]
        normalized_l1 = int("".join(stringified_l1[::-1]))
        normalized_l2 = int("".join(stringified_l2[::-1]))
        normalized_sum = str(normalized_l1 + normalized_l2)
        return [int(char) for char in normalized_sum][::-1]

    def addTwoNumbersLL(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll1_head = ListNode(l1[0], None)
        ll2_head = ListNode(l2[0], None)

        current_l1 = ll1_head
        for i in range(1, len(l1)):
            new_node = ListNode(l1[i], None)
            current_l1.next = new_node
            current_l1 = new_node

        current_l2 = ll2_head
        for i in range(1, len(l2)):
            new_node = ListNode(l2[i], None)
            current_l2.next = new_node
            current_l2 = new_node

        max_len = max(len(l1), len(l2))

        new_ll_head = None
        current_new_node = new_ll_head
        current_l1 = ll1_head
        current_l2 = ll2_head
        carry_over = 0
        for i in range(max_len):

            if new_ll_head is None:
                sum = current_l1.val + current_l2.val
                if sum >= 10:
                    stringified_sum = str(sum)
                    sum = int(stringified_sum[1])
                    carry_over = int(stringified_sum[0])
                new_ll_head = ListNode(val=sum, next=None)
                current_new_node = new_ll_head
                current_l1 = current_l1.next
                current_l2 = current_l2.next
            else:
                l1_val = current_l1.val if current_l1 is not None else 0
                l2_val = current_l2.val if current_l2 is not None else 0
                sum = l1_val + l2_val + carry_over
                if sum >= 10:
                    stringified_sum = str(sum)
                    sum = int(stringified_sum[1])
                    carry_over = int(stringified_sum[0])
                else:
                    carry_over = 0
                new_ll_node = ListNode(val=sum, next=None)
                current_new_node.next = new_ll_node
                current_new_node = new_ll_node
                current_l1 = current_l1.next if current_l1 is not None else None
                current_l2 = current_l2.next if current_l2 is not None else None

        if carry_over > 0:
            new_ll_node = ListNode(val=carry_over, next=None)
            current_new_node.next = new_ll_node

        final_ll = []
        next_is_None = False
        current_node = new_ll_head
        while not next_is_None:
            if current_node.next is None:
                next_is_None = True
                final_ll.append(current_node.val)
            else:
                final_ll.append(current_node.val)
                current_node = current_node.next

        return final_ll


class TestSolution(unittest.TestCase):
    def testAddTwoNumbers(self):
        s = Solution()

        l1 = [2,4,3]
        l2 = [5,6,4]
        expected = [7,0,8]
        actual = s.addTwoNumbersLL(l1, l2)
        self.assertEqual(actual, expected)
        actual = s.addTwoNumbersPythonic(l1, l2)
        self.assertEqual(actual, expected)

        l1 = [0]
        l2 = [0]
        expected = [0]
        actual = s.addTwoNumbersLL(l1, l2)
        self.assertEqual(actual, expected)
        actual = s.addTwoNumbersPythonic(l1, l2)
        self.assertEqual(actual, expected)
        

        l1 = [9,9,9,9,9,9,9]
        l2 = [9,9,9,9]
        expected = [8,9,9,9,0,0,0,1]
        actual = s.addTwoNumbersLL(l1, l2)
        self.assertEqual(actual, expected)
        actual = s.addTwoNumbersPythonic(l1, l2)
        self.assertEqual(actual, expected)

unittest.main()
