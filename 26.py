# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 18:29:09 2013

@author: 子怿
"""

def Xulie(L):
    up = sorted(L)
    down = sorted(L,reverse=True)
    if L == up:
        print "UP"
    elif L == down:
        print "DOWN"
    else:
        print "WRONG"

Xulie([2,3,4,5])