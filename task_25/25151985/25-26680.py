def fact(num):
    d = []
    i = 3
    while i*i < num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]
    return d

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


cnt = 0
for N in (5_000_001, 10**20, 2):
    M = fact(N)
    if len(M) == 2 and len(set(M)) == 2 and is_prime(abs(M[1]-M[1])):
        print(N, max(M))
        cnt += 1
        if cnt == 5:
            break


