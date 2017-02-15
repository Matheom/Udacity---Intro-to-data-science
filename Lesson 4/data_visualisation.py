#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:09:08 2017

@author: matthew
"""
import pandas 
from ggplot import *

df = pandas.read_csv('turnstile_data_master_with_weather.csv')

df_hours = df[['Hour','ENTRIESn_hourly']].groupby('Hour', as_index = False).sum()
print(df_hours)

ggplot(df_hours, aes('Hour', 'ENTRIESn_hourly')) + ggtitle('THE TITLE') +\
ylab('ENTRIES') + xlab('Hour') + geom_line(color = 'red') 


#df_hours = df[['Hour','ENTRIESn_hourly']]
#df_grouped_hours = df_hours.groupby('Hour', as_index = False).sum()
#
#
##df = df[['Hour','ENTRIESn_hourly']].groupby('Hour', as_index=False).sum()
#
#print(df_grouped_hours)
##
#ggplot(df_grouped_hours, aes('Hour','ENTRIESn_hourly')) + geom_line() + ggtitle('fuck you') +\
#      xlab('Hour') + ylab('entries')

