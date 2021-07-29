import turtle
clock = turtle.Turtle()
hour = turtle.Turtle()
min = turtle.Turtle()
sec = turtle.Turtle()
make_sec = turtle.Turtle()
make_min = turtle.Turtle()
min.color('red')
min.pensize(3)
hour.color('blue')
hour.pensize(5)

clock.up()
clock.goto(0, -110)
clock.down()
clock.pensize(3)
clock.shapesize(outline=3)
clock.circle(110)
clock.hideturtle()

def tik_tak():
    turtle.tracer(False)
    sec.goto(0, 0)
    min.goto(0, 0)
    hour.goto(0, 0)

    make_min.pensize(3)
    sec.clear()
    min.clear()
    hour.clear()

    angle_delta = 360 / 60
    make_sec.setheading(make_sec.heading() - angle_delta)
    make_min.setheading(make_min.heading()-angle_delta * 5)
    hour.setheading(hour.heading() - angle_delta / 360)
    min.setheading(min.heading() - angle_delta / 60)
    sec.setheading(sec.heading() - angle_delta)

    sec.forward(100)
    min.forward(80)
    hour.forward(50)

    make_sec.up()
    make_sec.forward(100)
    make_sec.down()
    make_sec.forward(10)
    make_sec.up()
    make_sec.goto(0, 0)
    make_sec.down()

    make_min.up()
    make_min.forward(95)
    make_min.down()
    make_min.forward(15)
    make_min.up()
    make_min.goto(0, 0)
    make_min.down()


    turtle.ontimer(tik_tak, 1000)
    turtle.tracer(True)
    make_sec.hideturtle()
    make_min.hideturtle()




sec.left(90)
min.left(90)
hour.left(90)
make_min.left(90)
make_sec.left(90)
turtle.ontimer(tik_tak, 1000)

turtle.done()