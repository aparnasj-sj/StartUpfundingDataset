'''
Find out if cities play any role in receiving funding.
Find top 10 Indian cities with most amount of fundings received. Find out percentage of funding each city has got (among top 10 Indian cities only).
Print the city and percentage with 2 decimal place after rounding off.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("startup_funding.csv")
df.replace("Delhi","New Delhi",inplace=True)
df["CityLocation"].dropna(inplace=True)

def separateCity(s):
    return s.split("/")[0].strip()

df["CityLocation"] = df["CityLocation"].apply(separateCity) # for handling multiple cities case 
df["CityLocation"] = df["CityLocation"].str.title() # first letter captial 
def fixamt(s):
    l=s.split(",")
    amt=""
    for n in l:
        amt+=n.strip()
    return amt
#above function will remove all commas from the numbers for conversion to float
df["AmountInUSD"].dropna(inplace=True)
df['AmountInUSD'] = df['AmountInUSD'].apply(fixamt)
df['AmountInUSD'] = df['AmountInUSD'].astype(float) # convert to float
df2=df.groupby('CityLocation') # grp by city 
grp=df2['AmountInUSD'].agg(np.sum).sort_values(ascending=False).head(10) #For each city , apply sum aggrgateion onf amt in usd column
# and sort by value n get highest 10 from tail

x=grp.index
y=grp.values
#x=grp.keys()

Percentage=np.true_divide(y,y.sum())*100
explode = (0.1, 0.0, 0.2, 0.3, 0.2, 0.2,0.1,0.1,0.2,0.2)# explode to view % vales better 
#print(x)
plt.pie(grp,labels=x,explode=explode,autopct="%1.2f%%")
plt.show()
for i in range(len(x)):
    print(x[i],format(Percentage[i],'.2f'))



