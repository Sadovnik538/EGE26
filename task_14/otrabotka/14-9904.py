from string import printable as alph
# y -> 9 ... 2
# x -> y+1 ... 13

ans = []
for y in range(9, 13):
    for x in range(y + 1, 14):
        num = int(f'7{alph[x]}37{alph[y]}', 14) + int(f'9{alph[y]}63', x) - int(f'15148', y)
        ans.append([num, num // (x+y)])
print(max(ans))

