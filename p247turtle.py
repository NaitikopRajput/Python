
import turtle

t=turtle.Turtle()
scr=turtle.Screen()
scr.bgcolor("SkyBlue1")
t.color("black","orange")
t.penup()
t.goto(-100,-150)
t.begin_fill()
t.pendown()
t.forward(200)
t.left(60)
t.forward(80)
t.setheading(180)
t.forward(280)
t.left(120)
t.forward(80)
t.end_fill()
t.backward(80)
t.setheading(0)
t.forward(140)
t.left(90)
t.pensize(8)
t.forward(125)
t.backward(5)
t.penup()
t.pensize(2)
t.pendown()
t.left(130)
t.forward(4)
t.color("white")
t.begin_fill()
t.forward(165)
t.setheading(0)
t.forward(125)
t.end_fill()
t.penup()
t.left(90)
t.forward(108)
t.right(90)
t.forward(7)
t.pensize(2)
t.pendown()
t.right(40)
t.color("white")
t.begin_fill()
t.forward(168)
t.setheading(180)
t.forward(125)
t.end_fill()
t.penup()
t.color("black","white")
t.goto(-70,-100)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.goto(-0,-100)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.goto(70,-100)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.goto(-800,-150)
t.setheading(0)
t.color("Blue","Blue")
t.pendown()
t.begin_fill()
t.forward(1500)
t.right(90)
t.forward(180)
t.right(90)
t.forward(1500)
t.end_fill()
turtle.done()
