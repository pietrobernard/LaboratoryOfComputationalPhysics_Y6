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

(3,4,5), (4,5,3), (5,3,4)
ma anche: (3,5,4) e (5,4,3) e (4,3,5)
ho 6 possibili permutazioni, infatti 3!



"""
"""
def rotate(l, n):
    return l[n:] + l[:n]

def perm(in_tuple):
    # calculates all the 6 permutations for a given triple
    perms = [rotate(in_tuple, x) for x in range(0,len(in_tuple),1)]
    n_tuple = (in_tuple[0],in_tuple[2],in_tuple[1])
    perms += [rotate(n_tuple, x) for x in range(0,len(n_tuple),1)]
    # then i should return the 'fundamental' that I decide to be the one with the smallest number first
    # the fundamental it is checked if it's already in the 'triples'
    perms.sort() #sorted(perms, key = lambda x: (x[0], x[1], x[2]))
    return perms[0]
"""

triples = [(x,y,z) for x in range(1,100) for y in range(1,100) for z in range(1,100) if (x**2+y**2==z**2)]
#print(triples)
# if i exchange a and b i'm ok so
unique_triples = []
triples_dict = {}
for i in triples:
    equiv_triple = (i[1],i[0],i[2])
    rep_triple = [i,equiv_triple]
    rep_triple.sort()
    if (rep_triple[0] not in triples_dict):
        triples_dict[rep_triple[0]] = 0
        unique_triples.append(rep_triple[0])

print(unique_triples, len(unique_triples))
"""
unique_triples = []
triples_rep = {}
for i in triples:
    triple_rep = perm(i)
    if triple_rep not in triples_rep:
        triples_rep[triple_rep] = 0
        unique_triples.append(triple_rep)
print(unique_triples)
"""


