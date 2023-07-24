#!/usr/bin/env python3

# Given a string containing of ‘0’, ‘1’ and ‘?’ wildcard characters, generate all binary strings that can be formed by replacing each wildcard character by ‘0’ or ‘1’

# Output: Print all binary string that can be formed by replacing each wildcard character.

import itertools


def get_binary_poss(s):
    slist = list(s)
    output = []
    count = s.count('?')
    chars = '01'
    for item in itertools.product(chars, repeat=count):
        new_list = []
        tmp = list("".join(item))
        for ele in slist:
            if ele == '?':
                new_list.append(tmp.pop(0))
            else:
                new_list.append(ele)
        output.append(''.join(new_list))

    return output        


if __name__ == '__main__':
    assert get_binary_poss('1??0?101') == ['10000101', '10001101', '10100101', '10101101', '11000101', '11001101', '11100101', '11101101'], 'error1'
    print("TESTS PASSED")
    
