from dataclasses import replace


def convert(num, sys):
    res = ''
    while num:
        res = str(num % sys) + res
        num = num // sys
    return res

cnt = []
N = 3 * 17**777 + 15 * 17**250 - 6 * 17**100 + 2
N = convert(N, 17)

