# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 21:24:45 2013

@author: 子怿
"""

def fi(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n>2:
        return fi(n-1)+fi(n-2)

def fi2(n):
    a = 1
    b = 0
    while n>0:
        a,b = b,a+b
        n -= 1
#    print b
    return b
    
result = fi2(10)
print result
print result % 20132013