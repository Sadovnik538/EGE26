# Переменные и типы данных
# = - Оператор присваивания
age = 57
print("Мне", age, "лет")

# Нотации

# snake_case
client_name = 'Sasha'
client_age = 17

#cameCase
clientName = 'Artyom'
clientAge = 18

#PascalCase
ClientAge = 27
ClientName = 'Ivan'

# Правила наименования переменных
# Только латинские символы a-z A-Z
# Цифры, но не на первой позиции
# Знак нижнего подчёркивания
client1 = 1
client2 = 2

# Типы данных
# integer / int / целое число
my_int = 10
print(my_int, type(my_int))

# float / float /  вещественное число
my_float = 10.54
print(my_float, type(my_float))

# string / str /  строка
my_str_1 = 'Hello'
my_str_2 = 'Hi'
my_str_3 = '"Help"'
print(my_str_1, type(my_str_1))
print(my_str_2, type(my_str_2))
print(my_str_3, type(my_str_3))

# list / list / список
my_list = ['Sasha', 20, 170.5]
print(my_list, type(my_list))
# Индексация
# У каждого элемента списка есть свой порядковый номер
# Нумерация элементов списка всегда начинается с 0
print(my_list[0], type(my_list[0]))
print(my_list[1], type(my_list[1]))

# tuple / tuple / кортеж
my_tuple = (19, 'hello', 8.9)
print(my_tuple, type(my_tuple))
print(my_tuple[0], type(my_tuple[0]))
my_list[0] = 'NeSasha'
# tuple нельзя изменить
# my_tuple[0] = 22

# set / set / множество
my_set = {1, 2, 3}
print(my_set, type(my_set))

test = [1, 1, 1, 1]
my_set_1 = {1, 1, 1, 1}
print(test, type(test))
print(my_set_1, type(my_set_1))

# dictionary / dict / словарь
my_dict = {'name':'Egor', 'age':17, 'height':180}
print(my_dict['name'])
print(my_dict, type(my_dict))

# boolean / bool / логический тип данных
my_bool_1 = True
my_bool_2 = False
print(my_bool_1, type(my_bool_1))

