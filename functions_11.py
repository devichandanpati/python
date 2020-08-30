import turtle
def make_window(color,title) :
    """ Make a window"""
    window = turtle.Screen()
    window.bgcolor(color)
    window.title(title)
    return window
def make_turtle(color,size) :
    """ Make a turtle"""
    dp = turtle.Turtle()
    dp.color(color)
    dp.pensize(size)
    return dp
def make_design(length,degree) :
    """ Make a design"""
    dp.left(180)
    for x in range(40) :
        length = length + 5
        dp.left(5)
        for i in range(2) :
            dp.forward(length)
            dp.right(degree)

wn = make_window("lightgreen","DP")
dp = make_turtle("red",2)
des = make_design(10,90)

wn.mainloop()