import turtle
import pprint
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

def checker_board(x,y, board):
    i=0
    j=0
    figure = board
    for i in range(len(figure)):
        for j in range(len(figure[i])):
            y = y + 50
            if i%2 == 1:
                for i in figure:
                    if i%2 == 0:
                        square(x, y, 'SaddleBrown')
                    else:
                        square(x, y, 'lightyellow')
                    x=x+50
            else:
                for j in figure:
                    if j%2 == 0:
                        square(x, y, 'lightyellow')
                    else:
                        square(x, y, 'SaddleBrown')
                    x=x+50

            x = -200

n=10
board=[[0]*n for ii in range(n)]

for i in range(len(board)):
    for j in range(len(board[i])):
        if i >= 5 and (i+j)%2==0:
            board[i][j] = 2
        if i < 3 and (i+j)%2==0:
            board[i][j] = 1

checker_board(-200, -200, board)
pprint.pprint(board)

player.hideturtle()
turtle.done()