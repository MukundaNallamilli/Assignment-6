from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
x1=[]
y1=[]
for x in range(1,7):
   x1.append(x)
   y1.append(2*x)

plt.style.use('seaborn')
plt.scatter(x1,y1,s=100,color='green')
plt.title('Probability distribution')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()