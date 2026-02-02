# Псевдослучайные числа

from random import random, uniform, randint, randrange, choice, choices, sample

#Генерирует псевдослучайные числа типа float от 0.0 до 1.0 включительно
rand_1 = random()
print(rand_1)

#Генерирует псевдослучайные числа типа float в указанном диапазоне
rand_2 = uniform(2.5, 5.5)
print(rand_2)

#Генерирует псевдослучайные числа типа int в указанном диапазоне
rand_3 = randint(0, 10)
print(rand_3)

#Генерирует псевдослучайные числа типа int в указанном диапазоне с шагом
rand_4 = randrange(0, 20, 2)
print(rand_4)


list = [10, 67, 98, 1]

# Выбирает 1 псевдослучайный элемент из списка
rand_5 = choice(list)
print(rand_5)

#Выбирает k элементов из списка cлучайным образом
rand_6 = choices(list, k=9)
print(rand_6)

# Выбирает K элементов из списка без дублирования
rand_7 = sample(list, 3)
print(rand_7)




