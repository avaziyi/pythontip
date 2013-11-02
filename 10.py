# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 15:28:30 2013

@author: 子怿
"""

def Gcd(a,b):
    if a<b:
        a,b = b,a
    while b!=0:
        a,b = b, a%b
    return a

def Lcm(a,b):
    return a*b/Gcd(a,b)
    
print Lcm(18,15)