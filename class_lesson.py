import turtle
import pprint
player = turtle.Turtle()
player.speed(0)

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
    iteration = 4
    player.begin_fill()
    for i in range(iteration):
        player.fd(length)
        player.lt(90)
    player.end_fill()

def checker(color, radius, x, y):
    player.up()
    player.goto(x, y)
    player.down()
    player.fillcolor(color)
    player.begin_fill()
    player.circle(radius)
    player.end_fill()
    return x + y



def checker_board(x,y):
    figure = [1, 0, 1, 0, 1, 0, 1, 0]
    for item in figure:
        y = y - 50
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


def position_on_board():
    n = 8
    board = [[0] * n for item in range(n)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            condition = i < 3
            black_condition = i >= 5
            if condition and (i + j) % 2 != 0:
                board[i][j] = 1
            if black_condition and (i + j) % 2 != 0:
                board[i][j] = 2
    return board



def figure_position(radius, x, y):
    a = position_on_board()
    start = x
    for i in range(len(a)):
        for j in range(len(a[i])):
            condition = i < 3
            black_condition = i >= 5

            if (i+j) % 2 == 0:
                x += 50
                j *= 50
            else:
                if condition:
                    if a[i][j] == 1:
                        checker('white', radius, x, y)
                if black_condition:
                    if a[i][j] == 2:
                        checker('black', radius, x, y)
                x += 50
                j *= 50
        y = y - 50
        x = start
    pprint.pprint(a)




class Checker(turtle.Turtle):
    c = figure_position()
    #def __init__(self):
        #сhecker = Checker
        def draw(self, x, y):
            for i in range(len(c)):
                for j in range(len(c[i])):
                    condition = i < 3
                    black_condition = i >= 5

                    if (i+j) % 2 == 0:
                        x += 50
                        j *= 50
                    else:
                        if condition:
                            if c[i][j] == 1:
                                checker('white', 20, x, y)
                        if black_condition:
                            if c[i][j] == 2:
                                checker('black', 20, x, y)
                        x += 50
                        j *= 50
                y = y - 50
                x = start
            pprint.pprint(c)


print(сhecker1.mileage)
checker_board(-200, 250)
figure_position(20, (-200 + 25), (200 + 5))

player.hideturtle()
turtle.done()



for i in range(24):
    сhecker.draw()


    class Checker(turtle.Turtle):
        black = 'black'
        white = 'white'
        x = 0
        y = 0

        def create(self, color, x, y):
            ch.goto(x, y)
            rad = 20
            b = rad * 0.7
            a = rad - b
            ch.up()

            ch.down()
            ch.fillcolor('white')
            ch.begin_fill()
            ch.circle(rad)
            ch.end_fill()
            ch.lt(90)
            ch.up()
            ch.fd(a)
            ch.down()
            ch.rt(90)
            ch.fillcolor(color)
            ch.begin_fill()
            ch.circle(b)
            ch.end_fill()

        # def draw(self):

        # def draw(self, color, x, y):
        def draw(self):
            board_a()


    ch = Checker()
    ch.speed(0)
    ch.draw()
    ch.create(ch.white, ch.x, ch.y)

    # board_a(-200, 200)
    # ch.draw(color, x, y)
    # board[i, j] = ch
    # test('white', rad, x, y)

    turtle.done()
    сhecker2 = Checker()
    сhecker3 = Checker()
сhecker1 = Checker('black', x, y)
сhecker2 = Checker()
сhecker3 = Checker()
сhecker1 = Checker()
сhecker2 = Checker()
сhecker3 = Checker()
сhecker1 = Checker()
сhecker2 = Checker()
сhecker3 = Checker()
сhecker1 = Checker()
сhecker2 = Checker()
сhecker3 = Checker()


car3 = Car()
сhecker1.forward(25)
сhecker1.forward(56)
сhecker1.rt(25)
car1.forward(27)
car1.lt(13)
car1.forward(13)
car2.forward(250)
car2.forward(25)
car2.forward(56)
car2.rt(25)
car3.forward(27)
car3.lt(13)
car3.forward(13)
car3.forward(250)
