import turtle

player = turtle.Turtle()
player.speed(0)

length = 400
position = length/2
player.rt(180)
player.up()
player.fd(position)
player.lt(90)
player.fd(position)
player.down()
player.lt(90)

iterations = 7

for i in range(iterations+1):
    player.fd(length)
    player.lt(180)
    player.up()
    player.fd(length)
    player.rt(90)
    player.fd(length/iterations)
    player.rt(90)
    player.down()

player.rt(90)
player.up()
player.fd(length/iterations)
player.down()
player.lt(90)

for i in range(iterations+1):
    player.rt(90)
    player.fd(length)
    player.lt(180)
    player.up()
    player.fd(length)
    player.rt(90)
    player.fd(length/iterations)
    player.down()



player.hideturtle()
turtle.done()