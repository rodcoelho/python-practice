import unittest

"""
Create a Multi-Stack Stack
"""


class Empty:
    def __eq__(self, other):
        return isinstance(other, Empty)


class MultiStack:
    def __init__(self, num_of_stacks, len_of_stacks):
        self.len_of_stacks = len_of_stacks
        self.num_of_stacks = num_of_stacks
        self.stack_len = num_of_stacks*len_of_stacks
        self.stack_list = [Empty() for i in range(self.stack_len)]
        self.stack_meta = {i:0 for i in range(num_of_stacks)}

    def _is_empty(self, val):
        return isinstance(val, Empty)

    def push(self, val, stack_id):
        if stack_id > self.num_of_stacks:
            return 404

        success = False
        index_start = stack_id * self.len_of_stacks
        for i in range(self.len_of_stacks):
            if self._is_empty(self.stack_list[index_start+i]):
                self.stack_list[index_start+i] = val
                success = True
                break
        
        if success:
            return val
        return "stack is full"
        
    def pop(self, stack_id):
        if stack_id > self.num_of_stacks:
            return 404

        ret_val = None
        index_start = stack_id * self.len_of_stacks
        index_to_pop = None
        for i in range(self.len_of_stacks):
            if not self._is_empty(self.stack_list[index_start+i]):
                index_to_pop = index_start+i


        if index_to_pop is not None:
            ret_val = self.stack_list[index_to_pop]
            self.stack_list[index_to_pop] = Empty()

        if ret_val == None:    
            return "stack is empty"
        return ret_val


class TestMultiStack(unittest.TestCase):
    def test_push_then_pop(self):
        ms = MultiStack(num_of_stacks=3, len_of_stacks=5)
        ms.push(0,0)
        ms.push(0,0)
        ms.push(1,1)
        ms.push(1,1)
        ms.push(2,2)
        ms.push(2,2)
        self.assertEqual(ms.stack_list, [0,0,Empty(), Empty(), Empty(), 1, 1, Empty(), Empty(), Empty(), 2, 2, Empty(), Empty(), Empty()])
        
        # test regular pop
        actual = ms.pop(0)
        self.assertEqual(actual, 0)
        self.assertEqual(ms.stack_list, [0,Empty(),Empty(), Empty(), Empty(), 1, 1, Empty(), Empty(), Empty(), 2, 2, Empty(), Empty(), Empty()])
        
        actual = ms.pop(0)
        self.assertEqual(actual, 0)
        self.assertEqual(ms.stack_list, [Empty(),Empty(),Empty(), Empty(), Empty(), 1, 1, Empty(), Empty(), Empty(), 2, 2, Empty(), Empty(), Empty()])

        actual1, actual2 = ms.pop(1), ms.pop(2)
        self.assertEqual(actual1, 1)
        self.assertEqual(actual2, 2)
        self.assertEqual(ms.stack_list, [Empty(),Empty(),Empty(), Empty(), Empty(), 1, Empty(), Empty(), Empty(), Empty(), 2, Empty(), Empty(), Empty(), Empty()])

        # test overflow stack edgecase
        ms.push('a', 0)
        ms.push('a', 0)
        ms.push('a', 0)
        ms.push('a', 0)
        ms.push('a', 0)
        self.assertEqual(ms.stack_list, ['a','a','a','a','a', 1, Empty(), Empty(), Empty(), Empty(), 2, Empty(), Empty(), Empty(), Empty()])

        actual = ms.push('a', 0)
        self.assertEqual(actual, "stack is full")
        self.assertEqual(ms.stack_list, ['a','a','a','a','a', 1, Empty(), Empty(), Empty(), Empty(), 2, Empty(), Empty(), Empty(), Empty()])

        # test stack is empty edgecase
        actual = ms.pop(1)
        self.assertEqual(actual, 1)
        self.assertEqual(ms.stack_list, ['a','a','a','a','a', Empty(), Empty(), Empty(), Empty(), Empty(), 2, Empty(), Empty(), Empty(), Empty()])
        actual = ms.pop(1)
        self.assertEqual(actual, "stack is empty")
        self.assertEqual(ms.stack_list, ['a','a','a','a','a', Empty(), Empty(), Empty(), Empty(), Empty(), 2, Empty(), Empty(), Empty(), Empty()])


if __name__ == "__main__":
    unittest.main()
