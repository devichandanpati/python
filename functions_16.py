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
    for x in range(5) :
        for i in range(5) :
            dp.forward(length)
            dp.right(degree)
        dp.penup()
        dp.forward(350)
        dp.right(144)
        dp.pendown()

wn = make_window("lightgreen","DP")
dp = make_turtle("red",2)
des = make_design(100,144)

wn.mainloop()


