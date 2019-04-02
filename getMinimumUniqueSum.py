def getMinimumUniqueSum(arr):
    arr = sorted(arr)
    prior = arr[0]
    final_sum = arr[0]

    for i in range(1, len(arr)):

        if prior >= arr[i]:
            prior += 1
            final_sum += prior
        else:
            final_sum += arr[i]
            prior = arr[i]

    return final_sum

# Driver code
a = [1 ,2, 2]
print(getMinimumUniqueSum(a))