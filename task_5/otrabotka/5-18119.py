def convert(num, sys):
    res = ''
    while num:
        res = str(num%sys) + res
        num = num // sys
    return res

ans = []
for N in range(1,1000000):
    R = convert(N, 3)
    R_2 = R.count('1') + R.count('2')*2
    if R_2 % 2 == 0:
        R = '1' + R + '2'
    else:
        R = '2' + R + '0'
    R = int(R, 3)
    if R > 100:
        ans.append(R)
print(min(ans))





