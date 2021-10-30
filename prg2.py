'''
Find out which cities are generally chosen for starting a startup.
Find top 10 Indian cities which have most number of startups ?
Plot a pie chart and visualise it.
Print the city name and number of startups in that city also.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("startup_funding.csv")
df.replace("Delhi","New Delhi",inplace=True)
df["CityLocation"].dropna(inplace=True)
def separateCity(s):
    return s.split("/")[0].strip()
df["CityLocation"] = df["CityLocation"].apply(separateCity)
city=df['CityLocation'].str.title()
fq=city.value_counts().head(10)
#print(fq)
x=fq.index
y=fq
plt.pie(y,labels=x)
plt.show()
for i in range(x.shape[0]):
    print(x[i],y[i])
