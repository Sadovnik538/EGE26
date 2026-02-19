def f(s,e,cnt):
    if s % 2 == 0:cnt += 1
    if s == e and s <= 15: return 1
    if s > e or cnt > 15: return 0
    return f(s+1, e, cnt) + f(s+3, e, cnt) + f(s*2+1, e, cnt)

print(f(1, 55, 0))