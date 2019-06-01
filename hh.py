import turtle

def draw_multicolor_square(t, sz):

    """Make turtle t draw a multi-color square of sz."""

    for i in ["red", "purple", "hotpink", "blue"]:

        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")
tess = turtle.Turtle()      # Create tess and set some attributes
tess.pensize(3)

size = 15                   # Size of the smallest square
for i in range(20):

    draw_multicolor_square(tess, size)
    size += 8        # Increase the size for next time
    tess.forward(20)        # Move tess along a little
    tess.right(36)          #    and give her some extra turn


wn.mainloop()
