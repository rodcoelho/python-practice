import unittest

class PlateStack:
    def __init__(self, height):
        self.height = height
        self.stack = []
        self.current_stack = []

    def pop(self):
        if not self.current_stack:
            return None
        else:
            ret_val = self.current_stack[-1]
            self.current_stack = self.current_stack[:-1]

            if not self.current_stack:
                if self.stack:
                    self.current_stack = self.stack[-1]
                    self.stack = self.stack[:-1]
        
        return ret_val

    def push(self, val):
        if not self.current_stack or len(self.current_stack) < self.height:
            self.current_stack.append(val)
        elif len(self.current_stack) == self.height:
            self.stack.append(self.current_stack)
            self.current_stack = [val]


class TestPlateStack(unittest.TestCase):
    def test_PlateStack_push_then_pop(self):
        ps = PlateStack(3)

        ps.push(9)
        self.assertEqual(len(ps.stack), 0)
        self.assertEqual(ps.current_stack, [9])

        ps.push(8)
        self.assertEqual(len(ps.stack), 0)
        self.assertEqual(ps.current_stack, [9,8])

        ps.push(7)
        self.assertEqual(len(ps.stack), 0)
        self.assertEqual(ps.current_stack, [9,8,7])

        ps.push(6)
        self.assertEqual(len(ps.stack), 1)
        self.assertEqual(ps.current_stack, [6])


        ps.push(5)
        self.assertEqual(len(ps.stack), 1)
        self.assertEqual(ps.current_stack, [6, 5])
        self.assertEqual(ps.stack, [[9,8,7]])


        actual = ps.pop()
        self.assertEqual(actual, 5)
        self.assertEqual(len(ps.stack), 1)
        self.assertEqual(ps.current_stack, [6])

        actual = ps.pop()
        self.assertEqual(actual, 6)
        self.assertEqual(len(ps.stack), 0)
        self.assertEqual(ps.current_stack, [9,8,7])


        actual = ps.pop()
        self.assertEqual(actual, 7)
        self.assertEqual(len(ps.stack), 0)
        self.assertEqual(ps.current_stack, [9,8])

        for i in range(10):
            ps.push(i)
        self.assertEqual(len(ps.stack), 3)
        self.assertEqual(ps.current_stack, [7,8,9])
        self.assertEqual(ps.stack, [[9,8,0],[1,2,3],[4,5,6]])

if __name__ == "__main__":
    unittest.main()
