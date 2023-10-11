"""
6. Combination of functions
Write two functions - one that returns the square of a number, and one that returns the cube.
Now write a third function that returns the number raised to the 6th power using the two previous functions.
"""

f = lambda x, n : x**n
g = lambda x : f(f(x, 2),3)

def f0(n):
    return n**2
def f1(n):
    return n**3
def g0(n):
    return f1(f0(n))

print(g(2),g0(2))