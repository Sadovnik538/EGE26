def f(A):
    for x in range(1, 10000):
        F = ((405%x == 0) <= (81%x == 0)) or ((A-x)>162)
        if not F:
            return False
    return True

for A in range(1,100000):
    if f(A):
        print(A)
