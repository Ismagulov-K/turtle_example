import turtle
player = turtle.Turtle()

def checker(x, y, size, color):
    """
    Нарисуем фигуру в нужном месте
    :param x: координата Х фигуры
    :param y: координата У фигуры
    :param color: цвет фигуры
    :return: в нужном положении рисуется фигура
    """
    player.speed(0)
    player.up()
    player.goto(x, y)
    player.down()
    player.fillcolor(color)

    iterations = 30
    player.begin_fill()


    for i in range(iterations+1):
        player.fd(size/iterations)
        player.left(360/iterations)


    player.end_fill()

checker(0, 0, 360,'darkgrey')
checker(11, 10, 300, 'white')
checker(15, 20, 240, 'darkgrey')


#player.circle(100)
#player.circle(800)
#player.circle(600)


player.hideturtle()
turtle.done()