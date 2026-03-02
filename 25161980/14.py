from string import printable as alph

ans = []
for y in range(9, 18):
    for x in range(y):
        num = int(f'5{alph[x]}{alph[y]}a', 18) + int(f'18{alph[x]}7', y)
        ans.append(num)

print(len(set(ans)))


