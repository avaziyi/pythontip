# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 14:23:10 2013

@author: 子怿
"""

def Listrank(L):
    length = len(L)
    for i in xrange(length):
        for j in xrange(i+1,length):
            if L[i]>L[j]:
                L[i],L[j] = L[j],L[i]
    return L

L = [3,7,1,99]
print Listrank(L)

