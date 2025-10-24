import turtle


screen = turtle.Screen()
screen.bgcolor('black')

t = turtle.Turtle()
t.speed(0)
t.color('cyan')

for i in range(100):
    t.forward(5 * i)
    t.right(144)


turtle.done()