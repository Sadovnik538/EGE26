def f(x, s):
    if x <= 11: return s % 2 == 0
    if s == 0: return False
    n = [f(x-3, s-1), f(x-7, s-1), f(x//3, s-1)]
    return any(n) if (s-1)%2 == 0 else all(n)

print('19)', min([x for x in range(12, 1000) if f(x, 2)]))
print('20)', [x for x in range(12, 1000) if f(x, 3) and not f(x, 1)][0], [x for x in range(12, 1000) if f(x, 3) and not f(x, 1)][1])
print('21)', min([x for x in range(12, 1000) if f(x, 4) and not f(x, 2)]))