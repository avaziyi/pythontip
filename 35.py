# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 20:07:02 2013

@author: 子怿
"""


def MCS(L):
    print L
    test1 = float("-Infinity") 
    test2 = float("-Infinity") 
    for i in xrange(0,len(L)-1):
        result1 = L[i]
        print '---',result1
        result2 = 0
        for j in xrange(i+1,len(L)):
            result2 += L[j] 
            print '+++',result2
            if result2 <= 0:
                break
            print 'result2',result2
            if result2 > test1:
                test1 = result2
                print 'max1',test1
        max2 = max(test1,result1)
        print 'fi',max2     
        if max2 > test2:
            test2 = max2
            print 'test2',test2
    return test2
            
            
L = [2,-3,10,3,50]
L2 = [4,-3,-3,-4]
print MCS(L)