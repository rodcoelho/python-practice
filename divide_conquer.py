x = list(range(5))

def rec_sum(x):
    if len(x) == 0:
        return 0
    else:
        a = x[0]
        b = x[1:]
        return a + rec_sum(b)

rs = rec_sum(x)
print(rs)