import turtle
def make_window(color,title) :
    """ Making Window"""
    window = turtle.Screen()
    window.bgcolor(color)
    window.title(title)
    return window

def make_turtle(color,size) :
    "Making a turtle"
    animal = turtle.Turtle()
    animal.color(color)
    animal.pensize(size)
    return animal

def make_square(length,degree) :
    """Making a square"""
    for x in range(5) :
        for a in range(4) :
            dp.forward(length)
            dp.left(degree)

        dp.penup()
        dp.forward(40)
        dp.pendown()

wn = make_window("lightgreen","DP")
dp = make_turtle("red",2)
sq = make_square(20,90)

wn.mainloop()

