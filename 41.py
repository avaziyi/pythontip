# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 20:44:07 2013

@author: 子怿
"""

def Jinzhi(a,num):
    result = 0
    while a != 0:
        add = a - a/num*num    
        result += add
        a = a / num
    return result
    
n = 2992   
if Jinzhi(n,10) == Jinzhi(n,16) == Jinzhi(n,12):
    print "Yes"
else:
    print "No"