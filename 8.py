# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 15:06:35 2013

@author: 子怿
"""

#L = [0,1,9]
##print "%.1f" % sum(L)/len(L)
#s1 = sum(L)/len(L)
#s2 = round(float(sum(L))/len(L),1)
#if sum(L) % len(L) == 0:
#    print s1
#else:
#    print s2

def median(L):
    n = len(L) 
    copy = L[:] # So that "numbers" keeps its original order 
    copy.sort() 
    if n & 1: # There is an odd number of elements 
        return copy[n/2] 
    else: 
        temp = float(copy[n/2-1]+copy[n/2]) / 2
#        print temp
        return round(temp,1)

L = [0,2,3,4]
print median(L)