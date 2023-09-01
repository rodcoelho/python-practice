#!/usr/bin/env python3

import unittest

"""
Implement a MyQueue(FIFO) class which implements a queue using two stacks(FILO).
"""

class MyStack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if not self.stack:
            return None
        ret_val = self.stack[-1]
        self.stack = self.stack[:-1]
        return ret_val

    def push(self, val):
        self.stack.append(val)


class MyQueue:
    def __init__(self):
        self.out_q = MyStack()
        self.in_q = MyStack()
        self.receiving = True

    def enqueue(self, val):
        if self.receiving:
            self.in_q.push(val)
        else:
            self.receiving = True

            flipping = True
            while flipping:
                ele = self.out_q.pop()
                if ele:
                    self.in_q.push(ele)
                else:
                    flipping = False
            
            self.in_q.push(val)

    def dequeue(self):
        if self.receiving:
            self.receiving = False
        else:
            return self.out_q.pop()
        
        flipping = True
        while flipping:
            ele = self.in_q.pop()
            if ele:
                self.out_q.push(ele)
            else:
                flipping = False
            
        return self.out_q.pop()



class TestMyQueue(unittest.TestCase):
    def test_MyQueue(self):
        
        mq = MyQueue()

        mq.enqueue(1)
        mq.enqueue(2)
        mq.enqueue(3)
        self.assertEqual(mq.in_q.stack, [1,2,3])
        self.assertEqual(mq.out_q.stack, [])

        actual = mq.dequeue()
        self.assertEqual(actual, 1)
        self.assertEqual(mq.in_q.stack, [])
        self.assertEqual(mq.out_q.stack, [3,2])

        actual = mq.dequeue()
        self.assertEqual(actual, 2)
        self.assertEqual(mq.in_q.stack, [])
        self.assertEqual(mq.out_q.stack, [3])

        mq.enqueue(4)
        self.assertEqual(mq.in_q.stack, [3,4])
        self.assertEqual(mq.out_q.stack, [])

        mq.enqueue(5)
        self.assertEqual(mq.in_q.stack, [3,4,5])
        self.assertEqual(mq.out_q.stack, [])

        actual = mq.dequeue()
        self.assertEqual(actual, 3)
        self.assertEqual(mq.in_q.stack, [])
        self.assertEqual(mq.out_q.stack, [5,4])

        actual = mq.dequeue()
        self.assertEqual(actual, 4)
        self.assertEqual(mq.in_q.stack, [])
        self.assertEqual(mq.out_q.stack, [5])

        actual = mq.dequeue()
        self.assertEqual(actual, 5)
        self.assertEqual(mq.in_q.stack, [])
        self.assertEqual(mq.out_q.stack, [])

        actual = mq.dequeue()
        self.assertEqual(actual, None)
        self.assertEqual(mq.in_q.stack, [])
        self.assertEqual(mq.out_q.stack, [])


if __name__ == "__main__":
    unittest.main()
