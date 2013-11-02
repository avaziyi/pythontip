# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 19:05:54 2013

@author: 子怿
"""

def Dami(a,n):
    result = 1
    for i in xrange(n):
        result = result*a
        if result > 20132013:
            result = result % 20132013
    return result

#print Dami(99999,100000000000)
a = 99999+1
n = 100000000000
print pow(long(a),long(n),20132013L)