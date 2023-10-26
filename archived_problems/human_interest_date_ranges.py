import unittest
from datetime import date, timedelta

class Solution:
    def count_unique_days_datetime(self, ranges):
        unique_days = set()

        for beg, end in ranges:
            current = beg
            while current <= end:
                unique_days.add(current)
                current += timedelta(days=1)

        return len(unique_days)
    
    def count_unique_days_string(self, ranges):
        unique_days = set()
        for r in ranges:
            beg, end = r
            b_yyyy, b_mm, b_dd = beg.split(", ")
            e_yyyy, e_mm, e_dd = end.split(", ")
            beg_date = date(int(b_yyyy), int(b_mm), int(b_dd))
            end_date = date(int(e_yyyy), int(e_mm), int(e_dd))

            current_date = beg_date
            while current_date <= end_date:
                unique_days.add(current_date)
                current_date += timedelta(days=1)
            
        return len(unique_days)
        

class TestSolution(unittest.TestCase):
    def test_count_unique_days_datetime(self):
        s = Solution()

        ranges = [
            (date(2022, 1, 1), date(2022, 1, 5)),
            (date(2022, 1, 4), date(2022, 1, 8)),
            (date(2022, 1, 10), date(2022, 1, 12))
        ]
        expected = 11
        actual = s.count_unique_days_datetime(ranges)
        self.assertEqual(actual, expected)

    def test_count_unique_days_string(self):
        s = Solution()

        ranges = [
            ("2022, 1, 1", "2022, 1, 5"),
            ("2022, 1, 4", "2022, 1, 8"),
            ("2022, 1, 10", "2022, 1, 12")
        ]
        expected = 11
        actual = s.count_unique_days_string(ranges)
        self.assertEqual(actual, expected)

unittest.main()