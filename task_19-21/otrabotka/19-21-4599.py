def f(x, y, s):
    if x+y >= 259: return s % 2 == 0
    if s == 0: return False
    n = [f(x+1, y, s-1),
         f(x, y+1, s-1),
         f(x*2, y, s-1),
         f(x, y*2, s-1)]
    return any(n) if (s-1)%2 == 0 else all(n)

# print('19)', [y for y in range(1, 242) if f(y, 17, 2)])
print('20)', [y for y in range(1, 242) if f(y, 17, 3) and not f(y, 17, 1)])
print('21)', min([y for y in range(1, 242) if f(y, 17, 4) and not f(y, 17, 2]))