from itertools import product

cnt = 0
for val in product('зеркало', repeat=6):
    val = ''.join(val)
    if len(val) == len(set(val)):
        cnt += 1
print(cnt)