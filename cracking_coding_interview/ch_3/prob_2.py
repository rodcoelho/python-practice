#!/usr/bin/env python3
import unittest


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def pop(self):
        ret_val = None

        if self.stack:
            ret_val = self.stack[-1]
            self.stack = self.stack[:-1]

        if self.min_stack:
            if self.min_stack[-1] == ret_val:
                self.min_stack = self.min_stack[:-1]
            
        return ret_val

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif self.min_stack:
            if val < self.min_stack[-1]:
                self.min_stack.append(val)

    def min(self):
        if self.min_stack:
            return self.min_stack[-1]


class TestMinStack(unittest.TestCase):
    def test_MinStack(self):
        ms = MinStack()

        ms.push(3)
        self.assertEqual(ms.min(), 3)
        ms.push(2)
        self.assertEqual(ms.min(), 2)
        ms.push(1)
        self.assertEqual(ms.min(), 1)

        self.assertEqual(ms.pop(), 1)
        self.assertEqual(ms.min(), 2)

        self.assertEqual(ms.pop(), 2)
        self.assertEqual(ms.min(), 3)


if __name__ == "__main__":
    unittest.main()