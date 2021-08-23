import turtle

turtle.speed('slowest')

def triangle(side_length, colour):
    angle = 120

    turtle.color(colour, colour)
    turtle.begin_fill()

    for side in range(3):
        turtle.forward(side_length)
        turtle.right(angle)

triangle(60, 'pink')
triangle(120, 'green')