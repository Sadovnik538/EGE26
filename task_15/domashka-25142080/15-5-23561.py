def f(A):
    for x in range(-1000, 1000):
        F = (x % 128 == 0) <= ((not(x % A == 0)) <= (not(x % 80 == 0)))
        if not F:
            return False
    return True


ans = []
for A in range(1, 1000):
    if f(A):
        ans.append(A)

print(max(ans))

# 640