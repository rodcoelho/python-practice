#!/usr/bin/env python3

# Given a String of length N reverse each word in it. 
# Words are separated by dots.


def rev_words(words):
    word_list = words.split('.')
    rev_list = [word[::-1] for word in word_list]
    return '.'.join(rev_list)


if __name__ == "__main__":
    assert rev_words("i.like.this.program.very.much") == "i.ekil.siht.margorp.yrev.hcum", 'error 1'
    assert rev_words("pqr.mno") == "rqp.onm", 'error 2'
    print("TESTS PASSED")
