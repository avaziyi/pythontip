# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 18:32:55 2013

@author: 子怿
"""

def Same(L):
    for i in xrange(0,len(L)-1):
        for j in xrange(i+1,len(L)):
            if L[i] == L[j]:
                print "YES"
                return ''
    print "NO"

s = Same([2,3,4,7])
