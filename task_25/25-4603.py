from fnmatch import fnmatch

for N in range(12347 - 12347 % 141, 10**8, 141):
    if fnmatch(str(N), '1234*7') and N % 141 == 0:
        print(N, N // 141)

####################################################

from itertools import product

for l in range(0, 4):
    for zv in product('0123456789', repeat=l):
        zv = int('1234' + ''.join(zv) + '7')
        if zv % 141 == 0:
            print(zv, zv // 141)