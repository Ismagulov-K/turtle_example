import turtle
from typing import List, Tuple, Optional
import math



class Label(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__(shape='blank')
        self.up()
        self.goto(x, y)

    def msg(self, text):
        self.clear()
        self.write(text, align="left")


class Checker(turtle.Turtle):
    is_lady: bool = False

    def __init__(self, i: int, j: int, size: float, color):
        super().__init__(shape='circle')
        self.up()
        self._color = color
        self.fillcolor(color)
        self.pencolor('grey')
        self.goto(i * size, j * size)
        self.shapesize(1.6, 1.6, 2)

    def select_checker(self):
        self.pencolor('red')

    def unselect_checker(self):
        self.pencolor('grey')

    def is_black(self) -> bool:
        """Проверяет шашка чёрная или нет"""
        if self._color == 'white':
            return False
        elif self._color == 'black':
            return True

    def __str__(self):
        if self.is_black():
            return '0   '
        else:
            return '1   '

    def __repr__(self):
        return self.__str__()


class Square(turtle.Turtle):
    def __init__(self, i, j, size, color):
        super().__init__(shape='square')
        self.size = size
        self.up()
        self.fillcolor(color)
        self.goto(i * size, j * size)
        self.shapesize(2, 2)


class PointXy:
    x: int()
    y: int()


class Board(turtle.Turtle):

    board: List[List[Square]] = []
    size = 800
    count = 8
    checkers: List[List[Checker]] = []
    take_checker: Optional[Tuple[int, int]] = None
    status: Label = Label(-100, -150)
    step_white: bool = True

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

        #for i in self.checkers:
            #for j in i:
                #if j is not None:
                    #j.hideturtle()
                    #j = None

        turtle.tracer(False)

        for i in range(self.count):
            chess_line = []
            for j in range(self.count):
                is_set = (i + j) % 2

                if is_set:
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

    def trace_path(self, i1: int, j1: int, i2: int, j2: int):
        distance_i = i2 - i1
        distance_j = j2 - j1
        i: int = int(i1)
        j: int = int(j1)

        count_steps = abs(distance_i)
        trace_step = []

        for k in range(count_steps + 1):
            trace_step.append((i, j, str(self.checkers[i][j])))
            i += int(math.copysign(1, distance_i))
            j += int(math.copysign(1, distance_j))
        return trace_step



    def validation_move(self, i1: int, j1: int, i2: int, j2: int) -> bool:
        return True
        f: Checker = self.checkers[i1][j1]
        # 1 Ходить можно только шашкой пустым местом не ходим
        if f is None:
            self.status.msg('Не можем ходить пустым местом')
            return

    def move(self, i1: int, j1: int, i2: int, j2: int):

        f: Checker = self.checkers[i1][j1]

        # --> Троссировка шашки <-

        # 2 Ходить только в пустое место
        f1: Checker = self.checkers[i2][j2]
        if f1 is not None:
            self.status.msg('Нельзя ходить на другую шашку')
            return

        # 12 Шашка не может ходить назад
        if f.is_black():
            if i2 < i1:
                self.status.msg('Нельзя ходить назад')
                return
        else:
            if i2 > i1:
                self.status.msg('Нельзя ходить назад')
                return

        # 5. Шашка может ходить только на 1 клетку по диагонали



        f.goto(i2 * 40, j2 * 40)

        if self.step_white:
            self.status.msg('Ход белых')
        else:
            self.status.msg('Ход черных')

        self.step_white = not self.step_white

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

#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#
# class RoundButton(turtle.Turtle):
#     point1: Point
#     point2: Point
#     title: str
#
#     def __init__(self, point1: Point, point2: Point, title: str):
#         super(RoundButton, self).__init__()
#
#         self.point1 = point1
#         self.point2 = point2
#         self.title = title
#         self.round_button()
#
#     def round_button(self):
#         turtle.tracer(False)
#         self.hideturtle()
#
#         self.up()
#         self.goto(self.point1.x, self.point1.y)
#         radius = math.sqrt((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2)
#         self.down()
#         self.circle(radius)
#         turtle.tracer(True)
#         print(radius)
#
#     def on_button(self, x, y):
#         """Обработчик нажатия на кнопку"""
#         print('Нажата круглая кнопка')
#
#     def test_button(self, x: int, y: int):
#         """проверка нажатия на круглую кнопку"""
#         radius = math.sqrt((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2)
#         if ((self.point2.x - self.point1.x) ** 2) + ((self.point2.y - self.point1.y) ** 2) <= radius ** 2:
#             print(f'({x}, {y}')
#             # turtle.tracer(False)
#             # round_t = turtle.Turtle()
#             # round_t.shape('turtle')
#             # round_t.up()
#             # round_t.goto(x, y)
#             # turtle.tracer(True)
#             self.on_button(x, y)
#

turtle.tracer(False)
turtle.up()
turtle.goto(-50, -86)
turtle.down()
turtle.write("New game", font=("Arial", 16, "normal"))
turtle.hideturtle()
turtle.tracer(True)

board = Board()
b1 = SquareButton(Point(-100, -50), Point(100, -100), title=1, board=board)

buttons = [b1]


def on_click_screen(x, y):
    print('клик в точку (', x, y, ')')
    size = 40
    x1, y1 = -size // 2, -size // 2

    if x < x1 or y < y1 or y > 8 * size or x > 8 * size:
        print('мимо')
        return

    cx, cy = x - x1, y - y1
    i, j = int(cx // size), int(cy // size)
    check = board.checkers[i][j]

    print('норм координаты', i, j)
    print(check)

    if board.take_checker is None:
        board.take_checker = (i, j)
        active_checker = board.checkers[i][j]
        if active_checker is not None:
            active_checker.select_checker()
    else:
        board.move(
            board.take_checker[0], board.take_checker[1],
            i, j
        )
        act_checker = board.checkers[board.take_checker[0]][board.take_checker[1]]
        if act_checker is not None:
            act_checker.unselect_checker()

        board.take_checker = None


turtle.onscreenclick(on_click_screen)

turtle.done()
