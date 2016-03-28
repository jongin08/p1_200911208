import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def MakeSwirlSquare(size):
    sides=30
    bigger=10
    angle=90

    t1.home()
    t1.clear()

    for i in range(0,sides):
        if(i%3):
            size=size+bigger
            t1.fd(size)
            t1.right(angle)

MakeSwirlSquare(10)


wn.exitonclick()