#!/usr/bin/env python3

# Given a String of length N reverse each word in it. Words are separated by dots.

# Output: For each test case, output a String in single line containing the reversed words of the given String.


def rev_inplace(s):
    s = s.split('.')
    s = [''.join(list(x)[::-1]) for x in s]
    return '.'.join(s)

if __name__ == "__main__":
    assert rev_inplace("i.like.this.program.very.much") == "i.ekil.siht.margorp.yrev.hcum", 'error1'
    assert rev_inplace("pqr.mno") == "rqp.onm", 'error2'
    print("TESTS PASSED")
