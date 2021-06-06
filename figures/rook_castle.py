import turtle

player = turtle.Turtle()
size = 100

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

#player.fd(size/20)
player.rt(90)
player.fd(size/10)

player.rt(60)
player.fd(size/5.25)
player.lt(60)
player.fd(size/1.5)

player.lt(60)
player.fd(size/4)


player.hideturtle()
turtle.done()

