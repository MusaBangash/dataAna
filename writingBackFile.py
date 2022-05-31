import imp
from urllib.request import urlretrieve
import pandas as pd

#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

italyCovid = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urlretrieve(italyCovid, 'italy-covid-daywise.csv')


urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 
            'locations.csv')

locations_df = pd.read_csv('locations.csv')
df=pd.read_csv('italy-covid-daywise.csv')
initalTest=935310

df['total_cases'] = df.new_cases.cumsum()
df['total_deaths'] = df.new_deaths.cumsum()
df['total_tests'] = df.new_tests.cumsum() + initalTest



df['location']='Italy'
mergeddf=df.merge(locations_df,on='location')
mergeddf['cases_per_million']=mergeddf.total_cases*1e6/mergeddf.population
mergeddf['deaths_per_million']=mergeddf.total_deaths*1e6/mergeddf.population
mergeddf['tests_per_million']=mergeddf.total_tests*1e6/mergeddf.population




print(mergeddf.head(2))


result_df = mergeddf[['date',
                       'new_cases', 
                       'total_cases', 
                       'new_deaths', 
                       'total_deaths', 
                       'new_tests', 
                       'total_tests', 
                       'cases_per_million', 
                       'deaths_per_million', 
                       'tests_per_million']]


print(result_df.head(2))

result_df.to_csv('results.csv', index=None)


print(result_df.new_cases.plot())






