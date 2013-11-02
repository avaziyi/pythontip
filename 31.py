# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 18:57:27 2013

@author: 子怿
"""

def Moun(L):
#    print L
    count = 0
    for i in xrange(1,len(L)-1):
        if L[i]>L[i-1] and L[i]>L[i+1]:
            count += 1
    return count
    
h=[0.9,1.2,1.22,1.1,1.6,0.99]
print Moun(h)