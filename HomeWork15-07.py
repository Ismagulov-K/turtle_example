import turtle
#turtle.tracer(0)

class Checker(turtle.Turtle):
    def __init__(self, i, j, size, color):
        super().__init__(shape='circle')
        self.up()
        self.fillcolor(color)
        self.pencolor('white')
        self.goto(i*size, j*size)
        self.shapesize(1.6, 1.6)

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
        for i in range(self.count):
            board_line = []
            for j in range(self.count):
                color = (i + j) % 2
                color = 'SaddleBrown' if color == 1 else 'lightyellow'
                board_line.append(Square(i, j, 40, color=color))
            self.board.append(board_line)

    def create_checkers(self):
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

    def move(self, i1, j1, i2, j2):
        f: Checker = self.checkers[i1][j1]
        if f is None:
            return
        f.goto(i2 * 40, j2 * 40)

        self.checkers[i2][j2] = f
        self.checkers[i1][j1] = None

board = Board()
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

#turtle.tracer(1)
turtle.done()




