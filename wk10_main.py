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
    
    
def coffeepot():
    
    coffee=[["Coffee","Water","Milk","Icecream"],
            ["Espresso","No","No","No"],
            ["Long Black","Yes","No","No"],
            ["Flat White","No","Yes","No"],
            ["Cappuccino","No","Yes","No"],
            ["Affogato","No","No","Yes"]]

    ingredient=coffee[1:6]
    
    milk=0
    for i in range(0, len(ingredient)):
        if (ingredient[i][2]=="Yes"):
            milk+=1
            print ingredient[i][0]
    
    print "milk =",float(milk)/len(ingredient)*100,"%"
    

def calGrade():
    Class=[["English", "Math"],
           [100, 200], 
           [200, 200], 
           [100, 300]]
    
    score=Class[1:4]
    eSum=0
    mSum=0
    
    for i in range(0, len(score)):
        eSum=eSum+score[i][0]
        mSum=mSum+score[i][1]
        
    eAvg=eSum/len(score)
    mAvg=mSum/len(score)
    
    print "English :  Sum is",eSum,", and average is", eAvg
    print "M a t h :  Sum is",mSum,", and average is", mAvg



def max3word():
    lyrics= [" When I find myself in times of trouble",
            " Mother Mary comes to me",
            " Speaking words of wisdom, let it be",
            " And in my hour of darkness",
            " She is standing right in front of me",
            " Speaking words of wisdom, let it be",

            " Let it be, let it be",
            " Let it be, let it be",
            " Whisper words of wisdom, let it be",

            " And when the broken-hearted people",
            " Living in the world agree",
            " There will be an answer, let it be",
            " For though they may be parted",
            " There is still a chance that they will see",
            " There will be an answer, let it be",

            " Let it be, let it be",
            " Let it be, let it be",
            " Yeah, there will be an answer, let it be",
            " Let it be, let it be",
            " Let it be, let it be",
            " Whisper words of wisdom, let it be",

            " Let it be, let it be",
            " Ah, let it be, yeah, let it be",
            " Whisper words of wisdom, let it be",

            " And when the night is cloudy",
            " There is still a light that shines on me",
            " Shine on until tomorrow, let it be",
            " I wake up to the sound of music,",
            " Mother Mary comes to me",
            " Speaking words of wisdom, let it be",

            " Let it be, let it be",
            " Let it be, yeah, let it be",
            " Oh, there will be an answer, let it be",
            " Let it be, let it be",
            " Let it be, yeah, let it be",
            " Whisper words of wisdom, let it be"]
    
    
    word=[]
    
    for i in range(0, len(lyrics)):
        for j in range(0, len(lyrics[i].split())):
            word.append(lyrics[i].split()[j])
    
    
    d={}
    
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
            
    for h in d:
        if(d[h]>=20):
            print h, d[h]
            
            
def lab10():
    pop=population()
    calPop(pop)
    graph(pop)
    coffeepot()
    calGrade()
    max3word()

    
def main():
    lab10()
    
    
if __name__=="__main__":
    main()
