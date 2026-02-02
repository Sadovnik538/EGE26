from itertools import combinations

def f(x):
    c = 48 <= x <= 94
    j = 83 <= x <=100
    a = A1 <= x <= A2
    return (not (c or j)) <= (not a)


line = sorted([48, 83, 94, 100])

linex = [50, 90, 96]

ans = []
for A1, A2 in combinations(line, 2):
     if all(f(x) for x in linex):
         ans.append(A2 - A1)

print(max(ans))