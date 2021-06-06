import turtle

player = turtle.Turtle()
size = 150

player.fd(size)
player.lt(90)
player.fd(size/10)
player.lt(90)
player.fd(size)
player.lt(90)
player.fd(size/10)
player.lt(180)
player.fd(size/10)


player.rt(60)
player.fd(size/4)
player.lt(60)
player.fd(size/1.5)
player.lt(60)
player.fd(size/5.25)
player.rt(60)
player.fd(size/10)
player.rt(90)
player.fd(size /10)

iter_rook = 3
for i in range(iter_rook+1):
    player.rt(90)
    player.fd(size/10)
    player.lt(90)
    player.fd(size/10)
    player.lt(90)
    player.fd(size / 10)
    player.rt(90)
    player.fd(size / 10)

player.rt(90)
player.fd(size/10)

player.rt(60)
player.fd(size/5.25)
player.lt(60)
player.fd(size/1.5)

player.lt(60)
player.fd(size/4)

#на новое место
player.rt(60)
player.fd(size/10)
player.rt(90)
player.up()
player.fd(400)
player.lt(90)

player.down()
player.lt(90)

#чёрная ладья
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
player.rt(60)
player.fd(size/4)
player.lt(60)
player.fd(size/1.5)
player.lt(60)
player.fd(size/5.25)
player.rt(60)
player.fd(size/10)
player.rt(90)
player.fd(size /10)

iter_rook = 3
for i in range(iter_rook+1):
    player.rt(90)
    player.fd(size/10)
    player.lt(90)
    player.fd(size/10)
    player.lt(90)
    player.fd(size / 10)
    player.rt(90)
    player.fd(size / 10)

player.rt(90)
player.fd(size/10)

player.rt(60)
player.fd(size/5.25)
player.lt(60)
player.fd(size/1.5)

player.lt(60)
player.fd(size/4)

player.end_fill()
player.hideturtle()

turtle.done()

