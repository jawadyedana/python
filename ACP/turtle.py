import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("light gray")

# Draw equilateral triangle
triangle = turtle.Turtle()
triangle.color("blue", "yellow")
triangle.begin_fill()
for _ in range(3):
    triangle.forward(100)
    triangle.left(120)
triangle.end_fill()

# Move to draw rectangle
triangle.penup()
triangle.goto(150, 0)
triangle.pendown()

# Draw rectangle
rectangle = turtle.Turtle()
rectangle.color("red", "pink")
rectangle.begin_fill()
for _ in range(2):
    rectangle.forward(150)
    rectangle.left(90)
    rectangle.forward(80)
    rectangle.left(90)
rectangle.end_fill()

# Move to draw hexagon
rectangle.penup()
rectangle.goto(-150, 0)
rectangle.pendown()

# Draw hexagon
hexagon = turtle.Turtle()
hexagon.color("green", "light green")
hexagon.begin_fill()
for _ in range(6):
    hexagon.forward(80)
    hexagon.left(60)
hexagon.end_fill()

turtle.done()
