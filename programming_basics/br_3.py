# Операции с переменными
from operator import truediv

# Присваивание
num_1 = 49

# Множественное присваивание
num_2 = num_3 = 1
num_2 = num_2 + 1
print(num_2,num_3)

num_4, num_5 = 10, 20

# SWAP
a = 8
b = 10
print(a,b)
c = a
a = b
b = c
print(a,b)

a, b = b, a
print(a,b)


#############################################################################


# Арифметические переменные
data_1, data_2 = 15, 7
# сложение
summ = data_1 + data_2
# вычитание
sub = data_1 - data_2
# умножение
mult = data_1 * data_2
# возведение в степень
pow = data_1 ** data_2
# взятие корня
root = data_1 ** 0.5
# деление дробное (/)
div_1 = data_1 / data_2
# остаток от деления (%)
div_2 = data_2 % data_1
# целая часть от деления(//)
div_3 = data_2 // data_1

# Разбиение числа на разряды
number = 963
print(number % 10) # получение разряда единиц
print(number // 10 % 10) # получение разряда десятков
print(number // 100) # получение разряда сотен

# Остаток от деления отрицательных чисел
number_1, number_2 = -15, 7
print(number_1 % number_2)
#-15 % 7 = -1 (7 + -1) = 6
#-15 + 7 = -8 + 7 = -1 + 7 = 6

#############################################################################


# Операторы сравнения

number_3, number_4 = 10, 20

# равенство - ==
bool_1 = number_3 == number_4 # False
print(bool_1)

# неравенство - !=
bool_2 = number_3 != number_4 # True
print(bool_2)

# больше / меньше
bool_3 = number_3 < number_4 #True
bool_4 = number_3 > number_4 #False
print(bool_3)
print(bool_4)

#    не меньше     /     не больше
# больше или равно / меньше или равно
bool_5 = number_3 >= number_4 # False
bool_6 = number_3 <= number_4 # True
print(bool_5)
print(bool_6)

test_1 = True
test_2 = True
print(test_1+test_2)


#############################################################################


# Операторы инентичности - is, is not

a = b = 1
b = 3
print(a is b)

a = [1, 2, 3]
b = a
print(a is b)
b[0] = 20
print(a)
print(b)

number_5 = number_6 = 1
print(number_5 is number_6)

# Оператор принадлежности - in, not in
my_list = [9, 86, 3]
my_str = 'hello world'
print(86 in my_list)
print('q' not in my_str)

#############################################################################

# Логические операторы

# Инверсия - not
my_bool = True
print(not my_bool)

# Коньюкция -  and
my_bool_1 = True
my_bool_2 = True
print(my_bool_1 and my_bool_2)

# Дизъюнкция - or
my_bool_3 = True
my_bool_4 = False
print(my_bool_3 or my_bool_4)

# Импликация - <=
my_bool_5 = True
my_bool_6 = False
print(my_bool_5 <= my_bool_6)

# Эквиввалентность - ==
# Требуетб чтобы оба высказывания были одинаковыми
my_bool_7 = True
my_bool_8 = False
print(my_bool_7 == my_bool_8)

# Исключающее или - ^
# Возвращает истину, когда оба элимента разные
my_bool_9 = True
my_bool_10 = False
print(my_bool_9 ^ my_bool_10)

# 1 1 0
# 0 1 1
# 1 0 1
# 0 0 0


#############################################################################


# Порядок выполнения операций
# В  Python

# 1. Действия в скобках
# 2. **
# 3. *, /, %, //
# 4. +, -
# 5. in, not in
# 6. >, <, >=, <=, !=, ==
# 7. ^
# 8. not
# 9. and
# 10. or

#  Порядок выполнения операций  в алгебре логики
# 1. Действия в скобках - ()
# 2. Инверсия - not
# 3. Коньюкция - and
# 4. Дизъюнкция - or
# 5. Импликация - <=
# 6. Эквивалентность - ==


#############################################################################


# Системы счисления

# двоичная
print(bin(number))
# восьмеричная
print(oct(number))
# шестнадцатеричная
print(hex(number))

# Все три ф-ции принимают на вход int и возвращают str

# Перевод в 10 сис
num_bin = '101'
num_tri = '101'
num_dec = '101'
num_hex = '101'
num_dva = '101'
print(int(num_bin), 2)
print(int(num_tri), 3)
print(int(num_dec))
print(int(num_hex), 16)
print(int(num_dva), 20)

# ф-ция int принимает на вход str и возвращает int





