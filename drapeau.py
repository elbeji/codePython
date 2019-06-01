import turtle
x=800
y=800
turtle.setup(x,y)
turtle.bgcolor('red')
#cercle blanc
turtle.penup()
turtle.goto(0,-90)
turtle.pencolor('white')
turtle.pendown()
turtle.begin_fill()
turtle.circle(90,None,None)
turtle.color('white')
turtle.end_fill()

#cercle rouge
turtle.penup()
turtle.goto(0,-60)
turtle.pen()
turtle.pencolor('red')
turtle.pendown()
turtle.begin_fill()
turtle.circle(60,None,None)
turtle.color('red')
turtle.end_fill()


#etoile
turtle.penup()
turtle.goto(38,15)
turtle.pen()
turtle.pencolor('white')
turtle.pendown()
turtle.begin_fill()
turtle.left(18)

for i in range(5):
    turtle.forward(25)
    turtle.right(144)

turtle.forward(25)
turtle.left(72)
turtle.color('red')
turtle.end_fill()


