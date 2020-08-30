import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("DP")
dp = turtle.Turtle()
dp.color("red")
dp.pensize(5)

# A polygon with 18 sides
for _ in range(18) :
    dp.forward(50)
    dp.left(20)

dp.penup()
dp.forward(100)
dp.pendown()

# An asterisk
for i in range(5) :
    dp.forward(100)
    dp.left(144)

window.mainloop()
