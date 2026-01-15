# Системы счисления
from programming_basics.br_3 import num_2

N = 25

# Двоичная сис
# bin() - переводит десятичное число в двоичную систему
#Принимает на вход int, возвращает str
print(bin(N)[2:])
# f'' - это форматируемая строка, котораяя позволяет вставлять в себя переменные
print(f'{N:b}')

print(f'Мне {N} лет')

# Восьмеричная сис
print(oct(N)[2:])
print(f'{N:o}')

# Шестнадцатеричная сис
print(hex(N)[2:])
print(f'{N:x}')

#0123456789ABCDEFG

# Перевод в любую сис (2 <= sys <= 9)
from string import printable
print(printable)
def convert(num, sys):
    res = ''
    while num != 0:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

print(convert(31, 3))

print(hex(16*15+1))


# Сумма цифр числа
# Двоичное число
num_1 = '1010'
print(num_1.count('1'))

# Системы до 10 включительно
num_2 = '823'
print(sum(map(int, num_2)))

print(list(map(int, num_2)))

# Квадратный корень
from math import sqrt
print(list(map(sqrt, [4, 9, 16])))

# Системы до 36 включительно
num_3 = 'AF5'
print(sum(map(lambda x: int(x, 36), num_3)))

# * - распаковка
# lol - переменная
# map -  извлекает все элементы из списка, подставляет на место переменной и выполняет заданное действие
print(*map(lambda lol: lol + 1, [9, 10, 5]))


# Срезы
test_1 = 'hello'
print(test_1[2:]) # срезает первые два символа - llo
print(test_1[:2]) # оставляет первые два символа, срезает остальное - he
print(test_1[-2:]) # оставляет два последних символа, срезает остальные - lo
print(test_1[:-2]) # срезает два последних символа, остальные оставляет - hel
print(test_1[::2]) # шаг слева направо - hlo
print(test_1[::-2]) # шаг справа налево - olh


# Swap
test_2 = '1313202103'
test_2 = test_2.replace('3', 'a')
test_2 = test_2.replace('1', 'b')
test_2 = test_2.replace('a', '1')
test_2 = test_2.replace('b', '3')
print(test_2)


new_test_2 = ''
for i in test_2:
    if i == '3':
        new_test_2 = new_test_2 + '1'
    elif i == '1':
        new_test_2 = new_test_2 + '3'
    else:
        new_test_2 = new_test_2 + i