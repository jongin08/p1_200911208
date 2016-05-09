%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt

def population():
    pop = [[74425, 76326], [61164, 61636], [109688, 115744],
        [144796, 146776], [174996, 181676], [177841, 177434],
        [204630, 205980], [223373, 232245], [161055, 166130],
        [171576, 176735], [279169, 293772], [239450, 251066],
        [148690, 156510], [182977, 196992], [237792, 242641],
        [283869, 296762], [209344, 210282], [118965, 114441],
        [186503, 186856], [195734, 203014], [254381, 249472],
        [212401, 229111], [271654, 295354], [319197, 335045],
        [229829, 231671]]
    return pop

def calPop(pop):
    mSum=0
    fSum=0
    for i in range(0, len(pop)):
        mSum=mSum+pop[i][0]
        fSum=fSum+pop[i][1]
        
    mAvg=float(mSum)/float(len(pop))
    fAvg=float(fSum)/float(len(pop))
    
    
    print "Sum(male) : ", mSum ," and Sum(female) : ", fSum
    print "Avg(male) : ", mAvg ," and Avg(female) : ", fAvg

def graph(pop):
    
    d=dict()
    for i in range(0, len(pop)):
        d[i]=pop[i][0]+pop[i][1]
    
    plt.bar(range(len(d)), d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()
    
def lab10():
    pop=population()
    calPop(pop)
    graph(pop)
    
def main():
    lab10()
    
    
if __name__=="__main__":
    main()
