import turtle

player = turtle.Turtle()
player.speed(0)

length = 200
position = length/2
player.rt(180)
player.up()
player.fd(position)
player.lt(90)
player.fd(position)
player.down()
player.lt(90)

iterations = 4
for j in range(iterations):
    for i in range(iterations):
        player.fillcolor('SaddleBrown')
        player.begin_fill()
        player.fd(length/8)
        player.lt(90)
        player.fd(length/8)
        player.lt(90)
        player.fd(length/8)
        player.lt(90)
        player.fd(length/8)
        player.end_fill()
        player.lt(90)
        player.fd(length/4)
    player.lt(90)
    player.fd(length/8)
    player.lt(90)
    player.fd(length)
    player.lt(180)
    for i in range(iterations):
        player.fd(length/8)
        player.lt(90)
        player.fd(length/8)
        player.lt(90)
        player.fd(length/8)
        player.lt(90)
        player.fd(length/8)
        player.lt(90)
        player.fd(length/4)
        player.fillcolor('SaddleBrown')
        player.begin_fill()
        player.lt(90)
        player.fd(length / 8)
        player.lt(90)
        player.fd(length / 8)
        player.lt(90)
        player.fd(length / 8)
        player.lt(90)
        player.fd(length / 8)
        player.end_fill()
    player.lt(90)
    player.fd(length/8)
    player.lt(90)
    player.fd(length)
    player.lt(180)








player.hideturtle()
turtle.done()