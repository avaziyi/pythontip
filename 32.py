# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 19:00:40 2013

@author: 子怿
"""

def San(a,b,c):
    if a<0 or b<0 or c<0:
        return ''
    minN = min(a,b,c)
    maxN = max(a,b,c)
    oth = a + b + c - minN - maxN
    if minN + oth <= maxN:
        return ''
    return minN,oth,maxN

def Xing(a,b,c):
    try:
        a,b,c = San(a,b,c)    
        if a**2 + b**2 > c**2:
            print "R"
        if a**2 + b**2 == c**2:
            print "Z"
        if a**2 + b**2 < c**2:
            print "D"
    except:
        print "W"

Xing(3,4,3)