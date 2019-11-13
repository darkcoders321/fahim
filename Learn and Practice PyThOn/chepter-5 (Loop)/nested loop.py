import turtle
turtle.shape("turtle")
turtle.speed(8)

for side_length in range(1,1000,5):
         for i in range(4):
                  turtle.forward(side_length)
                  turtle.left(90)
