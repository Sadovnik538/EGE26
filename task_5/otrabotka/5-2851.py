cnt_chet = 0
for N in range(2, 100000):
    R = bin(N)[2:]
    for i in range(1, len(R), 2):  # range(1, 6, 2) -> 1 3 5
        if R[i] == '1':
            cnt_chet += 1

