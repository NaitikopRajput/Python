import turtle

t1=turtle.Turtle()
turtle.bgcolor("black")
t1.pensize(2)
t1.speed(0)

for i in range(6):
    for colors in ["red","magenta","blue","cyan","green","yellow","white"]:
        t1.color(colors)
        t1.circle(100)
        t1.left(10)

turtle.done()
