import turtle
#turtle.tracer(0)
#player = turtle.Turtle()
#player.speed(0)

class Checker(turtle.Turtle):
    def __init__(self, i, j, size, color):
        super().__init__(shape='circle')
        self.up()
        self.fillcolor(color)
        self.pencolor('white')
        self.goto(i*size, j*size)
        self.shapesize(0.8, 0.8)

class SquareBoard(turtle.Turtle):
    def __init__(self, i, j, size, color):
        super().__init__(shape='square')
        self.size = size
        self.up()
        self.fillcolor(color)
        self.goto(i * size, j * size)
        self.shapesize(1, 1)

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
                color = 'black' if color == 1 else 'white'
                board_line.append(SquareBoard(i, j, 20, color=color))

            self.board.append(board_line)

    def create_checkers(self):
        for i in range(self.count):
            chess_line = []

            for j in range(self.count):
                is_set = (i+j) % 2

                if is_set:
                    if i < 3:
                        c = 0.2 + i / 8
                        checker = Checker(i, j, 20, (c, c, c))
                        chess_line.append(checker)
                        continue
                    if i >= 5:
                        c = 0 + (i / 8)
                        checker = Checker(i, j, 20, (c, c, c))
                        chess_line.append(checker)
                        continue
                chess_line.append(None)
            self.checkers.append(chess_line)

    def move(self, i1, j1, i2, j2):
        f: Checker = self.checkers[i1][j1]
        if f is None:
            return
        f.goto(i2 * 20, j2 * 20)

        self.checkers[i2][j2] = f
        self.checkers[i1][j1] = None

board = Board()
board.move(2, 3, 3, 2)
board.move(5, 0, 4, 1)
board.move(3, 2, 5, 0)




#player.hideturtle()
#turtle.tracer(1)
turtle.done()




