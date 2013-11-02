# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 14:40:56 2013

@author: 子怿
"""


#def Sushu(num):
#    No = 0
#    for i in xrange(2,num):
#        if num % i != 0:
#            No += 1
#    if No == num - 2:
#        print num,
##L = Sushu([i for i in range(100)])
#for i in xrange(2,100):
#    Sushu(i)

#import math
#L = [p for p in xrange(2,100) if 0 not in [p%d for d in xrange(2,p-1)]]
#for i in L:
#    print i,

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

for i in xrange(2,100):
    if Zhishu(i):
        print i,