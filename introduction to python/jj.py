# for making square
import turtle

# turtle setup 
pen = turtle.Turtle()
pen.speed(2)
pen.color("red")
pen.fillcolor("cyan")

pen.begin_fill()
# square drawing
for i in range(4):
    pen.forward(100)
    pen.right(90)

pen.end_fill()

turtle.done()
