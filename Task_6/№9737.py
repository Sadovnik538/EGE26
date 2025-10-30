from turtle import *

screensize(3000,3000)
tracer(0)

m = 20

for i in range(2):
    forward(10*m)
    rt(90)
    fd(18*m)
    rt(90)

penup()
fd(5*m)
rt(90)
fd(7*m)
lt(90)
down()

for i in range(2):
    fd(10*m)
    rt(90)
    fd(7*m)
    rt(90)

penup()

for x in range(-10,20):
    for y in range (-20,10):
        goto(x*m,y*m)
        dot(4,'blue')

update()
done()