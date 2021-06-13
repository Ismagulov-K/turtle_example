import turtle
player = turtle.Turtle()

def paint_figure(x, y, color):
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

    iterations = 10
    player.begin_fill()

    for j in range(iterations):
        for i in range(iterations+1):
            player.fd(200/iterations)
            player.left(360/iterations)

        player.fd(200/iterations)
    player.end_fill()

paint_figure(100, 100, color='red')
paint_figure(100, -100, 'orange')
paint_figure(-100, 100, 'green')
paint_figure(-100, -100, (1, 1, .5))
paint_figure(0, 0, 'blue')


player.hideturtle()
turtle.done()