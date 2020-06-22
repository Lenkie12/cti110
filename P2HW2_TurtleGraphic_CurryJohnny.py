#To use "Turtle" to draw shapes.
#22 June 2020
#CTI-110 P2HW2 - Turtle Graphic
#Johnny Curry
#

#Call the turtle
import turtle

#Show the turtle
turtle.showturtle()
turtle.pensize(10)

#Draw blue circle
turtle.pencolor('blue')
turtle.penup()
turtle.goto(-175, 50)
turtle.pendown()
turtle.circle(75)

#Draw yellow circle
turtle.pencolor('yellow')
turtle.penup()
turtle.goto(-85, -40)
turtle.pendown()
turtle.circle(75)

#Draw black circle
turtle.pencolor('black')
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.circle(75)

#Draw green circle
turtle.pencolor('green')
turtle.penup()
turtle.goto(85, -40)
turtle.pendown()
turtle.circle(75)

#Draw red circle
turtle.pencolor('red')
turtle.penup()
turtle.goto(175, 50)
turtle.pendown()
turtle.circle(75)
