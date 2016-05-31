import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.home()
t1.clear()

def drawSquareWithCoords(coords):
    x1=int(coords[0][0])
    y1=int(coords[0][1])
    x2=int(coords[0][2])
    y2=int(coords[0][3])
    
    x3=int(coords[1][0])
    y3=int(coords[1][1])
    x4=int(coords[1][2])
    y4=int(coords[1][3])


    
    t1.goto(x1, y1)
    t1.goto(x1, y2)
    t1.goto(x2, y2)
    t1.goto(x2, y1)
    t1.goto(x1, y1)

    
    t1.penup()
    
    t1.goto(x3, y3)
    t1.pendown()
    t1.goto(x3, y4)
    t1.goto(x4, y4)
    t1.goto(x4, y3)
    t1.goto(x3, y3)
    
    t1.penup()
    t1.home()
    t1.pendown()
    wn.exitonclick()

def coords():
    fin=open('coords.txt.','r')
    
    coords=list()
    for line in fin:
        coords.append(line.split())
    
    return coords

def file():
    try:
        fin1=open('python.txt', 'a')
        fin2=open('outputNumber.txt', 'r')

        for line in fin2:
            fin1.write(line)

        fin1.close()
        fin2.close()

    except IOError as e:
        print e

def lab13():
    drawSquareWithCoords(coords())
    file()


def main():
    lab13()
    
if __name__=="__main__":
    main()