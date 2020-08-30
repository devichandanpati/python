import turtle
angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]
window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("DP")
dp = turtle.Turtle()
dp.color("hotpink")
dp.pensize(5)

for a in angles :
    if a < 0 :
        dp.left(-a)
        dp.forward(100)
    if a > 0 :
        dp.left(a)
        dp.forward(100)

window.mainloop()

