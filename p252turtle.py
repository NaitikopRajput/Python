import turtle
from turtle import*


ans=int(input("Enter Number =>"))

if ans%2==0:
    screen = turtle.Screen()

    t = turtle.Turtle()
    speed(0)

    t.penup()
    t.goto(-400, 250)
    t.pendown()

    t.color("orange")
    t.begin_fill()
    t.forward(800)
    t.right(90)
    t.forward(167)
    t.right(90)
    t.forward(800)
    t.end_fill()
    t.left(90)
    t.forward(167)

    t.color("green")
    t.begin_fill()
    t.forward(167)
    t.left(90)
    t.forward(800)
    t.left(90)
    t.forward(167)
    t.end_fill()

    t.penup()
    t.goto(70, 0)
    t.pendown()
    t.color("navy")
    t.begin_fill()
    t.circle(70)
    t.end_fill()

    t.penup()
    t.goto(60, 0)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(60)
    t.end_fill()

    t.penup()
    t.goto(-57, -8)
    t.pendown()
    t.color("navy")
    for i in range(24):
        t.begin_fill()
        t.circle(3)
        t.end_fill()
        t.penup()
        t.forward(15)
        t.right(15)
        t.pendown()
        
    t.penup()
    t.goto(20, 0)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.pensize(2)
    for i in range(24):
        t.forward(60)
        t.backward(60)
        t.left(15)
        
    turtle.done()
else:
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

