#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 08:23:34 2017

@author: matthew
"""

import pandas
import pandasql

def avg_weekend_temperature(filename):
    '''
    This function should run a SQL query on a dataframe of
    weather data.  The SQL query should return one column and
    one row - the average meantempi on days that are a Saturday
    or Sunday (i.e., the the average mean temperature on weekends).
    The dataframe will be titled 'weather_data' and you can access
    the date in the dataframe via the 'date' column.
    
    You'll need to provide  the SQL query.
    
    Also, you can convert dates to days of the week via the 'strftime' keyword in SQL.
    For example, cast (strftime('%w', date) as integer) will return 0 if the date
    is a Sunday or 6 if the date is a Saturday.
    
    You can see the weather data that we are passing in below:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/weather_underground.csv
    '''
    weather_data = pandas.read_csv(filename)
    
    #print weather_data.dtypes
    
    q = """
    select avg(meantempi) as average from weather_data where cast(strftime('%w', date) as integer) in (0,6)
    """
    
    #Execute your SQL command against the pandas frame
    mean_temp_weekends = pandasql.sqldf(q.lower(), locals())
    return mean_temp_weekends