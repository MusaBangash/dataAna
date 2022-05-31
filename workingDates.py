import imp
from turtle import position
from urllib.request import urlretrieve
import pandas as pd


italyCovid = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urlretrieve(italyCovid, 'italy-covid-daywise.csv')

df=pd.read_csv('italy-covid-daywise.csv')


print(df.date)

#pd.to_datetime(df.date date time format of panda you can change from string to panda datetime format

df['date']=pd.to_datetime(df.date)

print(df['date'])

#extract different part of date


df['year']=pd.DatetimeIndex(df.date).year
df['month']=pd.DatetimeIndex(df.date).month
df['day']=pd.DatetimeIndex(df.date).day
df['weekday']=pd.DatetimeIndex(df.date).weekday
#print(df.head(2))



#now check for months as we have month column 

dfMM=df[df.month==5]
#print(dfMM)


dfmm=dfMM[['new_cases','new_deaths','new_tests']]   #double braket because of indexing 
print(dfmm)


mayTotal=dfmm.sum()
print(mayTotal)


#over all average

print(df.new_cases.mean())


#average for sunday
print(df[df.weekday==6].new_cases.mean())