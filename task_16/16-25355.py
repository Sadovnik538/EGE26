from functools import lru_cache

def F(n):
    if n < 19: return 6 * (G(n-7)-36)
    return F(n-4) + 3580

@lru_cache(None)
def G(n):
    if n < 248045: return G(n+9)-4
    return n/20 + 28

for i in range(248045, 1, -1):
    G(i)

print(F(673))