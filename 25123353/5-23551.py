for N in range(0,10000000)[::-1]:
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R = '10' + R
    else:
        R = '1' + R + '01'
    R = int(R,2)
    if R < 30:
        print(N)
        break

#6