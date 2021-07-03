import turtle

class Car(turtle.Turtle):
    mileage = 0
    def forward(self, distance):
        super().forward(distance)
        self.mileage +=distance

class Checker(turtle.Turtle):
    def draw(self, color, x, y):
        pass


car = Car()
car1 = Car()
car2 = Car()
car3 = Car()
car.forward(25)
car.forward(56)
car.rt(25)
car1.forward(27)
car1.lt(13)
car1.forward(13)
car2.forward(250)
car2.forward(25)
car2.forward(56)
car2.rt(25)
car3.forward(27)
car3.lt(13)
car3.forward(13)
car3.forward(250)

print(car.mileage)
turtle.done()