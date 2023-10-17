
import unittest

"Write an algorithm which computes the number of trailing zeros in n factorial."


class FactorialHandler:
    def _factorial(self, num):
        output = 1
        for i in range(1, num+1):
            # print("i", i)
            output = output * i

            # print("output", output)
        
        return output

    def compute_trailing(self, num):
        factorial = self._factorial(num)
        normalized_factorial = str(factorial)
        count = 0
        for i in range(1, len(normalized_factorial)):
            char = normalized_factorial[-i]
            if char == "0":
                count += 1
            else:
                break

        return count


class TestFactorialHandler(unittest.TestCase):
    def test_compute(self):
        test_cases = [
            (0, 0), 
            (1, 0), 
            (2, 0), 
            (3, 0), 
            (4, 0), 
            (5, 1), 
            (6, 1), 
            (7, 1), 
            (8, 1), 
            (9, 1), 
            (10, 2), 
            (11, 2), 
            (12, 2), 
            (13, 2), 
            (14, 2), 
            (15, 3), 
            (16, 3), 
            (17, 3), 
            (18, 3), 
            (19, 3), 
        ]

        fh = FactorialHandler()
        for test_case in test_cases:
            num, expected = test_case
            actual = fh.compute_trailing(num)
            self.assertEqual(actual, expected)
            

if __name__ == "__main__":
    unittest.main()
