import turtle
def make_window(color,title) :
    """ Making a window"""
    window = turtle.Screen()
    window.bgcolor(color)
    window.title(title)
    return window

def make_turtle(color,size) :
    dp = turtle.Turtle()
    dp.color(color)
    dp.pensize(size)
    return dp

def make_polygon(n,sz) :
    deg = 360/n
    for i in range(n) :
        dp.forward(sz)
        dp.left(deg)

wn = make_window("lightgreen","DP")
dp = make_turtle("red",2)
pl = make_polygon(8,50)

wn.mainloop()

