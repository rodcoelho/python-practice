#!/usr/bin/env python3

"""
You have given two 32-bit numbers,N and M,and two bit positions,i and j.
Write a method to set all bits between i and j in N equal to M
(E.G.,m becomes a subdtring of N located at i and starting at j).
"""

import unittest


class BitManipulator:
    def manipulate(self, n, m, i, j):
        bin_n, bin_m = [char for char in str(bin(n)[2:])], [char for char in str(bin(m)[2:])]
        
        for x in range(len(bin_n)):
            if x >= i*2:
                if bin_m:
                    tmp = bin_m[0]
                    bin_m = bin_m[1:]
                    bin_n[x] = tmp

        return int("".join(bin_n), 2)



class TestBitManipulator(unittest.TestCase):
    def test_bitmanipulator_manipulate(self):
        self.test_cases = [
            ((int("10000000000", 2), int("10011", 2), 2, 6), int("10001001100", 2)),
            ((int("11111111111", 2), int("10011", 2), 2, 6), int("11111001111", 2)),
        ]

        bm = BitManipulator()

        for test_case in self.test_cases:
            inputs, expected = test_case
            n, m, i, j = inputs

            self.assertEqual(bm.manipulate(n, m, i, j), expected, (bm.manipulate(n, m, i, j), expected))


if __name__ == "__main__":
    unittest.main()