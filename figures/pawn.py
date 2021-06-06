import turtle

player = turtle.Turtle()
size = 80

player.fd(size)
player.lt(90)
player.fd(size/10)
player.lt(90)
player.fd(size)
player.lt(90)
player.fd(size/10)
player.lt(180)
player.fd(size/10)


iterations = 8

for i in range(iterations+1):
    player.fd(size/12)
    player.rt(7)

player.fd(size/20)
player.lt(63)
player.fd(size/5)
player.lt(90)
player.fd(size/10)
player.rt(90)
player.fd(size/10)
player.rt(90)
player.fd(size/10)
player.lt(90)
player.fd(size/10)
player.lt(60)

iter = 15
for i in range(iter+1):
    player.fd(size/9)
    player.rt(20)

player.lt(80)
player.fd(size/10)
player.lt(90)
player.fd(size/10)
player.rt(90)
player.fd(size/10)
player.rt(90)
player.fd(size/10)
player.lt(90)
player.fd(size/5)
player.lt(63)

for i in range(iterations+1):
    player.fd(size/12)
    player.rt(7)
player.fd(size/20)

player.fd(size/9)
player.hideturtle()



player.rt(90)
player.up()
player.fd(300)
player.lt(90)

player.down()
player.lt(90)

#чёрный

player.fillcolor('black')
player.begin_fill()
player.fd(size)
player.lt(90)
player.fd(size/10)
player.lt(90)
player.fd(size)
player.lt(90)
player.fd(size/10)
player.lt(180)
player.fd(size/10)
player.end_fill()


player.fillcolor('black')
player.begin_fill()
for i in range(iterations+1):
    player.fd(size/12)
    player.rt(7)

player.fd(size/20)
player.lt(63)
player.fd(size/5)
player.lt(90)
player.fd(size/10)
player.rt(90)
player.fd(size/10)
player.rt(90)
player.fd(size/10)
player.lt(90)
player.fd(size/10)
player.lt(60)


for i in range(iter+1):
    player.fd(size/9)
    player.rt(20)

player.lt(80)
player.fd(size/10)
player.lt(90)
player.fd(size/10)
player.rt(90)
player.fd(size/10)
player.rt(90)
player.fd(size/10)
player.lt(90)
player.fd(size/5)
player.lt(63)

for i in range(iterations+1):
    player.fd(size/12)
    player.rt(7)
player.fd(size/20)

player.fd(size/9)
player.end_fill()
player.hideturtle()


turtle.done()