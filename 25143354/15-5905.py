def f(A):
    for x in range(1,400):
        for y in range(1,400):
            for z in range(1,400):
                F = (x|50 == x) or (y&34 != 0) or (z|24 != 24) or (x*y*z > A//8)
                if not F:
                    return False
    return True

for A in range(1, 400)[::-1]:
    if f(A):
        print(A)
        break
