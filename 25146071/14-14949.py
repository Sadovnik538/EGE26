from string import printable
from math import log2

for x in printable[1:8]:
    num = int(f'{x}1{x}', 16) + int(f'{x}3{x}3', 8)
    if log2(num) % 1 == 0 or log2(num) == int(log2(num)) or str(log2(num))[-1] == '0':
        print(x)