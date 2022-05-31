import imp
from urllib.request import urlretrieve
import pandas as pd


italyCovid = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urlretrieve(italyCovid, 'italy-covid-daywise.csv')

df=pd.read_csv('italy-covid-daywise.csv')

df['year']=pd.DatetimeIndex(df.date).year
df['month']=pd.DatetimeIndex(df.date).month
df['day']=pd.DatetimeIndex(df.date).day
df['weekday']=pd.DatetimeIndex(df.date).weekday

monthdf=df.groupby('month')[['new_cases','new_tests','new_deaths']].sum()

#print(monthdf)


#aggregated by mean
weekdaydf=df.groupby('weekday')[['new_cases','new_tests','new_deaths']].mean()
#print(weekdaydf)


#cummulative sum
df['total_cases']=df.new_cases.cumsum()
print(df.head(2))
