def drawSquareAt(size,pos):
    t1.home()
    t1.clear()
    x1=list()
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    for i in range(0,4):
        t1.fd(size)
        t1.right(90)
        x1.append(t1.pos())
    return x1

def lab5():
   drawSquareAt(100,(0,0))

def main():
   lab5()

if __name__=="__main__":
    main()