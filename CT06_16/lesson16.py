import turtle
window = turtle.Screen()
t = turtle.Turtle()


def drawShape(length, num_sides):
    for i in range(num_sides):
        t.forward(length)

length_var =int(input("what is the length "))


window.mainloop()