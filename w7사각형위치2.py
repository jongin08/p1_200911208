import turtle
wn = turtle.Screen()
t1= turtle.Turtle()

def drawSquareForm(tracks):   
    t1.home()
    for i in range(0,4):
        t1.setpos(tracks[i])
 
tracks=list()
tracks.append((90.00,0.00))
tracks.append((90.00,-90.00))
tracks.append((00.00,-90.00))
tracks.append((00.00,0.00))
drawSquareForm(tracks)