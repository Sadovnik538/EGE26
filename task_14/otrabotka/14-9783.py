from string import printable as alph

for x in alph[:22]:
    num = int(f'18{x}89957', 22) + int(f'80{x}33', 22) + int(f'521{x}6', 22)
    if num % 21 == 0:
        print(x, num // 21)

# Так как надо найти наименьшее значение, мы будем смотреть на первую строку