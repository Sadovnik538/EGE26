def convert(num, sys):
    res = ''
    while num:
        res = str(num%sys) + res
        num = num//sys
    return res


cnt_2 = 0
for x in range(1, 9430):
    num_1 = 39**483 + 39**235 - x
    num_2 = convert(num_1, 39)
    cnt = 0
    for i in num_2:
        if i in '0':
            cnt += 1
    if cnt > cnt_2:
        cnt_2 = max([cnt, cnt_2])
    if cnt == cnt_2:
        cnt_2 = cnt

print(cnt_2)