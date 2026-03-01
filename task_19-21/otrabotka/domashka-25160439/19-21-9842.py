def f(x, s):
    if x >= 111: return s % 2 == 0
    if s == 0: return False
    n = [f(x+1, s-1), f(x+3, s-1), f(x*4, s-1)]
    return any(n) if (s-1)%2 == 0 else all(n)

print('19)', [x for x in range(1, 111) if f(x, 2)])
print('20)', [x for x in range(1, 111) if f(x, 3) and not f(x, 1)])
print('21)', min([x for x in range(1, 111) if f(x, 4) and not f(x, 2)]))