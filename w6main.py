"""
@author j.Kim
@since 160406
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
        print "윤년"
    else:
        print "윤년아님"
        

def lab6():
    m35()
    a()
    
def main():
    lab6()
    
if __name__=="__main__":
    main()
    
