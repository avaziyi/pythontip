# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 17:56:20 2013

@author: 子怿
"""

def Run(year):
    year = int(year)
    if (year%4 == 0 and (year%100 != 0 or year%400 == 0) ) :
        print 366
    else :
        print 365

Run("2012")