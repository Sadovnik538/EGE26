#args

def f1(a, b, c):
    return a + b + c

test1 = [1, 2, 3]
print(f1(*test1[:10]))


#kwargs
def f2(a, b):
    return a / b

test2 = {'b': 2, 'a': 5}
print(f2(**test2))

# aftocod
from itertools import product, permutations

def f(x, y, z, w):
    return (x or y) and not (y == z) and not w

for i in product((0, 1), repeat=4):
    table = [
        (1, i[0], 1, i[1]),
        (0, 1, i[2], 0),
        (i[3], 1, 1, 0)
    ]
    # zip(p, t) - сопоставляет заголовки из p c значениями из t;
    # dict(zip(p, t)) - преобразует zip объект в базовый тип данных (словарь);
    # f(**dict(zip(p, t))) - распаковывает через kwargs все ключи в функцию;

    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
                print(*p, sep='')
