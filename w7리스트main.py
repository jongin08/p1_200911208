x=list()
def sumList(x):
    sum=0
    for i in range(1,1000):
        if(i%4==0 and i%5!=0):
            x.append(i)
            
    for i in range(0,len(x)):
        sum=sum+x[i]
    return sum

sumList(x)