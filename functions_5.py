import turtle
def make_window(color,title) :
    """ Making window"""
    window = turtle.Screen()
    window.bgcolor(color)
    window.title(title)
    return window

def make_turtle(color,size) :
    """ Making turtle"""
    animal = turtle.Turtle()
    animal.color(color)
    animal.pensize(size)
    return animal

def make_square(length,degree) :
    """Making square"""
    for a in range(4) :
        dp.forward(length)
        dp.left(degree)


wn = make_window("lightgreen","DP")
dp = make_turtle("hotpink",5)
sq = make_square(50,90)

wn.mainloop()
