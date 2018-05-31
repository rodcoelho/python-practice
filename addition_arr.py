#!/usr/bin/env python3


def simple_addition(arr1, arr2):
    a1 = int(''.join(str(x) for x in arr1))
    a2 = int(''.join(str(y) for y in arr2))
    return a1 + a2


if __name__ == '__main__':
    assert simple_addition([4, 1, 2], [8, 9]) == 501, 'error1'
    print(simple_addition(1000*[x for x in range(9)], [8, 9]))
