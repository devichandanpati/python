import turtle
def make_window(color,title) :
    window = turtle.Screen()
    window.bgcolor(color)
    window.title(title)
    return window
def make_turtle(color,size) :
    dp = turtle.Turtle()
    dp.color(color)
    dp.pensize(size)
    return dp
def make_design(length,degree) :
    for x in range(20) :
        for i in range(4) :
            dp.forward(length)
            dp.left(degree)
        dp.right(18)

wn = make_window("lightgreen","DP")
dp = make_turtle("red",2)
ds = make_design(100,90)

wn.mainloop()
