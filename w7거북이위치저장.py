import turtle
wn=turtle.Screen()
#wn.bgpic("myMaze.gif")
t1=turtle.Turtle()
mytracks=list()
def saveTracks():
    t1.speed(3)
    t1.penup()
    #list 사용이유 - 순서가있고 늘어남
    tracks=list()
    t1.goto(-400,300)
    tracks.append(t1.pos())
    t1.pendown()
    t1.pencolor("Red")
    t1.right(90)
    t1.fd(400)
    tracks.append(t1.pos())
    t1.backward(150)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(150)
    tracks.append(t1.pos())
    t1.right(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90)
    t1.right(90)
    t1.right(90)
    t1.fd(200)
    tracks.append(t1.pos())
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(100)
    t1.left(90)
    t1.fd(200)
    tracks.append(t1.pos())
    return tracks

def replayTracks(tracks):
    for i in range (0,len(tracks)):
        t1.setpos(tracks[i])
        

def lab7():


    mytracks=saveTracks()
    replyTracks(tracks)

def main():
    
    lab7()
    
if __name__=="__main__":
    main()