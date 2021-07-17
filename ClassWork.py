import turtle
turtle.tracer(0)

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
        self.lines()

    def create_board(self):
        for i in range(self.count):
            board_line = []
            for j in range(self.count):
                color = (i + j) % 2
                color = 'SaddleBrown' if color == 1 else 'lightyellow'
                board_line.append(Square(i, j, 40, color=color))
            self.board.append(board_line)

    def main_diagonal(self):
        for i in range(self.count):
            chess_line = []

            for j in range(self.count):
                if i == self.count - (1+j):
                    checker = Checker(i, j, 40, 'black')
                    chess_line.append(checker)
                    continue
                if i == j:
                    checker = Checker(i, j, 40, 'white')
                    chess_line.append(checker)
                    continue
                chess_line.append(None)
            self.checkers.append(chess_line)

    def cross(self):
        for i in range(self.count):
            chess_line = []

            for j in range(self.count):
                m_diagonal = i
                s_diagonal = self.count - i -1
                if j <= s_diagonal and j >= m_diagonal:
                    checker = Checker(i, j, 40, 'black')
                    chess_line.append(checker)
                    continue
                if j >= s_diagonal and j <= m_diagonal:
                    checker = Checker(i, j, 40, 'white')
                    chess_line.append(checker)
                    continue
                chess_line.append(None)
            self.checkers.append(chess_line)

    def lines(self):
        for i in range(self.count):
            chess_line = []

            for j in range(self.count):
                m_diagonal = i
                s_diagonal = self.count - i - 1
                if j < s_diagonal and j > m_diagonal:
                    if i % 2 == 0:
                        color = 'black'
                    else:
                        color = 'white'
                    checker = Checker(i, j, 40, color)
                    chess_line.append(checker)
                    continue

                if j < s_diagonal and i > j:
                    if j % 2 == 1:
                        color = 'black'
                    else:
                        color = 'white'
                    checker = Checker(i, j, 40, color)
                    chess_line.append(checker)
                    continue

                if i == j or j == s_diagonal:
                    color='white'
                    checker = Checker(i, j, 40, color)
                    chess_line.append(checker)
                    continue
                chess_line.append(None)

                if j > s_diagonal and j < m_diagonal:
                    if i % 2 == 1:
                        color = 'black'
                    else:
                        color = 'white'
                    checker = Checker(i, j, 40, color)
                    chess_line.append(checker)
                    continue

                if j > s_diagonal and i < j:
                    if j % 2 == 0:
                        color = 'black'
                    else:
                        color = 'white'
                    checker = Checker(i, j, 40, color)
                    chess_line.append(checker)
                    continue

            self.checkers.append(chess_line)

    def move(self, i1, j1, i2, j2):
        f: Checker = self.checkers[i1][j1]
        if f is None:
            return
        f.goto(i2 * 40, j2 * 40)

        self.checkers[i2][j2] = f
        self.checkers[i1][j1] = None

board = Board()



turtle.tracer(1)
turtle.done()