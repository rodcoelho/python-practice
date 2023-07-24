# Input example: [9, 0, 1, 0, 5]
# Output example: [9, 1, 5, 0 0]

def move_zeroes(nums):
    def bubble_sort(l):
        length = len(l) - 1
        sorted = False
        while not sorted:
            sorted = True
            for i in range(length):
                if l[i] == 0 and l[i +1] != 0:
                    sorted = False
                    l[i], l[i + 1] = l[i + 1], l[i]
        return l
    bubble_sort(nums)
    return nums

# Do not comment out these tests.

assert move_zeroes([0, 0, 5]) == [5, 0, 0], "Test 1 Failed"
assert move_zeroes([9, 19, 0, 1]) == [9, 19, 1, 0], "Test 2 Failed"
assert move_zeroes([5, 0, 0, 0]) == [5, 0, 0, 0], "Test 3 Failed"
print("Passed All Tests!")

