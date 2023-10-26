"""
There are n gas stations along a circular route, 
where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and 
it costs cost[i] of gas to travel 
from the ith station to its next (i + 1)th station. 

You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, 
return the starting gas station's index if you can travel around
the circuit once in the clockwise direction, 
otherwise return -1. 

If there exists a solution, it is guaranteed to be unique
"""

import unittest
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_station_map = []
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            gas_station_map.append([i, gas[i], cost[i], diff])
        
        gas_station_map.sort(key=lambda x: x[3], reverse=True)

        for candidate in gas_station_map:

            index, g, c, d = candidate

            tmp_gas = gas[index:] + gas[:index]
            tmp_cost = cost[index:] + cost[:index]
            tank = 0

            for i in range(len(tmp_gas)):
                tank += tmp_gas[i] - tmp_cost[i]

                if tank < 0:
                    return -1
            
            if tank >= 0:
                return index
            
        return -1


class TestSolution(unittest.TestCase):
    def test_gas_station(self):
        s = Solution()

        gas = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        expected = 3
        actual = s.canCompleteCircuit(gas, cost)
        self.assertEqual(actual, expected)

        gas = [2,3,4]
        cost = [3,4,3]
        expected = -1
        actual = s.canCompleteCircuit(gas, cost)
        self.assertEqual(actual, expected)

unittest.main()