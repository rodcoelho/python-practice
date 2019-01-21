#!/usr/bin/env python3

# Given a number N. Write a program to the find number of diagonals possible in N sided convex polygon.

# Input:
# First line of input contains a single integer T which denotes the number of test cases. T test cases follows. First line of each test case contains a single integer N.

# Output:
# For each test case print number of diagonals possible in N sided convex polygon.

def get_possible_diagnols(num_of_sides):
    # n(n-3)/2
    return num_of_sides * (num_of_sides - 3) / 2

if __name__ == "__main__":
    print("begin assert tests")
    assert get_possible_diagnols(5) == 5, "error 1"
    assert get_possible_diagnols(6) == 9, "error 2"
    print("end assert tests")
