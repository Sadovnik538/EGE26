def  convert(num, sys):
    res = ''
    while num:
        res = str(num%sys) + res
        num = num // sys
    return res

for sys in range(2, 36):
    num_1 = convert(41, sys)
    num_2 = convert(131, sys)
    if num_1[-1:] == '2' and num_2[-1:] == '1':
        print(sys)

