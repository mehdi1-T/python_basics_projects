import turtle 

screen = turtle.Screen()
screen.bgcolor('#800080')
screen.title('DOUAA')
screen.setup(height=1.0, width=1.0)

t = turtle.Turtle()
t.color("white")
t.pensize(50)
t.speed(100)


def draw_d(t):
    t.penup()
    t.goto(-500, 150)
    t.pendown()
    t.right(90)
    t.forward(300)
    t.left(90)
    t.circle(150, 180)
    t.penup()

def draw_o(t):
    t.penup()
    t.goto(-300, -150)
    t.pendown()
    t.circle(150)

def draw_u(t):
    t.backward(250)
    t.left(90)
    t.pendown()
    t.forward(230)
    t.circle(100, 180)
    t.forward(230)

def draw_a(t):
    t.penup()
    t.goto(10, -150) 
    t.pendown()
    t.right(15)
    t.forward(300) 
    t.right(150)
    t.forward(300) 
    t.left(75) 
    t.penup()
    t.forward(25)
    t.pendown()
    t.left(75)
    t.penup()
    t.pendown()
    t.forward(300) 
    t.right(150)
    t.forward(300)  

    
draw_o(t)
draw_d(t)
draw_u(t)
draw_a(t)

turtle.done() 