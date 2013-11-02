# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 20:16:47 2013

@author: 子怿
"""
'''
no
'''
def MCS(L):
    print L
    su = []
    for i in xrange(0,len(L)-1):
        result = L[i]
        for j in xrange(i+2,len(L)):
            result += L[j]
        print result
        su.append(result)
    return su
            
            
L = [2,-3,3,50]
print MCS(L)