#This script creates a table containing the presence of dense urban centers based on the best assessment at each of 10 time slices

import pandas as pd
import numpy as np
survey = pd.read_csv('Survey_scrubbed_Aug6.csv')

#isolate first column of interest
df1 = survey.iloc[:,0:12].copy()
df2 = survey.iloc[:,63:73].copy()
df1 = pd.concat([df1,df2],axis=1)


#sort values to visualize data better
df3 = df1.sort_values('Region', ascending=1)

#replace string values w/ integers
intreplace = {'None': 0, 'Low': 1, 'High': 2}
df4 = df3.replace({'EXPERTISE_10kbp': intreplace,'EXPERTISE_8kbp': intreplace,'EXPERTISE_6kbp': intreplace,'EXPERTISE_4kbp': intreplace,'EXPERTISE_3kbp': intreplace,'EXPERTISE_2kbp': intreplace,'EXPERTISE_1kbp': intreplace,'EXPERTISE_1500CE': intreplace,'EXPERTISE_1750CE': intreplace,'EXPERTISE_1850CE': intreplace})

intreplace2 = {'Absent': 0, 'Present': 1}
df5 = df4.replace({'URBAN_CENTERS_10kbp': intreplace2,'URBAN_CENTERS_8kbp': intreplace2,'URBAN_CENTERS_6kbp': intreplace2,'URBAN_CENTERS_4kbp': intreplace2,'URBAN_CENTERS_3kbp': intreplace2,'URBAN_CENTERS_2kbp': intreplace2,'URBAN_CENTERS_1kbp': intreplace2,'URBAN_CENTERS_1500CE': intreplace2,'URBAN_CENTERS_1750CE': intreplace2,'URBAN_CENTERS_1850CE': intreplace2})



#ITERATION FOR URBAN_CENTERS AT 10KBP
#get max expertise level for each region
def func(group):
    return group.loc[group['EXPERTISE_10kbp'] == group['EXPERTISE_10kbp'].max()]

maxexpert = df5.groupby('Region', as_index=False).apply(func).reset_index(drop=True)

#Finds the median of the values in the Urban Centers column
median_value = maxexpert.groupby('Region', as_index = False)['URBAN_CENTERS_10kbp'].agg('median')

#select columns we want and save it to a time slice dataframe
urban10 = median_value.iloc[:,0:2].copy()




#ITERATION FOR URBAN_CENTERS AT 8KBP
#get max expertise level for each region
def func(group):
    return group.loc[group['EXPERTISE_8kbp'] == group['EXPERTISE_8kbp'].max()]

maxexpert2 = df5.groupby('Region', as_index=False).apply(func).reset_index(drop=True)

#Finds the median of the values in the Urban Centers column
median_value2 = maxexpert2.groupby('Region', as_index = False)['URBAN_CENTERS_8kbp'].agg('median')

#select columns we want and save it to a time slice dataframe
urban8 = median_value2.iloc[:,[1]].copy()



#ITERATION FOR URBAN_CENTERS AT 6KBP
#get max expertise level for each region
def func(group):
    return group.loc[group['EXPERTISE_6kbp'] == group['EXPERTISE_6kbp'].max()]

maxexpert3 = df5.groupby('Region', as_index=False).apply(func).reset_index(drop=True)

#Finds the median of the values in the Urban Centers column
median_value3 = maxexpert3.groupby('Region', as_index = False)['URBAN_CENTERS_6kbp'].agg('median')

#select columns we want and save it to a time slice dataframe
urban6 = median_value3.iloc[:,[1]].copy()



#ITERATION FOR URBAN_CENTERS AT 4KBP
#get max expertise level for each region
def func(group):
    return group.loc[group['EXPERTISE_4kbp'] == group['EXPERTISE_4kbp'].max()]

maxexpert4 = df5.groupby('Region', as_index=False).apply(func).reset_index(drop=True)

#Finds the median of the values in the Urban Centers column
median_value4 = maxexpert4.groupby('Region', as_index = False)['URBAN_CENTERS_4kbp'].agg('median')

#select columns we want and save it to a time slice dataframe
urban4 = median_value4.iloc[:,[1]].copy()



#ITERATION FOR URBAN_CENTERS AT 3KBP
#get max expertise level for each region
def func(group):
    return group.loc[group['EXPERTISE_3kbp'] == group['EXPERTISE_3kbp'].max()]

maxexpert5 = df5.groupby('Region', as_index=False).apply(func).reset_index(drop=True)

#Finds the median of the values in the Urban Centers column
median_value5 = maxexpert5.groupby('Region', as_index = False)['URBAN_CENTERS_3kbp'].agg('median')

#select columns we want and save it to a time slice dataframe
urban3 = median_value5.iloc[:,[1]].copy()




#ITERATION FOR URBAN_CENTERS AT 2KBP
#get max expertise level for each region
def func(group):
    return group.loc[group['EXPERTISE_2kbp'] == group['EXPERTISE_2kbp'].max()]

maxexpert6 = df5.groupby('Region', as_index=False).apply(func).reset_index(drop=True)

#Finds the median of the values in the Urban Centers column
median_value6 = maxexpert6.groupby('Region', as_index = False)['URBAN_CENTERS_2kbp'].agg('median')

#select columns we want and save it to a time slice dataframe
urban2 = median_value6.iloc[:,[1]].copy()



#ITERATION FOR URBAN_CENTERS AT 1KBP
#get max expertise level for each region
def func(group):
    return group.loc[group['EXPERTISE_1kbp'] == group['EXPERTISE_1kbp'].max()]

maxexpert7 = df5.groupby('Region', as_index=False).apply(func).reset_index(drop=True)

#Finds the median of the values in the Urban Centers column
median_value7 = maxexpert7.groupby('Region', as_index = False)['URBAN_CENTERS_1kbp'].agg('median')

#select columns we want and save it to a time slice dataframe
urban1 = median_value7.iloc[:,[1]].copy()




#ITERATION FOR URBAN_CENTERS AT 1500CE
#get max expertise level for each region
def func(group):
    return group.loc[group['EXPERTISE_1500CE'] == group['EXPERTISE_1500CE'].max()]

maxexpert8 = df5.groupby('Region', as_index=False).apply(func).reset_index(drop=True)

#Finds the median of the values in the Urban Centers column
median_value8 = maxexpert8.groupby('Region', as_index = False)['URBAN_CENTERS_1500CE'].agg('median')

#select columns we want and save it to a time slice dataframe
urban1500 = median_value8.iloc[:,[1]].copy()




#ITERATION FOR URBAN_CENTERS AT 1750CE
#get max expertise level for each region
def func(group):
    return group.loc[group['EXPERTISE_1750CE'] == group['EXPERTISE_1750CE'].max()]

maxexpert9 = df5.groupby('Region', as_index=False).apply(func).reset_index(drop=True)

#Finds the median of the values in the Urban Centers column
median_value9 = maxexpert9.groupby('Region', as_index = False)['URBAN_CENTERS_1750CE'].agg('median')

#select columns we want and save it to a time slice dataframe
urban1750 = median_value9.iloc[:,[1]].copy()





#ITERATION FOR URBAN_CENTERS AT 1850CE
#get max expertise level for each region
def func(group):
    return group.loc[group['EXPERTISE_1850CE'] == group['EXPERTISE_1850CE'].max()]

maxexpert10 = df5.groupby('Region', as_index=False).apply(func).reset_index(drop=True)

#Finds the median of the values in the Urban Centers column
median_value10 = maxexpert10.groupby('Region', as_index = False)['URBAN_CENTERS_1850CE'].agg('median')

#select columns we want and save it to a time slice dataframe
urban1850 = median_value10.iloc[:,[1]].copy()




urban_centers = pd.concat([urban10, urban8, urban6, urban4, urban3, urban2, urban1, urban1500, urban1750, urban1850],axis=1)


urban_centers.to_csv('Urban_Centers_v2.csv')

print('Done!')
