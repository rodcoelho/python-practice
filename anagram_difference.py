# Given two strings, A and B, that may or may not be of the same length, determine the minimum number of character deletions required to make A and B anagrams. 
# Any characters can be deleted from either of the strings.

def number_needed(a, b):
    count = 0
    for i in range(0, 25):
        xa = sum(letter == chr(x) for letter in a)
        xb = sum(letter == chr(x) for letter in b)
        count += abs(xa-xb)
    return count


