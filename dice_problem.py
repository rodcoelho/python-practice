#!/usr/bin/env python3

# You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. The numbers are in the range of 1 to 6, like any ordinary dice. You will be provided with a face of this cube; your task is to guess the number on the opposite face of the cube.

# Input:
# The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows, a single line of the input containing a positive integer N.

# Output:
# For each testcase, print the number that is on the opposite side of the given face.

dice_dict = {
    1:6,
    2:5,
    3:4,
    4:3,
    5:2,
    6:1
}


def find_opposite_dice_num(num):
    return dice_dict[num]


if __name__ == "__main__":
    print("---")
    print("assert tests begin")
    assert find_opposite_dice_num(1) == 6, "error 1"
    assert find_opposite_dice_num(2) == 5, "error 2"
    assert find_opposite_dice_num(3) == 4, "error 3"
    assert find_opposite_dice_num(4) == 3, "error 4"
    assert find_opposite_dice_num(5) == 2, "error 5"
    assert find_opposite_dice_num(6) == 1, "error 6"
    print("assert tests passed")
