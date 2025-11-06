# системы счисления

N = 25

# двоичная
# bin переврдит 10- число в 2-систему
#принимает на выход int врзырвщвет str
print(bin(N))
# [2:4]срез уьирающий первые 2 символам '0b'
print(bin(N)[2:])
# f'' формат. строка
print(f'{N:b}')

# восьмеричная
print(oct(N))
print(oct(N)[2:])
print(f'{N:o}')

# шестнадцатеричная
print(hex(N)[2:])
print(f'{N:x}')

# перевод в любую сис счисления (2<= sys <=9)
def convert(num, sys):
    res =''
    while num != 0:
        res += str(num % sys)
        num //= sys
        num = num // sys
    return res[::-1]

print(convert(31, 3))

# перевод в любую сис счисления (2<= sys <=36)
from string import printable

def convert2(num, sys):
    res = ''
    while num != 0:
        res += printable[num % sys]
        num //= sys
    return res[::-1]