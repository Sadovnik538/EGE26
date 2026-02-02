def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        return True

def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i):
                d.add(i)
            if is_prime(num//i):
                d.add(num//i)

    if len(d) >= 2:
        M = min(d) + max(d)
        if M > 60_000 and str(M) == str(M)[::-1]:
            return M
        return 0

cnt = 0
for N in range(5400001, 10**30):
    if M := f(N):
        print(M, N)
        cnt += 1
        if cnt == 5:
            break