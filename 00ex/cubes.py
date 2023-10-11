"""
7. Cubes
Create a list of the cubes of x for x in [0, 10] using:
a) a for loop
b) a list comprehension
"""

list_of_cubes_0 = []
for x in range(0,10):
    list_of_cubes_0.append(x**3)

list_of_cubes_1 = [x**3 for x in range(0,10)]
