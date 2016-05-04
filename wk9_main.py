%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt
d=dict()
e=dict()

def CharCount(word):    
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    print d
    
def CCgraph(word):
    
    plt.bar(range(len(d)),d.values(),align='center')
    plt.xticks(range(len(d)),list(d.keys()))
    plt.show()
    
def AlphaDigit(word):
    e['alpha']=0
    e['digit']=0
    for c in word:
        if c.isalpha()==True:
            e['alpha']+=1
        elif c.isdigit()==True:
            e['digit']+=1    
    print e     
    
    
def ADgraph(word):
    plt.bar(range(len(e)), e.values(), align='center')
    plt.xticks(range(len(e)), list(e.keys()))
    plt.show()
    

    
    
def CC():
    word='sangmyung university'
    CharCount(word)
    CCgraph(word)
    
def AD():
    word="7 hongi,Jongro"
    AlphaDigit(word)
    ADgraph(word)
  

   
def friend_and_I():
    i=set(['TV', 'phone', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'])
    f=set(['coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'])
    
    print "  "
    print "===1st==="
    print i.union(f)
    print "========="
    print "===2nd==="
    print i-f
    print "========="
    print "===3rd==="
    print f-i
    print "========="
    print "===4th==="
    print i.intersection(f)
    print "========="

    ee=dict()
    for c in i.union(f):
        if c not in i&f:
            ee[c]=1
        else:
            ee[c]=2
            
    print "===5th==="
    print ee
    print "========="
    
    
def lab9():
    CC()
    AD()
    friend_and_I()
    
def main():
    lab9()
    
    
if __name__=="__main__":
    main()
