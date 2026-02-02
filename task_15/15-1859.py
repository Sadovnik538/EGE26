def f(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f1 = (2 * x + y != 70) or (x < y) or (A < x)
            if not f1:
                return False
    return True


for A in range(20, 1000):
    if f(A):
        print(A)

