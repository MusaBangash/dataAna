import imp
from urllib.request import urlretrieve
import pandas as pd


italyCovid = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urlretrieve(italyCovid, 'italy-covid-daywise.csv')

df=pd.read_csv('italy-covid-daywise.csv')


#what is the total number of reported case4s and deaths related to covid

totalCases=df.new_cases.sum()
totalDeaths=df.new_deaths.sum()

print(totalCases)
print(totalDeaths)

print('the number of reported cases is {} and number of deaths {}'.format(totalCases,totalDeaths) )


#what is overall death ratio

deathRate=df.new_deaths.sum()/df.new_cases.sum()
print('the overall reported death rate in italy is {:.2f}'.format(deathRate))
#.2f mean 2 floating points 



#what is the overall number tests conducted. 
#first non Nan indext using first valid index

initalTest=935310
totalTest=initalTest+df.new_tests.sum()
print(totalTest)



#fractin of test return postive result 
postiveRate=totalCases/totalTest
print('{:.2f} of tests in itlay led positive'.format(postiveRate))



