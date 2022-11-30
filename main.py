import turtle
bob=turtle.Turtle()
bob.speed(10)
#drawing a quadrilateral
#forward direction
#bob.forward(100)
#left direction
#bob.left(45)
#bob.forward((100))
#right direction
#bob.right(90)
#bob.forward(100)
#bob.forward(100)
#bob.right(90)
#bob.forward(100)
#bob.forward(100)
#bob.right(110)
#bob.forward(100)
#bob.forward(100)
#bob.forward(100)
#drawing a square
#bob.forward(100)
#bob.left(90)
#bob.forward(100)
#bob.left(90)
#bob.forward(100)
#bob.left(90)
#bob.forward(100)
bob.color("red","yellow")
bob.begin_fill()
for i in range(100):
    bob.forward(200)
    bob.left(168.3)

    bob.end_fill()
turtle.done()