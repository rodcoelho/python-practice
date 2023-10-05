# Write a function to swap a number in place without temporary variables.

def swap(a, b):
    a = a + b # 15
    b = a - b # 5
    a = a - b
    return a, b

if __name__ == "__main__":
    x, y = 5, 10
    print(swap(x,y))