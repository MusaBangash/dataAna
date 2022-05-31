import imp
from urllib.request import urlretrieve
import pandas as pd


italyCovid = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urlretrieve(italyCovid, 'italy-covid-daywise.csv')


urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 
            'locations.csv')

locations_df = pd.read_csv('locations.csv')
df=pd.read_csv('italy-covid-daywise.csv')

#print(df.head(2))
#print(locations_df)

initalTest=935310

df['total_cases'] = df.new_cases.cumsum()
df['total_deaths'] = df.new_deaths.cumsum()
df['total_tests'] = df.new_tests.cumsum() + initalTest

#print(locations_df[locations_df.location=='Italy'])

df['location']='Italy'
#print(df.head())

#to merage the dataframe you need to atleast one common column

mergeddf=df.merge(locations_df,on='location')
print(mergeddf)


mergeddf['case_per_million']=mergeddf.total_cases*1e6/mergeddf.population
mergeddf['deaths_per_million']=mergeddf.total_deaths*1e6/mergeddf.population
mergeddf['tests_per_million']=mergeddf.total_tests*1e6/mergeddf.population

#print(mergeddf)










