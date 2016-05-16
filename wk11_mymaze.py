import turtle
import math
wn=turtle.Screen()
t1=turtle.Turtle()
t1.color("red")
t1.shape("turtle")
t1.penup()
wn.bgpic("myMaze.gif")
t1.goto(-350,370)
t1.pendown()
#End line : t1.goto(430,-250)

    
    
def turnright():
    t1.right(45)

def turnleft():
    t1.left(45)

def keyup():
    t1.fd(100)
    
def turnback():
    t1.right(180)
    
def mousegoto(x,y):
    t1.setpos(x,y)
    feedback()
    

def keybye():
    wn.bye()


def addkeys():
    wn.onkey(turnright,"Right")
    wn.onkey(turnleft,"Left")
    wn.onkey(keyup,"Up")
    wn.onkey(turnback,"Down")
    wn.onkey(keybye,"q")

def addmouse():
    wn.onclick(mousegoto)

    
def feedback():
    if t1.xcor() > 410 or t1.xcor() < 440:
        t1.write("Good")

    if t1.ycor() > 260 or t1.ycor() < -300:
        t1.write("Good")

def lab11():

    addkeys()
    addmouse()
    turtle.listen()
    turtle.mainloop()
    
def main():
     lab11()

if __name__=="__main__":
     main()