#!/usr/bin/env python3

# For a given string delete the elements which are appearing 
# more than once consecutively. All letters are of lowercase.


def rem_dups(s):
    final = ''
    for char in s:
        if not final:
            final += char
        else:
            if final[-1] != char:
                final += char
    return final

if __name__ == '__main__':
    assert rem_dups('aababbccd') == 'ababcd', 'test 1'
    assert rem_dups('abcd') == 'abcd', 'test 2'
    assert rem_dups('aaabccc') == 'abc', 'test 3'
    print("TESTS PASSED")
