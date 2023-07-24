def is_palindrome(string):
    array = list(string)
    rev_array = array[::-1]
    if array == rev_array:
        return True
    else:
        return False

assert is_palindrome('abc_cba') == True, "Test1 Failed"
assert is_palindrome('1234554321') == True, "Test2 Failed"
assert is_palindrome('00001000') == False, "Test3 Failed"
assert is_palindrome('hellow_world') == False, "Test4 Failed"
