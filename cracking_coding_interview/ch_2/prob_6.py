#!/usr/bin/env python3

import unittest

from linkedlist import CustomLL


class PalindromeChecker:
    """
    Determine if a linked list is a palindrome
    """

    def __init__(self, ll):
        self.ll = CustomLL()
        for val in ll:
            self.ll.add(val)

    def check(self):
        if not self.ll.head:
            return True

        two_step, one_step = self.ll.head, self.ll.head

        while two_step and two_step.node_tail is not None:
            two_step = two_step.node_tail.node_tail
            one_step = one_step.node_tail
        
        middle = one_step.value

        forward, backward = self.ll.head, self.ll.tail

        while forward.value != middle and backward.value != middle:

            if forward.value != backward.value:
                return False
            
            forward = forward.node_tail
            backward = backward.node_head
        
        if forward.value != backward.value:
            return False

        return True


class TestPalindromeChecker(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1, 2, 3, 4, 3, 2, 1], True),
            ([1, 2, 3, 3, 2, 1], True),
            ([1], True),
            (["a", "a"], True),
            (["aba"], True),
            ([], True),
            ([1, 2, 3, 4, 5], False),
            ([1, 2], False),
        ]


    def test_PalindromeChecker_check(self):
        for test_case in self.test_cases:

            ll, expected = test_case
            pc = PalindromeChecker(ll)

            self.assertEqual(pc.check(), expected, "fail {} {}".format(ll, expected))


if __name__ == "__main__":
    unittest.main()
