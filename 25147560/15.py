def f(A):
    for x in range(1,10000):
        F = (x % A == 0) or ((x % 133 == 0) <= (not (x % 95 == 0)))
        if not F:
            return False
    return True

ans = []
for A in range(1, 10000) :
        if f(A):
            ans.append(A)

print(max(ans))




