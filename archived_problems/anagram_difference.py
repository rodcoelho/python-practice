def countManipulations(a, b):
    count = 0
    a = list(a)
    b = list(b)

    chars_list = [0] * 26

    for i in range(len(a)):

        chars_list[ord(a[i]) - ord('a')] += 1

    for i in range(len(b)):

        chars_list[ord(b[i]) - ord('a')] -= 1

        if chars_list[ord(b[i]) - ord('a')] < 0:
            count += 1

    return count


a = 'abb'
b = 'bbc'
print(countManipulations(a,b))