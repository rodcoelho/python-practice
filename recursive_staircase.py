stairs = [7, 35, 70, 350]
d = {0:0, 1:1, 2:2, 3:4}
def rec_sum(n):
    if n in d.keys():
        return d[n]
    payload = rec_sum(n-3) + rec_sum(n-2) + rec_sum(n-1)
    d[n] = payload
    return d[n]

for _ in stairs:
    __ = rec_sum(_)
    print(str(_) + ' stairs = ' + str(__) + ' ways to get up')