from functools import lru_cache

def F(n):
    return G(n-1) + G(n-3)

@lru_cache(None)
def G(n):
    if n > 9: return G(n-4)+ 2
    return 3*n

for i in range(1, 42999):
    G(i)

print(F(42999))