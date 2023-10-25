"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.

insert(int val) Inserts an item val into the set if not present. 
Returns true if the item was not present, false otherwise.

remove(int val) Removes an item val from the set if present. 
Returns true if the item was present, false otherwise.

getRandom() Returns a random element from the current set of elements 
(it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.

You must implement the functions of the class such that each function 
works in average O(1) time complexity.
"""

import unittest 
import random


class RandomizedSet:
    def __init__(self):
        self.data = set()
        
    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.data.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.data:
            self.data.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(tuple(self.data))

class TestRandomizedSet(unittest.TestCase):
    def test_insert_remove_get_random(self):
        rs = RandomizedSet()

        methods = ["insert", "remove", "insert", "remove", "insert", "getRandom"]
        args = [[1], [2], [2], [1], [2], []]
        expecteds = [True, False, True, True, False, 2]

        for method, arg, expected in zip(methods, args, expecteds):
            f = getattr(rs, method)
            actual = f(*arg)
            self.assertEqual(actual, expected, "actual {} expected {}".format(actual, expected))


unittest.main()
