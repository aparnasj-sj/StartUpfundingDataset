'''
Which type of companies got more easily funding. To answer this question, find -
Top 5 industries and percentage of the total amount funded to that industry. (among top 5 only)
Print the industry name and percentage of the amount funded with 2 decimal place after rounding off.
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
df.replace("eCommerce","Ecommerce",inplace=True)
df.replace("ECommerce","Ecommerce",inplace=True)
df.replace("ecommerce","Ecommerce",inplace=True)

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
df2=df.groupby('IndustryVertical') # grp by U 
grp=df2['AmountInUSD'].agg(np.sum).sort_values(ascending=False).head(5) #
x=grp.index
y=grp.values
#x=grp.keys()

Percentage=np.true_divide(y,y.sum())*100

plt.pie(grp,labels=x,autopct="%1.2f%%")
plt.show()
for i in range(len(x)):
    print(x[i],format(Percentage[i],'.2f'))



