"""
The MickeyMouse problem
a) Write a program that prints the numbers from 1 to 100. But for multiples of 3 print Mickey instead of the corresponding number
and for the multiples of 5 print Mouse. For numbers which are multiples of both three and five print MickeyMouse

b) Put the result in a tuple and substitute Mickey with Donald and Mouse with Duck
"""

def check(n):
    t = [(n%3==0),(n%5==0)]
    if (t[0]==0 and t[1]==0):
        return n
    elif (t[0]==1 and t[1]==0):
        return 'Mouse'
    elif (t[0]==0 and t[1]==1):
        return 'Mickey'
    else:
        return 'MickeyMouse'

def transform(i):
    try:
        n = i.replace('Mickey','Donald')
        return n.replace('Mouse','Duck')
    except:
        return i

number_list = [check(i) for i in range(1,101,1)]
final_tuple = tuple([transform(i) for i in number_list])
print(final_tuple)
