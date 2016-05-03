%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt

def CharCount(word):
    d=dict()
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
    e=dict()
    e['alpha']=0
    e['digit']=0
    for c in word:
        if c.isalpha()==True:
            e['alpha']+=1
        elif c.isdigit()==True:
            e['digit']+=1    
    print e     
    
    
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
    
    
def lab9():
    CC()
    AD()
    
def main():
    lab9()
    
    
if __name__=="__main__":
    main()
