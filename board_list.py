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
    length = 50
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

def checker_board(x,y):
    figure = [1, 0, 1, 0, 1, 0, 1, 0]
    for item in figure:
        y = y + 50
        if item%2 == 1:
            for item in figure:
                if item%2 == 0:
                    square(x, y, 'SaddleBrown')
                else:
                    square(x, y, 'lightyellow')
                x=x+50
        else:
            for item in figure:
                if item%2 == 0:
                    square(x, y, 'lightyellow')
                else:
                    square(x, y, 'SaddleBrown')
                x=x+50

        x = -200




player.hideturtle()
turtle.done()