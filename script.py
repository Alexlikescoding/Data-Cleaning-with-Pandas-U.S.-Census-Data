import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import glob

file_list=[]

files=glob.glob('states*.csv')
for file in files:
  data=pd.read_csv(file)
  file_list.append(data)
us_census=pd.concat(file_list)

print(us_census.columns)
#print(us_census.dtypes)
#print(us_census.head())
us_census.Income=us_census.Income.str.replace('$','')

us_census.Hispanic=us_census.Hispanic.str.replace('%','')
us_census.White=us_census.White.str.replace('%','')
us_census.Black=us_census.Black.str.replace('%','')
us_census.Native=us_census.Native.str.replace('%','')
us_census.Asian=us_census.Asian.str.replace('%','')
us_census.Pacific=us_census.Pacific.str.replace('%','')

us_census.Hispanic=pd.to_numeric(us_census.Hispanic)
us_census.White=pd.to_numeric(us_census.White)
us_census.Black=pd.to_numeric(us_census.Black)
us_census.Native=pd.to_numeric(us_census.Native)
us_census.Asian=pd.to_numeric(us_census.Asian)
us_census.Pacific=pd.to_numeric(us_census.Pacific)

################# fill in NaN race percentage based on U.S. national average, values have to sum up to 100 ##################
us_census=us_census.fillna(value={'Hispanic': 17.2, 'White': 62, 'Black': 13.4, 'Native': 1.3, 'Asian': 5.9, 'Pacific': 0.2})

#print(us_census.head())

us_census['split']=us_census.GenderPop.str.split('_')
us_census['Men']=us_census.split.str.get(0)
us_census['Women']=us_census.split.str.get(1)
us_census=us_census.drop(columns=['GenderPop','split'])

us_census.Men=us_census.Men.str.replace('M','')
us_census.Women=us_census.Women.str.replace('F','')
us_census.Men=pd.to_numeric(us_census.Men)
us_census.Women=pd.to_numeric(us_census.Women)
us_census.Income=pd.to_numeric(us_census.Income)
#print(us_census.dtypes)
#print(us_census.head())

plt.scatter(us_census.Women,us_census.Income)
plt.show()

us_census=us_census.fillna(value={'Women': us_census.TotalPop - us_census.Men})
print(us_census.State.value_counts())

us_census=us_census.drop_duplicates(subset=['State'])
print(us_census.State.value_counts())

plt.scatter(us_census.White,us_census.Income)
plt.scatter(us_census.Hispanic,us_census.Income)
plt.scatter(us_census.Black,us_census.Income)
plt.scatter(us_census.Asian,us_census.Income)
plt.scatter(us_census.Native,us_census.Income)
plt.scatter(us_census.Pacific,us_census.Income)
plt.show()
