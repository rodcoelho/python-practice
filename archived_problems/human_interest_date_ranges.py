import unittest
from datetime import date, timedelta

class Solution:
    def count_unique_days(self, ranges):
        unique_days = set()

        for beg, end in ranges:
            current = beg
            while current <= end:
                unique_days.add(current)
                current += timedelta(days=1)

        return len(unique_days)

class TestSolution(unittest.TestCase):
    def test_count_unique_days(self):
        s = Solution()

        ranges = [
            (date(2022, 1, 1), date(2022, 1, 5)),
            (date(2022, 1, 4), date(2022, 1, 8)),
            (date(2022, 1, 10), date(2022, 1, 12))
        ]
        expected = 11
        actual = s.count_unique_days(ranges)
        self.assertEqual(actual, expected)

unittest.main()