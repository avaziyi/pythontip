# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 21:36:40 2013

@author: 子怿
"""

def Z(a,b):
    for i in xrange(-10000,10000):
        x = a - i
        if x * i == b:
            print "Yes"
            return ''
    print "No"
    return ''

Z(9,18)