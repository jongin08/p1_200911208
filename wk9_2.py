%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt

word = 'hongji 2 gil 20,Jongrogu,Seoul'

z=dict()
z['alpha']=0
z['number']=0
for i in word:
    if i.isalpha():
            z['alpha']=z['alpha']+1
    elif i.isdigit:
            z['number']=z['number']+1
print z


plt.bar(range(len(z)),z.values(),align='center')
plt.xticks(range(len(z)),list(z.keys()))
plt.show()