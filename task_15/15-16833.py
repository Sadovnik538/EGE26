from itertools import permutations

def f(x):
    p = 25 <= x <= 73
    q = 75 <= x <= 188
    a = A1 <= x <= A2
    return (a and not q) <= (p or q)

line = ([25, ])