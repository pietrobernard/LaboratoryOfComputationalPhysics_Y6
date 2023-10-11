"""
2. The swap function
Write a function that swaps the values of two input variables x and y (whatever the type). Try to do that also without a temporary variable
"""
a = 1
b = 2

def swapfun(x, y):
    global a, b
    a = y
    b = x

print("before:",a,b)
swapfun(a, b)
print("after:",a,b)