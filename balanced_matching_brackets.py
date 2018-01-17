d = {'{':'}','[':']','(':')','}':'{',']':'[',')':'('}
def is_matched(expression):
    exp = list(expression)
    stack = [exp[0]]
    for i in range(1,len(exp)):
        stack.append(exp[i])
        try:
            if d[stack[-2]] == stack[-1]:
                stack.pop()
                stack.pop()
        except:
            continue
    if len(stack) == 0:
        return True
    else:
        return False

assert is_matched('{[()]}') == True, "Test1 Failed"
assert is_matched('{}()[]') == True, "Test2 Failed"
assert is_matched('[{}()[]]') == True, "Test3 Failed"
assert is_matched('{{(}}[]') == False, "Test4 Failed"