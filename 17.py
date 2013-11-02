# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 16:21:07 2013

@author: 子怿
"""

def Gcd(a,b):
    if a<b:
        a,b = b,a
    while b!=0:
        a,b = b, a%b
    return a
    
a = 32
b = 16
max1 = Gcd(a,b)
count = 0
for i in xrange(1,max1):
    if a%i == 0 and b%i == 0:
        count += 1

print count+1