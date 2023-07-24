#!/usr/bin/env python3

fib_list = []


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def find_fibo_index(value_of_n):
    x = 0
    flag = True
    while flag:
        value = fibo(x)
        if value == value_of_n:
            print(x)
            flag = False
        else:
            x += 1


if __name__ == '__main__':
    find_fibo_index(10946)

