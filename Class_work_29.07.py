import turtle
square_button = turtle.Turtle()
round_button = turtle.Turtle()
turtle.tracer(False)
square_button.up()
square_button.goto(-200, 0)
square_button.down()
square_button.left(180)
for i in range(4):
    square_button.forward(100)
    square_button.left(90)

round_button.up()
round_button.goto(0, -50)
round_button.down()
radius = 50
round_button.circle(radius)

turtle.tracer(True)

def button_click(x, y):
    turtle.tracer(False)
    if x>=-300 and x<=-200 and y>=-100 and y<0:
        print('Это квадратная кнопка')
    if (x**2+y**2) <= (radius**2):
        print('Это круглая кнопка')
    turtle.tracer(True)


turtle.onscreenclick(button_click)

turtle.done()