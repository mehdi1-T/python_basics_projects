import turtle 



screen = turtle.Screen()
screen.bgcolor('black')

t = turtle.Turtle()
t.color('yellow')
t.pensize(12)
t.speed(2)

# #############################

for _ in range(4):
    t.forward(100)
    t.right(90)


# #############################

turtle.done