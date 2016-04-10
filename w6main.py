"""
@author j.Kim
@since 160406
"""

import random
"""
This is for Up and down game at wk6
"""

def m35():
    result = 0
    for i in range(1,1000):
        if i%3 == 0 or i%5==0:
            result +=i
    return result


def a():
    year = float(input("year:"))
    if(year%4==0)and(year%100!=0 or year%400==0):
        print "Good! It is a leap year."
    else:
        print "It is not a leap year."

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
        

def lab6():
    print m35()
    a()
    UpAndDown()
    
def main():
    lab6()
    
if __name__=="__main__":
    main()
    
