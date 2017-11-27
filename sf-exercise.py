# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 21:18:29 2017

@author: tinyjaguar
"""

import pandas as pd
sal = pd.read_csv('Salaries.csv')

print("Printing head")
print(sal.head(5))

print("Printing info")
print(sal.info())

#===============================================================================
# print("Average base pay is ")
# print((sal['BasePay']).mean())
# 
# print("Highest overtime in set is ")
# print((sal['OvertimePay']).max())
# 
# print("Searching for JOSEPH DRISCOLL ")
# 
# driscoll = sal[sal['EmployeeName']=='JOSEPH DRISCOLL']
# print(driscoll['JobTitle'])
# 
# print("How much JOSEPH DRISCOLL make (including benefits)? ")
# print(driscoll['TotalPayBenefits'])
# 
# print("Name of highest paid person (including benefits)")
# print(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()])
# 
# print("What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?")
# print(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()])
# 
# print("Average (mean) BasePay of all employees per year? (2011-2014) ")
# print(sal.groupby('Year').mean()['BasePay'])
# 
# print("How many unique job titles are there? ")
# print(sal['JobTitle'].nunique())
#===============================================================================
#===============================================================================
# 
# print("What are the top 5 most common jobs? ")
# print(sal['JobTitle'].value_counts().head(5))
#===============================================================================
print("How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?)")
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts()==1))

