# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 20:57:34 2013

@author: 子怿
"""
import math

def Zhishu(n):
    if n <= 1:  
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    for i in range(2, n-1):#int(math.sqrt(n)) + 1):  
        if n % i == 0:  
            return False 
    return True

#s = Zhishu(11)
#print s
#print Zhishu(9)
#print Zhishu(7)

def Fen(n):
    result = 0
    for i in xrange(1,n/2,2):
#        print i
        if Zhishu(i) and Zhishu(n-i):
            print i,'+',n-i
            result += 1
    return result

print Fen(16)