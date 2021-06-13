import turtle

player = turtle.Turtle()
size = 100

player.fd(size)
player.lt(90)
player.fd(size/10)
player.lt(90)
player.fd(size)
player.lt(90)
player.fd(size/10)
player.lt(180)
player.fd(size/10)

player.rt(76)
player.fd(size/2.425)

player.lt(90)
player.fd(size/1.5)

player.rt(76)
player.fd(size/2)


#iterbishop = 6

#for i in range(iterbishop+1):
    #player.fd(size/12)
    #player.lt(8)

#player.fd(size/20)

#player.fd(size/20)
#for i in range(iterbishop+1):
    #player.fd(size/12)
    #player.lt(8)


player.hideturtle()

turtle.done()
