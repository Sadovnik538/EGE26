# Преобразование типов данных


data = '17'
new_age = float(data) + 1.5
print(new_age)

# int -> float, str,

test = 5
print(float(test))
print(str(test))
print(bool(test)) # любое значение отличное от нуля возвращает True

# float ->int, str, bool

test_1 = 0.99
print(int(test_1))
print('{:.3f}'.format(test_1))
print(str(test_1))
print(bool(test_1))

# str -> int, float, list, tuple, set, bool

test_2 = '2341'
print(int(test_2))
print(float(test_2))
test_3 = 'hello'
print(list(test_3))
print(tuple(test_3))
print(set(test_3)) # находит уникальные символы
print(bool(test_3)) # любой текст будет возвращать True
                    # Абсолютно пустая строка будет возвращать False

#list -> str, tuple, set, bool

test_4 = [1, 'test', 6, 1, 1,'test']
print(str(test_4))
print(tuple(test_4))
print(set(test_4))
print(bool(test_4))

#tuple -> str, tuple, set, bool
print(str(test_4))
print(list(test_4)) # Позволяет изменять неизменяемый список
print(set(test_4))
print(bool(test_4))

#set -> str, list, tuple, bool

test_5 = {1, 2, 3, 2, 2}
print(str(test_5))
print(list(test_5))
print(tuple(test_5))
print(bool(test_5))

#dict -> str, list, tuple, set, bool

test_6 = {'age':0, 'car':1}
print(str(test_6))
print(list(test_6))
print(tuple(test_6))
print(set(test_6))
print(bool(test_6))

#bool -> int, float, str

test_7 = True
print(int(test_7))
print(float(test_7))
print(str(test_7))



