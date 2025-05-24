import turtle
window = turtle.Screen()
t = turtle.Turtle()


def drawShape(length, num_sides):
    for i in range(num_sides):
        t.forward(length)
        t.left(360 / num_sides)

length_var =int(input("what is the length "))
drawShape(length_var, 4)

window.mainloop()