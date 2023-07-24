#!/usr/bin/env python3

# Given N, count all ‘a’(>=1) and ‘b’(>=0) that satisfy
# the condition a^3 + b^3 = N.

import math

def get_count_cubed(num):
    count = 0
    max_num = int(math.sqrt(num))
    
    for i in range(1, max_num + 1):
        for j in range(max_num):
            if i ** 3 + j ** 3 == num:
                count += 1

    return count


if __name__ == "__main__":
    assert get_count_cubed(9) == 2, 'test 1'
    assert get_count_cubed(28) == 2, 'test 2'
    print("TESTS PASSED")
