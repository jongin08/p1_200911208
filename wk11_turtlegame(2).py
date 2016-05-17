import turtle
import math

wn=turtle.Screen()

t1=turtle.Turtle()
t1.color("red")
t1.shape("turtle")

t2=turtle.Turtle()

t3=turtle.Turtle()

t4=turtle.Turtle()

coord=[(200,100),(300,200)]

line=[(200,-110),(300,-90)]

radius=50

circlePos=(-200,100)
#wn.bgpic("myMaze.gif")

def Rectangle():
    
    t2.home()
    t2.clear()
    t2.penup()
    t2.goto(200,200)
    t2.pendown()
    for i in range(0,4):
        t2.fd(100)
        t2.right(90)
        t2.write(t2.pos())
    t2.hideturtle()
        
def Circle():
    t3.penup()
    t3.goto(circlePos)
    t3.pendown()
    t3.circle(radius)
    t3.write(t1.pos())
    t3.hideturtle()

def Line():
    t4.penup()
    t4.goto(200,-100)
    t4.pendown()
    t4.fd(100)
    t4.hideturtle()
    
def turnright():
    t1.right(45)

def turnleft():
    t1.left(45)

def keyup():
    pt=t1.pos()
    t1.fd(50)
    if isInRectangle(pt, coord)or isInCircle(pt, radius, circlePos) or isOnLine(pt,line):
        t1.write("Good!")
    
def turnback():
    t1.right(180)
    
def mousegoto(x,y):
    t1.setpos(x,y)
    pt=t1.pos()
    if isInRectangle(pt, coord)or isInCircle(pt, radius, circlePos)or isOnLine(pt,line):
        t1.write("Good!")
    

def keybye():
    wn.bye()
    
    
    
def isInRectangle(curpos,coord):
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    if xs < xe and ys < ye:
        return xs <= curpos[0] <= xe and ys <= curpos[1] <= ye
    elif xs > xe and ys < ye:
        return xe <= curpos[0] <= xs and ye <= curpos[1] <= ys
    elif xs < xe and ys > ye:
        return xs <= curpos[0] <= xe and ys <= curpos[1] <= ys
    else:
        return xe <= curpos[0] <= xs and ys <= curpos[1] <= ye
    
def isInCircle(curpos, radius, pos):
    dist = math.sqrt(math.pow(curpos[0]-pos[0], 2) + math.pow(curpos[1]-pos[1], 2))
    if (dist<=radius):
        return True
    else:
        return False

def isOnLine(curpos,line):
    xs=line[0][0]
    xe=line[1][0]
    ys=line[0][1]
    ye=line[1][1]
    if xs < xe and ys < ye:
        return xs <= curpos[0] <= xe and ys <= curpos[1] <= ye
    elif xs > xe and ys < ye:
        return xe <= curpos[0] <= xs and ye <= curpos[1] <= ys
    elif xs < xe and ys > ye:
        return xs <= curpos[0] <= xe and ys <= curpos[1] <= ys
    else:
        return xe <= curpos[0] <= xs and ys <= curpos[1] <= ye
    
    
def addkeys():
    wn.onkey(turnright,"Right")
    wn.onkey(turnleft,"Left")
    wn.onkey(keyup,"Up")
    wn.onkey(turnback,"Down")
    wn.onkey(keybye,"q")

def addmouse():
    wn.onclick(mousegoto)
        



def lab11():
    Line()
    Rectangle()
    Circle()
    addkeys()
    addmouse()
    turtle.listen()
    turtle.mainloop()
    
def main():
     lab11()

if __name__=="__main__":
     main()
