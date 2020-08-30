import turtle
def draw_square(animal,size) :
    """
    make animal draw a square

    """
    for i in range(4) :
        animal.forward(size)
        animal.left(90)

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("DP")

dp = turtle.Turtle()
dp.pensize(5)
dp.color("hotpink")
draw_square(dp,50)
window.mainloop()

