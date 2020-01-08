import turtle
turtle.speed(1000)
for i in range(72000):
    angle = i / 100
    for j in range(int(angle * 1.5)):
        turtle.forward(j*2)
        turtle.right(angle)
    turtle.tracer(True)
    turtle.tracer(False)
    turtle.reset()
