import turtle
def make_window(color,title) :
    """ Making a window"""
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

def make_square(size,degree) :
    """Making a square"""
    for x in range(5) :
        for i in range(4) :
            dp.forward(size)
            dp.left(degree)
        dp.penup()
        dp.forward(size)
        size = size +20
        dp.right(45)
        dp.forward(14)
        dp.left(135)
        dp.forward(size)
        dp.left(90)
        dp.forward(size)
        dp.left(90)
        dp.forward(size)
        dp.left(90)
        dp.pendown()

wn = make_window("lightgreen","DP")
dp = make_turtle("red",2)
sq = make_square(20,90)

wn.mainloop()

