def f(A):
    for x in range(1, 1000):
        F = ((x % A) == 0) or ((70 <= x <= 90) <= (not ((x % 22) == 0)))
        if not F:
            return False
    return True


ans = []
for A in range(1, 1000):
    if f(A):
        ans.append(A)

print(max(ans))

# 88