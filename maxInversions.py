def getInvCount(prices):
    n = len(prices)
    cnt = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if prices[i] > prices[j]:
                for k in range(j + 1, n):
                    if prices[j] > prices[k]:
                        cnt += 1
    return cnt
