#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:33:46 2017

@author: matthew
"""
from scipy import stats
import numpy as np

#np.random.seed(12345678)

rvs1 = stats.norm.rvs(loc=5,scale=10,size=500)
rvs2 = stats.norm.rvs(loc=5,scale=10,size=500)
rvs3 = stats.norm.rvs(loc=5, scale=20, size=500)


print(stats.ttest_ind(rvs1,rvs3))