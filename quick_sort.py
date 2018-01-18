def qksort(array):
    if len(array)< 2:
        return array
    else:
        pivot = array[0]
        less = [_ for _ in array[1:] if _ <= pivot]
        greater = [_ for _ in array[1:] if _ > pivot]
        return qksort(less) + [pivot] + qksort(greater)

assert qksort([1,2,3,4,5,6,7,8,9,10]) == [1,2,3,4,5,6,7,8,9,10], "Test1 Failed"
assert qksort([1,4,3,2,7,6,5,10,9,8]) == [1,2,3,4,5,6,7,8,9,10], "Test2 Failed"
assert qksort([10,9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9,10], "Test3 Failed"
assert qksort([0,0,0,0,0,10,0,0,0,0]) == [0,0,0,0,0,0,0,0,0,10], "Test4 Failed"
