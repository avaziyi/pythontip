# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 18:46:30 2013

@author: 子怿
"""

def San(a,b,c):
    if a<0 or b<0 or c<0:
        print "NO"
    minN = min(a,b,c)
    maxN = max(a,b,c)
    oth = a + b + c - minN - maxN
    if minN + oth > maxN:
        print "YES"
    else:
        print "NO"

San(3,4,9)