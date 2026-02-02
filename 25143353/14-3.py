
N = 17 * 125**453 + 117 * 5**231 - 3 * 5**13 - 2357

cnt =[]
cnt = 0
while N:
    if N % 125 <= 37:
        cnt += 1
    N //= 125
print(cnt)

