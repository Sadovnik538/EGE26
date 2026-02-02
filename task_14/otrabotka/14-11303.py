from string import printable as alph

for x in alph[:20]:
    num = int(f'627{x}j8',20) + int(f'h45i{x}5hij',20) + int(f'4idb49j{x}7',20)
    if num % 19 == 0:
        print(x, num//19)