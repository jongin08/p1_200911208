#거북이게임
import turtle
import math
import random


wn=turtle.Screen()
wn.bgcolor("lightgreen")

#프레임을 낮춰서 게임을 부드럽게 함
wn.tracer(3)



#사각형 게임공간을 만듬 
stadium = turtle.Turtle()
stadium.penup()
stadium.setposition(-300,-300)
stadium.pendown()
stadium.pensize(3)
for side in range(4):
    stadium.forward(600)
    stadium.left(90)
stadium.hideturtle()


#플레이를 할 거북이를 만듬
player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.shapesize(2,2)
player.penup()
player.speed(0)

#점수
score = 0

#거북이 먹이(포인트)를 만들어 리스트에 넣음
maxPoints = 10
points = []


#획득할 먹이의 모양과 나타날 위치를 랜덤으로 지정
for count in range(maxPoints):
    points.append(turtle.Turtle())
    points[count].color("red")
    points[count].shape("circle")
    points[count].penup()
    points[count].speed(0)
    points[count].setposition(random.randint(-300,300), random.randint(-300,300 ))
    

#기본 속도 지정
speed = 1

#마우스입력으로부터 거북이를 움직이게 할 함수들을 지정

def turnleft():
    player.left(30)    
    
def turnright():
    player.right(30)    
    
def increasespeed():
    global speed
    speed +=1

def isCollision(t1,t2): 
    #math를 이용해 거북이가 포인트를 먹었을 때의 변화를 설정하는 함수
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) +
                  math.pow(t1.ycor()-t2.ycor(),2))
    if d <20:
        return True
    else:
        return False

    
#키보드 입력으로 거북이를 움직임
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")



while True:
    player.forward(speed)
    
    #거북이(player)가 벽에 부딪히면 뒤를 돌아보게 설정
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
            
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
     
    

    #거북이 먹이를 움직이게 만듬
    for count in range(maxPoints):
        points[count].forward(3)

        #먹이도 벽에 부딪히면 뒤를 돌아봄
        if points[count].xcor() > 290 or points[count].xcor() < -290:
            points[count].right(180)

        if points[count].ycor() > 290 or points[count].ycor() < -290:
            points[count].right(180)
            
        #거북이가 먹이를 먹었을 때 다시 나타날 장소를 랜덤으로 지정    
        if isCollision(player,points[count]):
            points[count].setposition(random.randint(-300,300), random.randint(-300,300 ))
            points[count].right(random.randint(0,360))
            score += 1
            #좌측 상단에 점수를 기록
            stadium.undo()
            stadium.penup()
            stadium.hideturtle()
            stadium.setposition(-290,310)
            scorestring = "Score: %s" %score
            stadium.write(scorestring, False, align = "left", font =("Arial",14,"normal"))
            


        
    
delay = raw_input("Press Enter to finish.")

    