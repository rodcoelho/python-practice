#!/usr/bin/env python3

import math, numbers


class Prime:
    def __init__(self, n):
        flag = True

        # check if int
        if isinstance(n, numbers.Integral):
            pass
        else:
            print('not int')
            flag = False

        # check if positive
        if flag:
            if n < 0:
                print('not positive')
                flag = False
            else:
                pass

        if flag:

            # actual work
            # print primes
            count = 3
            while count < n:
                isprime = True
                for x in range(2, int(math.sqrt(count) + 1)):
                    if count % x == 0:
                        isprime = False
                        break

                if isprime:
                    print(count)  # add comma ?

                count += 1


someprime = Prime(-20)
someprime2 = Prime(19)
someprime3 = Prime('108')

