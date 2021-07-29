import turtle
from random import random
car = turtle.Turtle()
car.shape('turtle')


def create_car(x, y):
    turtle.tracer(False)
    car_xy = turtle.Turtle()
    car_xy.up()
    car_xy.goto(x, y)
    car_xy.fillcolor((random(), random(), random()))
    cars = []
    cars.append(car_xy)
    turtle.tracer(True)

def drive():
    create_car.goto(create_car, 1000)

turtle.onscreenclick(create_car)
turtle.ontimer(create_car, 100)
#cars = cars[]

#def drive():
    #turtle.tracer(False)
    #cars.goto(0, 10)
    #cars.clear()
    #cars.forward(1000)


    #turtle.tracer(True)




#turtle.ontimer(drive, 100)



turtle.done()