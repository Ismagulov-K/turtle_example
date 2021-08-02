import turtle
import math

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
        self.goto(self.point1.x,self. point1.y)
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
    def on_button(self, x, y):
        """Обработчик нажатия на кнопку"""
        print('Нажата квадратная кнопка')

    def test_button(self, x: int, y: int):
        """проверка нажатия на кнопку"""
        if self.point1.x < x < self.point2.x and self.point1.y > y > self.point2.y:
            print(f'({x}, {y}')
            self.on_button(x, y)


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

        #turtle.tracer(False)
        self.hideturtle()

        self.up()
        self.goto(self.point1.x, self.point1.y)
        radius = math.sqrt((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2)
        self.down()
        self.circle(radius)
        #turtle.tracer(True)
        print(radius)

    def on_button(self, x, y):
        """Обработчик нажатия на кнопку"""
        print('Нажата круглая кнопка')

    def test_button(self, x: int, y: int):
        """проверка нажатия на круглую кнопку"""
        radius = math.sqrt((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2)
        if math.sqrt((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2) < radius:
            print(f'({x}, {y}')
            #turtle.tracer(False)
            #round_t = turtle.Turtle()
            #round_t.shape('turtle')
            #round_t.up()
            #round_t.goto(x, y)
            #turtle.tracer(True)
            self.on_button(x, y)

class HelloButton(SquareButton):
    def on_button(self, x, y):
        print(f'Hello from button {self.title}')
        turtle.tracer(False)
        t = turtle.Turtle()
        t.up()
        t.goto(x, y)
        turtle.tracer(True)

b1 = SquareButton(Point(-300,0), Point(-200, -200), title=1)
b2 = HelloButton(Point(0, 0), Point(200, -200), title=2)
b3 = RoundButton(Point(50, 50), Point(100, 100), title=3)

buttons = [b1, b2, b3]

def on_click_screen(x,y):
    for obj in buttons:
        obj.test_button(x, y)

turtle.onscreenclick(on_click_screen)

turtle.done()
