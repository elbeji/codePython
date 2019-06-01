
#drapeau tunisien
import turtle
x=540
y=360
turtle.setup(x,y)
turtle.bgcolor("red")
turtle.penup()
#def whitecircle(posx,posy,radius, color1):
turtle.goto(0,-90)
turtle.pen()
turtle.pencolor('white')
turtle.pendown()
turtle.begin_fill()
turtle.circle(90, None, None)
turtle.color('white')
turtle.end_fill()
#turtle.done()
#def redcircle(posx,posy,radius, color2):
turtle.penup()
turtle.goto(0,-60)
turtle.pen()
turtle.pencolor('red')
turtle.pendown()
turtle.begin_fill()
turtle.circle(60, None, None)
turtle.color('red')
turtle.end_fill()
#turtle.done()

turtle.penup()
turtle.goto(18,-54)
turtle.pen()
turtle.pencolor('white')
turtle.pendown()
turtle.begin_fill()
turtle.circle(54, None, None)
turtle.color('white')
turtle.end_fill()
#turtle.done()

#star
turtle.penup()
turtle.goto(30,15)
turtle.pen()
turtle.pencolor('red')
turtle.pendown()
turtle.begin_fill()
turtle.left(18)

turtle.forward(25)
turtle.right(144)
turtle.forward(25)
turtle.left(72)

turtle.forward(25)
turtle.right(144)
turtle.forward(25)
turtle.left(72)

turtle.forward(25)
turtle.right(144)
turtle.forward(25)
turtle.left(72)

turtle.forward(25)
turtle.right(144)
turtle.forward(25)
turtle.left(72)

turtle.forward(25)
turtle.right(144)
turtle.forward(25)
turtle.left(72)

turtle.color('red')
turtle.end_fill()
