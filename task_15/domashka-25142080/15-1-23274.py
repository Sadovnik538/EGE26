def f(A, x, y):
    return ((2*x + y) != 110) or (x < y) or (A < x)

ans = []
for A in range(0, 1000):
    if all(f(A, x, y) for x in range(0, 1000) for y in range(0, 1000)):
        ans.append(A)

print(max(ans))

# 36