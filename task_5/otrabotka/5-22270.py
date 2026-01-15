def convert(num, sys):
    res = ''
    while num: # num - это есть num != 0
        res = str(num%sys) + res
        num = num // sys
    return res


ans = []
for N in range(1, 100000):
    R = convert(N, 4)
    if R[0] == '3':
         R = R.replace('3', 'a')
         R = R.replace('1', 'b')
         R= R.replace('a', '1')
         R= R.replace('b', '3')
         R = '21' + R
    else:
         R = '1' + R[1:] +'12'
    R = int(R, 4)
    if R < 598:
        ans.append(N)

print(max(ans))







