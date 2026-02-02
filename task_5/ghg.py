def sum_digits_math(n):
    s = 0
    while n > 0:
        s += n % 10  # Берем последнюю цифру (остаток от деления на 10)
        n //= 10     # Целочисленно делим число на 10 (убираем последнюю цифру)
    return s

# Пример использования:
number = 258
print(sum_digits_math(number))

num = '210202012101'
print((num.count('1') + num.count('2')*2) % 2 == 0)

def convert(num, sys):
    res = ''
    while num:
        res = str(num%sys) + res
        num = num // sys
    return res


for N in 4, 5:
    R = convert(N, 3)
    R_2 = R.count('1') + R.count('2')*2
    if R_2 % 2 == 0:
        R = '1' + R + '2'
    else:
        R = '2' + R + '0'
    R = int(R, 3)
    print(R)