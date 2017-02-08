#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:33:46 2017

@author: matthew
"""
import numpy as np
import pandas as pd
import pandasql


path_to_csv = "aadhaar_data.csv"


df = pd.read_csv(path_to_csv)

df.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)


q = """SELECT sum(aadhaar_generated) as volume,
                   gender,
                   district
      FROM df
      where age  > 50
           
      group by 
                  gender,
                  district;"""
                            

aadhaar_solution = pandasql.sqldf(q.lower(), locals())

print(aadhaar_solution)


# Write a query that will select from the aadhaar_data table how many men and how 
    # many women over the age of 50 have had aadhaar generated for them in each district.
    # aadhaar_generated is a column in the Aadhaar Data that denotes the number who have had
    # aadhaar generated in each row of the table





