'''
Check the trend of investments over the years. To check the trend, find -
Total number of fundings done in each year.
Plot a line graph between year and number of fundings. Take year on x-axis and number of fundings on y-axis.
Print year-wise total number of fundings also. Print years in ascending order.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("startup_funding.csv")
df.replace('12/05.2015',"12/05/2015",inplace=True)
df.replace('12/05.2015',"12/05/2015",inplace=True)
df.replace('13/04.2015',"13/04/2015",inplace=True)
df.replace('15/01.2015',"15/01/2015",inplace=True)
df.replace('22/01//2015',"22/01/2015",inplace=True)
year=df['Date'].str.split('/',expand=True)[2]
freq=year.value_counts()
freq.sort_index(ascending=True,inplace=True)
#print(freq)
x=freq.index
y=freq

plt.plot(x,y)
plt.show()
s=x.shape[0]
for i in range(s):
    
    print(x[i],y[i])

