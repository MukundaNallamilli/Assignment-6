from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
plt.style.use('seaborn')

x1=[]
x1.extend([0 for i in range(1,7)])
y1=[2,4,6,8,10,12]
plt.scatter(x1,y1,s=100,color='green',marker='^')

for i in range(1,6):
    x=[]
    x.extend([i for j in range(1,7-i)])
    y=[]
    for k in range(1,7-i):
        y.append(2*k+i)
    plt.scatter(x,y,s=100,color='green')

plt.title('Probability distribution')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
