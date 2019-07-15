#!/usr/bin/env python3

# Given a byte, swap the two nibbles in it. 
# For example 100 is be represented as 01100100 in a byte (or 8 bits). 
# The two nibbles are (0110) and (0100). 
# If we swap the two nibbles, we get 01000110 which is 70 in decimal.

# Output: In each separate line print the result after swapping the nibbles.

def swap_nibbles(num):
    if num < 0:
        return False
    bin = '{0:08b}'.format(num)
    bin_half = int(len(bin)/2)
    swap_bin = bin[bin_half:] + bin[:bin_half]
    return int(swap_bin, 2)


if __name__ == "__main__":
    assert swap_nibbles(100) == 70, "test 1 fail"
    assert swap_nibbles(129) == 24, "test 2 fail"
    assert swap_nibbles(0) == 0, "test 3 fail"
    assert swap_nibbles(-10) == False, "test 4 fail"
    print("TESTS PASSED")
