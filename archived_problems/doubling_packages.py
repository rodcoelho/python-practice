#!/usr/bin/env python3

# Ishaan has N candies with him. He wants to put them in packets. He can put 1 candy in the first packet, 2 candies in the second packet, 4 candies in the third and so on.
# Calculate the minimum number of packets he needs to store all the candies if he fills the packets starting from the first packet.


def packet_calculator(num):
    left_over = num
    p_size = 1
    packet = 1
    while left_over > 1:
        p_size *= 2
        packet += 1
        left_over -= p_size
    return packet


if __name__ == "__main__":
    assert packet_calculator(2) == 2, 'error1'
    assert packet_calculator(4) == 3, 'error2'
    assert packet_calculator(7) == 3, 'error3'



