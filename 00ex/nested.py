"""
8. Nested list comprehension
A Pythagorean triple is an integer solution to the Pythagorean theorem.
The first Pythagorean triple is (3,4,5). Find and put in a tuple all unique Pythagorean triples for the positive integers a, b and c less than 100.
"""

"""
a = [[0,1,2],[3,4,5]]

b for x in a for b in x

diventa: 0,1,2,3,4,5

vediamo perche':

for x in a: x diventa:
    [0,1,2]
    [3,4,5]

poi lui fa: for b in x:
    [0,1,2]
        0, 1, 2

"""

def rotate(l, n):
    return l[n:] + l[:n]

def perm(in_tuple):
    # calculates all the permutations
    perms = [rotate(in_tuple, x) for x in range(0,len(in_tuple),1)]
    # then i should return the 'fundamental' that I decide to be the one with the smallest number first
    # the fundamental it is checked if it's already in the 'triples'
    perms.sort() #sorted(perms, key = lambda x: (x[0], x[1], x[2]))
    return perms[0]

triples = [(x,y,z) for x in range(1,100) for y in range(1,100) for z in range(1,100) if (x**2+y**2==z**2)]
unique_triples = [triple for triple in triples if perm(triple) not in triples]

print(triples)
print(unique_triples)