def fact(num):
    d = []
    while num%2 ==0:
        d += 2
        num //= 2

    i = 3
    if i < int(num**0.5)+1:
        while num%i == 0:
            d += i
            num
