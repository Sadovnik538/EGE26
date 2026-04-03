def convert(num, sys):
    res = ''
    while num:
        res = str(num%sys) + res
        num = num//sys
    return res

ans = []
for N in range(1, 10000):
    R = convert(N, 4)
    if N%4 == 0:
        R = R + R[:2]
    else:
        R = R + convert((N%4) * 4, 4)
    R = int(R, 4)
    if R > 291:
        ans.append(R)

print(min(ans))

