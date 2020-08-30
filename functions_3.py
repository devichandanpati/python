import turtle
def draw_rectangle(animal,length,breadth) :
    """ Drawing a rectangle"""
    for i in range(2) :
        animal.forward(length)
        animal.left(90)
        animal.forward(breadth)
        animal.left(90)

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("DP")

dp = turtle.Turtle()
dp.color("red")
dp.pensize(3)

x = int(input("length of rectangle"))
y = int(input("breadth of rectangle"))

draw_rectangle(dp,x,y)

window.mainloop()

