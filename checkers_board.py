import turtle
player = turtle.Turtle()

def square(x, y, color):
    """
    Нарисуем фигуру в нужном месте
    :param x: координата Х фигуры
    :param y: координата У фигуры
    :param color: цвет фигуры
    :return: в нужном положении рисуется фигура
    """
    length = 30
    player.speed(0)
    player.up()
    player.goto(x, y)
    player.down()

    player.fillcolor(color)
    iterations = 1
    for i in range(iterations):
        player.begin_fill()
        player.fd(length)
        player.lt(90)
        player.fd(length)
        player.lt(90)
        player.fd(length)
        player.lt(90)
        player.fd(length)
        player.end_fill()
        player.lt(90)
        player.fd(length)


iterations = 8
for k in range(iterations):

    for j in range(8):
        if (j+k)%2==0:
            square(j*30, k*30, 'SaddleBrown')
        else:
            square(j*30, k*30, 'lightyellow')



#for l in range(iterations):


#square(j*(l*30)+30, 0, 'lightyellow')

#player.lt(180)
#player.fd(120)
#player.lt(180)





#player.hideturtle()
turtle.done()