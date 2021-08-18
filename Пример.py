import datetime
import turtle

turtle.tracer(False)
pen = turtle.Turtle()
pen.hideturtle()
pen.goto(0, 100)

t = datetime.datetime.today()
pen.write('Сегодня:', align="center", font=("Arial", 14, "bold"))
pen.forward(65)
pen.goto(0, 70)
pen.write(t, align="center", font=("Arial", 14, "normal"))
pen.goto(0, 50)
p = turtle.textinput("Name", "Введите Ваше имя: ")
turtle.write(p, False, align="left", font=("Arial", 16, "bold"))


def get_user_birthday():
    year = int(turtle.numinput('Вводим дату рождения', 'Введите год'))
    month = int(turtle.numinput('Вводим дату рождения', 'Введите месяц'))
    day = int(turtle.numinput('Вводим дату рождения', 'Введите день'))

    birthday = datetime.datetime(year, month, day)
    return birthday


def calc(original_date, now):
    delta1 = datetime.datetime(now.year, original_date.month, original_date.day)
    delta2 = datetime.datetime(now.year + 1, original_date.month, original_date.day)

    return ((delta1 if delta1 > now else delta2) - now).days


bd = get_user_birthday()
now = datetime.datetime.now()
c = calc(bd, now)
pen.goto(0, -30)
pen.write('До Вашего дня рождения осталось дней: ', align="center", font=("Arial", 14, "normal"))
pen.goto(0, -60)
pen.write(c, align="center", font=("Arial", 16, "bold"))

#f"{t.hour}:{minute}:{t.second}"

#turtle.write(arg, move=False, align="left", font=("Arial", 8, "normal"))


turtle.done()

