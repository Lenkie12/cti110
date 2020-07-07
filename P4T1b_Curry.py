#To use the turtle to write my initials.
#CTI-110 - Initials
#06 July 2020
#Johnny Curry
#

#Call turtle
import turtle

#Show the turtle.
turtle.hideturtle()
turtle.speed(1)
turtle.pensize(5)
turtle.pencolor('purple')


#Draw first initial.
turtle.penup()
turtle.goto(-175, 50)
turtle.pendown()
turtle.forward(120)
turtle.penup()
turtle.backward(60)
turtle.right(90)
turtle.pendown()
turtle.forward(120)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(45)

#Draw last initial.
turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.right(90)
turtle.forward(120)
turtle.backward(120)
turtle.right(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(120)


