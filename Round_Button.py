import turtle
import math

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


b1 = RoundButton(Point(50, 50), Point(100, 100), title='circle')

buttons = [b1]

def on_click_screen(x,y):
    for obj in buttons:
        obj.test_button(x, y)

turtle.onscreenclick(on_click_screen)

turtle.done()
