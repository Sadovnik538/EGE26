from string import printable as alph

for x in range(1, 150):
    num_1 = 5*150**4 + 1*150**3 + x*150**2 + 2*150**1 + 9*150**0 # ручной перевод в десятичную систему
    num_2 = x*150**3 + 0*150**2 + 2*150**1 + 3*150**0
    num = num_1 + num_2
    if num % 149 == 0:
        print(num // 149)


