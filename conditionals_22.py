#Create a square, equilateral triangle,hexagon,octagon
import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("DP")
dp = turtle.Turtle()
dp.color("hotpink")
dp.pensize(5)

#Square
for i in range(4) :
    dp.forward(50)
    dp.right(90)

dp.penup()
dp.forward(90)
dp.pendown()

#Triangle
for i in range(3) :
    dp.forward(40)
    dp.right(120)

dp.penup()
dp.forward(90)
dp.pendown()

#Hexagon
for i in range(6) :
    dp.forward(50)
    dp.left(60)

dp.penup()
dp.forward(120)
dp.pendown()

#Octagon
for i in range(8) :
    dp.forward(50)
    dp.left(45)

window.mainloop()

