import imp
from turtle import position
from urllib.request import urlretrieve
import pandas as pd


italyCovid = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urlretrieve(italyCovid, 'italy-covid-daywise.csv')

df=pd.read_csv('italy-covid-daywise.csv')



highNewCases=df.new_cases>1000
print(highNewCases)

#we can also pass as index
print(df[highNewCases])


#we can write above state as single line 

highNewCases2=df[df.new_cases>100]
print(highNewCases2)



initalTest=935310
#complex query involved multipl column
totalCases=df.new_cases.sum()
totalDeaths=df.new_deaths.sum()
totalTest=initalTest+df.new_tests.sum()
postiveRate=totalCases/totalTest


highRatio=df[df.new_cases / df.new_tests > postiveRate]
#print(highNewCases)


#print(df.new_cases/df.new_tests)

#adding new column to dataFrame

df['postive_rate']=df.new_cases/df.new_tests
print(df.head(2))


#remove column
print(df.drop(columns=['postive_rate'],inplace=True))
print(df.head(2))



#sorting row using column values

print(df.sort_values('new_cases',ascending=False).head(2))
print(df.sort_values('new_deaths', ascending=False).head(2))
print(df.sort_values('new_cases').head(2))




print(df.loc[168:175])


#172 have faulty value so we can put average or mean of two value above and below

d=df.at[172,'new_cases']=(df.at[171,'new_cases']+df.at[173,'new_cases'])/2
print(d)
print(df.at[172,'new_cases'])

