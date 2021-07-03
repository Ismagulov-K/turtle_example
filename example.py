import turtle
import pprint

board = turtle.Turtle()
board.speed(0)

def black_white(color, fd, x, y):  # Рисует
    board.up()
    board.goto(x, y)
    board.down()
    iterations = 4
    board.fillcolor(color)
    board.begin_fill()
    for i in range(iterations):
        board.fd(fd/iterations)
        board.lt(360/iterations)
    board.end_fill()
    board.fd(fd/iterations)

def test(color, rad, x, y):
    b = rad * 0.7
    a = rad - b
    board.up()
    board.goto(x, y)
    board.down()
    board.fillcolor('white')
    board.begin_fill()
    board.circle(rad)
    board.end_fill()
    board.lt(90)
    board.up()
    board.fd(a)
    board.down()
    board.rt(90)
    board.fillcolor(color)
    board.begin_fill()
    board.circle(b)
    board.end_fill()
    return x + y

def board_a(x, y):
    start = x
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                black_white('white', 200, x, y)
                x += 50
                j *= 50
            else:
                black_white('black', 200, x, y)
                x += 50
                j *= 50
        y = y - 50
        x = start



def figure_position(rad, x, y):
    c = list_initialization()
    start = x
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
                        test('white', rad, x, y)
                if black_condition:
                    if c[i][j] == 2:
                        test('black', rad, x, y)
                x += 50
                j *= 50
        y = y - 50
        x = start
    pprint.pprint(c)


def list_initialization():
    n = 8
    a = [[0] * n for item in range(n)]
    for i in range(len(a)):
        for j in range(len(a[i])):
            condition = i < 3
            black_condition = i >= 5
            if condition and (i + j) % 2 != 0:
                a[i][j] = 1
            if black_condition and (i + j) % 2 != 0:
                a[i][j] = 2
    return a
    # pprint.pprint(a)
board_a(-200, 200)
figure_position(20, (-200 + 25), (200 + 5))
turtle.done()
