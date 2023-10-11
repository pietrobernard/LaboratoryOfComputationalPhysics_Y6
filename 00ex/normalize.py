"""
9. Normalization
Write a function that takes a tuple of numbers and returns it with the entries normalized to one
"""

def TupleNorm(in_tuple):
    try:
        s = sum([x**2 for x in in_tuple])**0.5
        norm = [x/s for x in in_tuple]
        return tuple(norm)
    except:
        print("TypeError: input must be a valid n-tuple.")
        return 1

print(TupleNorm((1,2,3,4,5)))