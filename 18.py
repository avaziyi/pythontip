# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 16:26:17 2013

@author: 子怿
"""

import math

def Gcd(a,b):
    if a<b:
        a,b = b,a
    while b!=0:
        a,b = b, a%b
    return a
    
def Sol(a,b):
    if a>b:
        a,b = b,a
    result = []
    mul = a*b
    gen = int(math.sqrt(mul))
    for i in xrange(a,gen+1):
        if mul % i == 0:
            new = mul / i
            if a == Gcd(i,new):
                add = i+new
                print i,'+',new,'=',add
                result.append([i,new,i+new])
                
    return result
a = 3
b = 90
s = Sol(a,b)
#sorted(s, key=itemgetter(2))
#https://wiki.python.org/moin/HowTo/Sorting/
s.sort(key=lambda x: int(x[2]))
try:
    for i in s[0][0:2]:
        print i,
except:
    print 'no answer'