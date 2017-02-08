#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:51:42 2017

@author: matthew
"""

# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library: 
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
#matplotlib inline

names = ['bob','jessica','mary','john','mel']
births = [968, 155, 77,578, 973]

Babydataset = list(zip(names,births))

df = pd.DataFrame(data = Babydataset, columns = ['Names','Births'])

df.to_csv('births1880.csv', index = False,header = False)

Location = '/home/matthew/Udacity - Intro to Data Science/Jupyter Tutorials/births1880.csv'

df1 = pd.read_csv(Location, names = ['Names','Births'])

import os
os.remove(Location)

df.dtypes

Sorted = df.sort_values(['Births'], ascending = False)

df['Births'].plot()

Maxvalue = df['Births'].max()
Maxname = df['Names'][df['Births'] == df['Births'].max()].values
             
Text = str(Maxvalue) + ' - ' + Maxname
          
plt.annotate(Text, xy = (1,Maxvalue), xytext = (8,0),
             xycoords=('axes fraction', 'data'), textcoords = 'offset points')

print('the most popular name')
df[df['Births'] == df['Births'].max()]
