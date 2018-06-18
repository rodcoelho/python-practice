#!/usr/bin/env python3


def my_sorter(l):
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(len(l)-1):
            if l[i] < l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                unsorted = True

    print(l)


if __name__ == '__main__':
    my_sorter([1, 5, 4, 6, 8, 0, 9])

