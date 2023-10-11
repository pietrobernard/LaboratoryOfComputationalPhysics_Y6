"""
4. Counting letters
Write a program to calculate the number of times each character occurs in a given string s. Ignore differneces in capitalization
"""
def CharCount(in_str):
    freqs = {}
    for char in in_str:
        lchar = char.lower()
        if lchar not in freqs:
            freqs[lchar] = 0
        freqs[lchar] += 1
    return freqs

print(CharCount("ciao come stai oggi?"))