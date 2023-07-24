#!/usr/bin/env python3


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)




if __name__ == '__main__':

    # l = fibo(6)
    # print()

    x = map(fibo, range(0, 9))
    for ch in x:
        print(ch)



