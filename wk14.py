import turtle

class SquareTurtle(turtle.Turtle):
    def drawSquare(self,size):
        for i in range(0,4):
            self.fd(size)
            self.right(90)
            


class Ddog(object):
    def __init__(self,name):
        self.name=name
    def talk(self):
        print "mung mung"
        
class ShihTzuDog(Ddog):
    def talk(self):
        print "si si"

class MartDog(Ddog):
    def talk(self):
        print "mal mal"
        



def lab14():
    t1=SquareTurtle()
    t1.drawSquare(100)
    ADog=Ddog('d1')
    BDog=ShihTzuDog('d2')
    CDog=MartDog('d3')

    ADog.talk()
    BDog.talk()
    CDog.talk()    
        
        
def main():
    lab14()
    
if __name__=="__main__": 
     main()  