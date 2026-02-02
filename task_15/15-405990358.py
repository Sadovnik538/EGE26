def f(A, x, y):
    return (x<A) or (y<A) or ((x + 2*y)>50)

for A in range(0,1000):
    if all(f(A, x, y) for x in range(0,1000) for y in range(0,1000)):
        print(A)
        break



# def f(A):
#     for x in range(0, 1000):
#         for y in range(0,1000):
#             F = (x<A) or (y<A) or ((x + 2*y)>50)
#             if not F:
#                 return False
#     return True
#
#
# for A in range(-10, 1000): #здесь в рэндже мы указываем любые числа, просто потом когда принтовать будем изменим рендж так, как нам выгодней чтоб список прекратился
#     if f(A):
#         print(A)