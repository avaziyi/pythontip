# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 15:25:30 2013

@author: 子怿
"""

def Gcd(a,b):
    if a<b:
        a,b = b,a
    while b!=0:
        a,b = b, a%b
    print a

Gcd(18,15)