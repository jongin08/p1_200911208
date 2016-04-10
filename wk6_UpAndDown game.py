import random

def UpAndDown():
    num1=random.randrange(0,100)
    for i in range(0,20):
        num2=int(input("Try and guess a number between 1~100 : "))
        if num1<num2:
            print "Down"
        elif num1>num2:
            print "Up"
        elif num1==num2:
            print "You are right!"
            break
        
UpAndDown()