import imp
from urllib.request import urlretrieve
import pandas as pd


italyCovid = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urlretrieve(italyCovid, 'italy-covid-daywise.csv')

df=pd.read_csv('italy-covid-daywise.csv')
#print(df)

#type 
#print(type(df))

#information 
#print(df.info())


#description 
#print(df.describe())

#shape of data frame rows * columns
#print(df.shape)


#print(df['new_cases']) #new cases is column


#print(df['new_cases'][243]) #from specific column
#print(df.at[243,'new_cases']) #panda at method 


#print(df.new_cases)  #acces column
#print(df[['date','new_cases']]) #first bracket for indexing for multiple column



#if you change one dataframe but .copy method will not effect copy
dfCopy=df.copy()
#print(dfCopy)


#specify row access
#print(df.loc[243])
#print(df.head(2))
#print(df.tail(2))


#NAN now information or data avaliable if value blank it interset NAN
#print(df.at[0,'new_tests'])



#print(df.new_tests.first_valid_index())
#print(df.loc[108:113])


#radom sample row retrun

print(df.sample(10))




