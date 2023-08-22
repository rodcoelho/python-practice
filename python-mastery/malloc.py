#!/usr/bin/env python3

import tracemalloc


def measure_memory(func):
    def wrapper(*args, **kwargs):

        tracemalloc.start()

        ret_val = func(*args, **kwargs)

        current, peak = tracemalloc.get_traced_memory()
        print(f"\n\033[37mFunction Name       :\033[35;1m {func.__name__}\033[0m")
        print(f"\033[37mCurrent memory usage:\033[36m {current / 10**6}MB\033[0m")
        print(f"\033[37mPeak                :\033[36m {peak / 10**6}MB\033[0m")
        tracemalloc.stop()

        return ret_val

    return wrapper
