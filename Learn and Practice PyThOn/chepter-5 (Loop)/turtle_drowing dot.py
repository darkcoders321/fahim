import turtle
height=5
width=5

turtle.speed(2)

turtle.penup()

for y in range(height):
         for x in range(width):
                  turtle.dot()
                  turtle.forward(5)
                  turtle.backward(5*width)
                  turtle.right(90)
                  turtle.forward(5)
                  turtle.left(90)
