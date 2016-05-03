%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt
d=dict()

def charCount(word):

    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    print d
    

def graph():

    plt.bar(range(len(d)),d.values(),align='center')
    plt.xticks(range(len(d)),list(d.keys()))
    plt.show()
    
    
def lab9():
    word='sangmyung university'
    charCount(word)
    graph()
def main():
    lab9()
    
if __name__=="__main__":
    main()
