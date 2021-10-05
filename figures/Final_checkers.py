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

    def __init__(self, i: int, j: int, size: float, color: Tuple[float, float, float]):
        super().__init__(shape='circle')
        self.up()
        self._color = color
        self.fillcolor(color)
        self.pencolor('grey')
        self.goto(i * size, j * size)
        self.shapesize(1.6, 1.6, 2)

    def set_lady(self):
        self.is_lady = True
        self.shapesize(1.6, 1.6, 6)
        self.pencolor('green')

    def select_checker(self):
        self.pencolor('red')

    def unselect_checker(self):
        self.pencolor('grey')

    def is_black(self):
        """Проверяет шашка чёрная или нет"""
        if self._color == 'black':
            return False
        else:
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


class Board(turtle.Turtle):

    board: List[List[Square]] = []
    size = 800
    count = 8
    checkers: List[List[Checker]] = []
    take_checker: Optional[Tuple[int, int]] = None
    status: Label = Label(-100, -150)
    error: Label = Label(-200, -250)
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

     def move(self, i1: int, j1: int, i2: int, j2: int):

        distance_i = i2 - i1
        distance_j = j2 - j1
        i: int = int(i1)
        j: int = int(j1)

        count_steps = abs(distance_i)
        trace_step = []

        # 1 Ходить можно только шашкой пустым местом не ходим
        f: Checker = self.checkers[i1][j1]

        if f is None:
            self.error.msg('Не можем ходить пустым местом')
            return

        for k in range(count_steps + 1):
            trace_step.append((i, j, str(self.checkers[i][j])))
            i += int(math.copysign(1, distance_i))
            j += int(math.copysign(1, distance_j))

        victim_list = []

        if len(trace_step) >= 3:
            checker_attack = trace_step[0][2]
            attack_is_black = checker_attack.is_black()

            for kill_checker_tuple in trace_step:
                victim = kill_checker_tuple[2]

                if victim is None:
                    continue

                victim_is_black = victim_is_black()

                if attack_is_black != victim_is_black:
                    victim_list.append(kill_checker_tuple)


        # 2 Ходить только в пустое место
        f1: Checker = self.checkers[i2][j2]
        if f1 is not None:
            self.error.msg('Нельзя ходить на другую шашку')
            return

        f: Checker = self.checkers[i1][j1]

        # --> Троссировка шашки <-


        # 12 Шашка не может ходить назад
        if f.is_lady:
            if f.is_black():
                if i2 < i1:
                    self.error.msg('Нельзя ходить назад')
                    return
                else:
                    if i2 == i1 or j2 == j1:
                        self.error.msg('Неверный ход!')
                        return

            else:
                if i2 > i1:
                    self.error.msg('Нельзя ходить назад')
                    return
                else:
                    if i2 == i1 or j2 == j1:
                        self.error.msg('Неверный ход!')
                        return
        # Нельзя ходить через две клетки
        if f.is_lady:
            if f.is_black():
                if trace_step[1][2] is not None:
                    print('Верный ход')
                else:
                    if len(trace_step) >= 3:
                        self.error.msg('Нельзя ходить через две пустые клетки')
                        return
            else:
                if trace_step[1][2] is not None:
                    print('Верный ход')
                else:
                    if len(trace_step) >= 3:
                        self.error.msg('Нельзя ходить через две пустые клетки')
                        return

        # 7. Шашка превращается в дамку на противоположной стороне

        if f.is_black():
            if i2 == board.count - 1:
                f.set_lady()
        else:
            if i2 == 0:
                f.set_lady()

        # 4. дамка может ходить по диагонали в любое место

        first_step = trace_step[0]
        last_step = trace_step[-1]
        first_eq = first_step[0] == i1 and first_step[1] == j1
        last_eq = last_step[0] == i2 and last_step[1] == j2

        if not (first_eq and last_eq):
            self.error.msg('Ходить можно только по диагонали')
            return

        # 10. Дамка может бить по диагонали только чужих

        for color_is_black in trace_step[1:]:
            if first_step[2] is not None and first_step[2].is_black() == color_is_black[2].is_black():
                self.error.msg('Своих рубить нельзя!')
                return

        f.goto(i2 * 40, j2 * 40)

        for next_victim in victim_list

        if self.step_white:
            self.status.msg('Ход белых')
        else:
            self.status.msg('Ход черных')

        self.step_white = not self.step_white

        self.checkers[i2][j2] = f
        self.checkers[i1][j1] = None

turtle.tracer(False)
board = Board()
turtle.tracer(True)

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
        active_i = board.take_checker[0]
        active_j = board.take_checker[1]
        board.move(
            active_i, active_j,
            i, j
        )
        act_checker = board.checkers[active_i][active_j]
        if act_checker is not None:
            act_checker.unselect_checker()

        board.take_checker = None


turtle.onscreenclick(on_click_screen)

turtle.done()
