from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
x1=[]
plt.style.use('seaborn')
for x in range(1,7):
   x1.append(x)
for y in range(1,7):
    y1=[]
    y1.extend([y for i in range(1,7)])
    plt.scatter(x1,y1,s=100,color='green')

plt.title('Probability distribution')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()