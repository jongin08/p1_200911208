import turtle
import math
wn=turtle.Screen()

t1=turtle.Turtle()
t1.color("red")
t1.shape("turtle")
t1.penup()


def ring():

    ring = turtle.Turtle()
    ring.penup()
    ring.setpos(-300,300)
    ring.pendown()
    ring.pensize(3)

    #-300,300  ->  300,300  ->  300,-300  ->  -300,-300
    for side in range(4):
        ring.fd(600)
        ring.right(90)
        ring.write(ring.pos())
    ring.hideturtle()

    
    
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
    if t1.xcor() > 300 or t1.xcor() < -300:
        t1.right(180)
        t1.write("On the line")

    if t1.ycor() > 300 or t1.ycor() < -300:
        t1.right(180)
        t1.write("On the line")

def schoolLife():
    survey = [["highly satisfactoty", "satisfaction", "dissatisfaction" ,"highly unsatisfactory"],
                [13.1, 37.1, 8.7, 1.5],
                [10.6, 34.6, 13.4, 1.9],
                [27.1, 40.0, 2.9, 1.5],
                [16.2, 37.8, 6.8, 0.8],
                [11.4, 29.8, 14.8, 4.9],
                [12.2, 26.5, 14.9, 4.4],
                [13.5, 29.7, 11.1, 2.4],
                [13.7, 37.6, 4.1, 1.2]]
    grade=survey[1:8]
    sSum=0
    dsSum=0
    
    for i in range(len(grade)):
        sSum = sSum + grade[i][0] + grade[i][1]
        dsSum = dsSum + grade[i][2] + grade[i][3]
        
    sAvg=sSum/len(grade)
    dsAvg=dsSum/len(grade)
    
    print "Average of (highly) Satisfaction:", sAvg
    print "Average of (highly) unsatisfactory :", dsAvg

    
    
    
def lab11():

    ring()   
    addkeys()
    addmouse()
    turtle.listen()
    turtle.mainloop()
    schoolLife()
    

def main():
     lab11()

if __name__=="__main__":
     main()