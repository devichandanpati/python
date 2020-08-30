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
    for i in range(3) :
        dp.forward(length)
        dp.left(degree)

wn = make_window("lightgreen","DP")
dp = make_turtle("red",2)
des = make_design(50,120)

wn.mainloop()
