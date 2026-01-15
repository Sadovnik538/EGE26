def convert(num, sys):
    res = ''
    while num:
        res = str(num%sys) + res
        num = num // sys
    return res

for x in range(10000):
    num = 3*7**(x+1) + 13*7**(x+2) + 31*7**(3*x) + 7**(2*x)
    num = convert(num, 7)
    if sum(map(int, num)) == 18:
        print(x)
        break
