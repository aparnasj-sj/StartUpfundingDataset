'''
There are 4 different type of investments. Find out percentage of amount funded for each investment type.
Plot a pie chart to visualise.
Print the investment type and percentage of amount funded with 2 decimal places after rounding off.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("startup_funding.csv")
# fixing xome spelling issues 
df.replace("Delhi","New Delhi",inplace=True)
df.replace("SeedFunding","Seed Funding",inplace=True)
df.replace("Crowd funding","Crowd Funding",inplace=True)
df.replace("PrivateEquity","Private Equity",inplace=True)
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
df2=df.groupby('InvestmentType') # grp by U 
grp=df2['AmountInUSD'].agg(np.sum).sort_values(ascending=False).head(10) #For each IV type  , apply sum aggrgateion onf amt in usd column
# and sort by value n get highest 10 from tail

x=grp.index
y=grp.values
#x=grp.keys()

Percentage=np.true_divide(y,y.sum())*100
#explode = (0.1, 0.0, 0.2, 0.3)# explode to view % vales better 
#print(x)
plt.pie(grp,labels=x,autopct="%1.2f%%")
plt.show()
for i in range(len(x)):
    print(x[i],format(Percentage[i],'.2f'))



