# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 21:34:59 2013

@author: 子怿
"""

def fi2(n,a=1,b=0):
#    a = 1
#    b = 0
    while n>0:
        a,b = b,a+b
        n -= 1
#    print b
    return b

print fi2(10)