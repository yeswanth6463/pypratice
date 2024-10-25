import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
avenger = turtle.Turtle()
avenger.speed(2)

# Draw the outer circle
avenger.penup()
avenger.goto(0, -150)
avenger.pendown()
avenger.circle(150)

# Draw the 'A' symbol
avenger.penup()
avenger.goto(-60, 60)
avenger.pendown()
avenger.left(75)
avenger.forward(120)
avenger.right(150)
avenger.forward(50)
avenger.right(105)
avenger.forward(65)
avenger.right(75)
avenger.forward(100)
avenger.penup()
avenger.goto(-35, 15)
avenger.pendown()
avenger.left(180)
avenger.forward(80)

# Draw the arrow
avenger.penup()
avenger.goto(5, 70)
avenger.pendown()
avenger.right(60)
avenger.forward(50)
avenger.right(120)
avenger.forward(25)
avenger.right(180)
avenger.forward(25)
avenger.left(120)
avenger.forward(50)

# Hide the turtle and display the window
avenger.hideturtle()
turtle.done()
