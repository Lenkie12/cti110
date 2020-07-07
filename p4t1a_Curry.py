#To use "Turtle" to draw Repeating Squares.
#03 July 2020
#CTI-110 P4T1a - Turtle Graphic:Shapes
#Johnny Curry
#

#Show the turtle.
import turtle
turtle.hideturtle()
turtle.speed(10)

turtle.setup(width=500, height=500)


#Place starting mark.
turtle.penup()
turtle.backward(250)
turtle.right(90)
turtle.forward(250)
turtle.left(90)
turtle.pendown()

def square_draw(squares):
    for i in range(4):
        turtle.forward(squares)
        turtle.left(90)

squares = 10

for i in range(100):
    square_draw(squares)
    squares = squares + 5
    
turtle.exitonclick()
