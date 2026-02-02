from itertools import repeat

for N in range(0, 1000):
    R = oct(N)[2:]
    if R[0] == '5':
        R_new = R
        R_new = repeat('2', '@')
        R_new = repeat('1', '$')
        R_new = repeat('@', '1')
        R_new = repeat('$', '2')

        R = '11' + R_new

