import turtle
import math

class Checker(turtle.Turtle):
    def __init__(self, i, j, size, color):
        super().__init__(shape='circle')
        self.up()
        self.fillcolor(color)
        self.pencolor('grey')
        self.goto(i*size, j*size)
        self.shapesize(1.6, 1.6, 2)

class Square(turtle.Turtle):
    def __init__(self, i, j, size, color):
        super().__init__(shape='square')
        self.size = size
        self.up()
        self.fillcolor(color)
        self.goto(i * size, j * size)
        self.shapesize(2, 2)

class Board(turtle.Turtle):
    board = []
    size = 800
    count = 8
    checkers = []

    def __init__(self, size=800, count=8):
        super().__init__()
        self.size = size
        self.count = count
        self.create_board()
        self.create_checkers()

    def create_board(self):
        turtle.tracer(False)
        for i in range(self.count):
            board_line = []
            for j in range(self.count):
                color = (i + j) % 2
                color = 'SaddleBrown' if color == 1 else 'lightyellow'
                board_line.append(Square(i, j, 40, color=color))
            self.board.append(board_line)
        turtle.tracer(True)

    def create_checkers(self):
        # TODO:
        for i in self.checkers:
            for j in i:
                if j is not None:
                    j.hideturtle()
                    j = None


        turtle.tracer(False)

        for i in range(self.count):
            chess_line = []
            for j in range(self.count):
                set = (i+j) % 2
                if set:
                    if i < 3:
                        checker = Checker(i, j, 40, 'black')
                        chess_line.append(checker)
                        continue
                    if i >= 5:
                        checker = Checker(i, j, 40, 'white')
                        chess_line.append(checker)
                        continue
                chess_line.append(None)
            self.checkers.append(chess_line)
        turtle.tracer(True)

    def move(self, i1, j1, i2, j2):
        f: Checker = self.checkers[i1][j1]
        if f is None:
            return
        f.goto(i2 * 40, j2 * 40)

        self.checkers[i2][j2] = f
        self.checkers[i1][j1] = None


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Button(turtle.Turtle):
    point1: Point
    point2: Point
    title: str

    def __init__(self, point1: Point, point2: Point, title: str):
        super(Button, self).__init__()

        self.point1 = point1
        self.point2 = point2
        self.title = title

        self.draw_button()

    def draw_button(self):
        turtle.tracer(False)
        self.hideturtle()

        self.up()
        self.goto(self.point1.x, self.point1.y)
        self.down()
        self.goto(self.point2.x, self.point1.y)
        self.goto(self.point2.x, self.point2.y)
        self.goto(self.point1.x, self.point2.y)
        self.goto(self.point1.x, self.point1.y)
        turtle.tracer(True)

    def on_button(self, x, y):
        """Обработчик нажатия на кнопку"""
        pass

    def test_button(self, x: int, y: int):
        """проверка нажатия на кнопку"""
        pass


class SquareButton(Button):
    def __init__(self, point1: Point, point2: Point, title: str, board: Board):
        super(SquareButton, self).__init__(point1, point2, title)
        self.board = board

    def on_button(self, x, y):
        """Обработчик нажатия на кнопку"""
        print('Новая игра')
        self.board.create_checkers()


    def test_button(self, x: int, y: int):
        """проверка нажатия на кнопку"""
        if self.point1.x < x < self.point2.x and self.point1.y > y > self.point2.y:
            print(f'({x}, {y}')
            self.on_button(x, y)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class RoundButton(turtle.Turtle):
    point1: Point
    point2: Point
    title: str

    def __init__(self, point1: Point, point2: Point, title: str):

        super(RoundButton, self).__init__()

        self.point1 = point1
        self.point2 = point2
        self.title = title
        self.round_button()

    def round_button(self):

        turtle.tracer(False)
        self.hideturtle()

        self.up()
        self.goto(self.point1.x, self.point1.y)
        radius = math.sqrt((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2)
        self.down()
        self.circle(radius)
        turtle.tracer(True)
        print(radius)

    def on_button(self, x, y):
        """Обработчик нажатия на кнопку"""
        print('Нажата круглая кнопка')

    def test_button(self, x: int, y: int):
        """проверка нажатия на круглую кнопку"""
        radius = math.sqrt((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2)
        if ((self.point2.x - self.point1.x)**2) + ((self.point2.y - self.point1.y)**2) <= radius**2:
            print(f'({x}, {y}')
            #turtle.tracer(False)
            #round_t = turtle.Turtle()
            #round_t.shape('turtle')
            #round_t.up()
            #round_t.goto(x, y)
            #turtle.tracer(True)
            self.on_button(x, y)

turtle.tracer(False)
turtle.up()
turtle.goto(-50, -86)
turtle.down()
turtle.write("New game", font=("Arial", 16, "normal"))
turtle.hideturtle()
turtle.tracer(True)



board = Board()
b1 = SquareButton(Point(-100, -50), Point(100, -100), title=1, board=board)

board.move(2, 3, 3, 2)
board.move(5, 0, 4, 1)
board.move(3, 2, 5, 0)
board.move(2, 1, 3, 2)

board.move(5, 6, 4, 7)
board.move(2, 7, 3, 6)
board.move(6, 7, 5, 6)
board.move(1, 0, 2, 1)

board.move(5, 4, 4, 5)
board.move(2, 5, 3, 4)
board.move(5, 2, 4, 3)
board.move(5, 2, 4, 3)

board.move(1, 2, 2, 3)
board.move(6, 5, 5, 4)
board.move(2, 1, 3, 0)
board.move(6, 1, 5, 2)

board.move(1, 4, 2, 5)
board.move(7, 6, 6, 7)
board.move(1, 6, 2, 7)
board.move(7, 4, 6, 5)

board.move(0, 1, 1, 0)
board.move(7, 0, 6, 1)
board.move(0, 3, 1, 2)
board.move(4, 3, 2, 1)

board.move(2, 1, 0, 3)
board.move(0, 5, 1, 4)
board.move(5, 2, 4, 3)
board.move(3, 4, 5, 2)

board.move(5, 2, 7, 4)
board.move(4, 5, 3, 4)
board.move(0, 7, 1, 6)
board.move(6, 1, 5, 2)

board.move(3, 6, 4, 5)
board.move(7, 2, 6, 1)

buttons = [b1]

def on_click_screen(x,y):
    for obj in buttons:
        obj.test_button(x, y)



turtle.onscreenclick(on_click_screen)

turtle.done()