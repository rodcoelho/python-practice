#!/usr/bin/env python3

# pop, peek, push, isEmpty


def stack_sort(s1):
    s2 = []
    fs = []
    l = len(s1)

    while len(fs) < l:
        g = None
        # search for greatest in s1 / s2
        for i in range(len(s1)):
            temp = s1.pop()
            s2.append(temp)
            if g is None:
                g = temp
            else:
                if temp < g:
                    g = temp

        # now we know the greatest, let's move it to fs
        for i in range(len(s2)):
            temp = s2.pop()
            if temp == g:
                fs.append(temp)
            else:
                s1.append(temp)

    return fs


if __name__ == '__main__':
    assert stack_sort([4, 5, 3, 8]) == [3, 4, 5, 8], 'error1'
