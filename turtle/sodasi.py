import turtle



screen = turtle.Screen()
screen.bgcolor('black')
screen.title('hello world')


t = turtle.Turtle()
t.pensize(10)
t.color('green')

# ===================================
for _ in range(4):
    t.backward(100)
    t.left(120)
    t.forward(100)
    t.left(120)




turtle.done()