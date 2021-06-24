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


    for i in range(iterations):
        player.fd(size/iterations)
        player.left(360/iterations)


    player.end_fill()



figure = [1, 0, 1, 1, 1, 1, ]
x=-200
y=0
for item in figure:
    if item%2 == 0:
        checker(x, y, 360, 'darkgrey')
    else:
        checker(x, y, 300, 'black')
    x=x+150

player.hideturtle()
turtle.done()