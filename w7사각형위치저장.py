def drawSquareAt(size,pos):
    t1.home()
    t1.clear()
    tracks=list()
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    for i in range(0,4):
        t1.fd(size)
        t1.right(90)
        tracks.append(t1.pos())
    return tracks

def lab7():
   drawSquareAt(100,(0,0))

def main():
   lab7()

if __name__=="__main__":
    main()