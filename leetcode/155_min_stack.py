"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""

import unittest

class MinStack:

    def __init__(self):
        self.stack = []
        self.currentMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.currentMin or val < self.currentMin[-1]:
            self.currentMin.append(val)
        else:
            self.currentMin.append(self.currentMin[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.currentMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currentMin[-1]


class TestMinStack(unittest.TestCase):
    def test_stack(self):
        ms = MinStack()
        
        calls = ["push","push","push","getMin","pop","top","getMin"]
        args = [[-2],[0],[-3],[],[],[],[]]
        expecteds = [None,None,None,-3,None,0,-2]

        for call, arg, expected in zip(calls, args, expecteds):

            method = getattr(ms, call)
            actual = method(*arg)
            self.assertEqual(actual, expected)


unittest.main()
