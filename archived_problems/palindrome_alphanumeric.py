#!/usr/bin/env python3

# Jarvis is weak in computing palindromes for Alphanumeric characters.
# While Ironman is busy fighting Thanos, he needs to activate sonic punch but Jarvis is stuck in computing palindromes.
# You are given a string containing the alphanumeric character. Find whether the string is palindrome or not.
# If you are unable to solve it then it may result in the death of Iron Man.
#
# Input:
# The first line of the input contains t, the number of test cases. Each line of the test case contains string 'S'.
#
# Output:
# Each new line of the output contains "YES" if the string is palindrome and "NO" if the string is not a palindrome.


def palindrome_alphanumeric_test(s):
    s = [x.lower() for x in s if x.isalnum()]
    rev_s = s[::-1]
    if rev_s == s:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    assert palindrome_alphanumeric_test('i am :IronnorI Ma, i') == 'YES'
    assert palindrome_alphanumeric_test('Ab?/Ba') == 'YES'


