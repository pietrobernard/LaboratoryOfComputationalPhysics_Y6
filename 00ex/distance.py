"""
3. Computing the distance
Write a function that calculates and returns the euclidean distance between
two points u and v, where u and v are both 2-tuples (x,y).
For example, if u=(3,0) and v=(0,4), the function should return 5
"""

def EuclideanDistance(u, v):
    try:
        d = ((u[0]-v[0])**2 + (u[1]-v[1])**2)**0.5
        return d
    except:
        print("TypeError: u and v must be both 2-tuples (x,y).")
        return 1

print(EuclideanDistance((3,0),(0,4)))