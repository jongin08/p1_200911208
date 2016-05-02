%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt

def charCount():
    word=raw_input("")

    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    print d
    

def graph(charCount):

    plt.bar(range(len(d)),d.values(),align='center')
    plt.xticks(range(len(d)),list(d.keys()))
    plt.show()
    
    
def lab9():
    d=dict()
    charCount()
    graph(charCount)
def main():
    lab9()
    
if __name__=="__main__":
    main()