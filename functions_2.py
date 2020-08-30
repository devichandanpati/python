import turtle

def draw_square(animal,size) :
    """
    Make animal draw a multi color square of given size
    """

    for color in ["red","blue","hotpink","hotpink"] :
        animal.color(color)
        animal.forward(size)
        animal.left(90)

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("DP")

dp = turtle.Turtle()
dp.pensize(5)
size = 20
for i in range(15) :
    draw_square(dp,size)
    size = size + 10
    dp.forward(size)
    dp.right(18)

window.mainloop()


