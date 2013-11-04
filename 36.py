# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 20:16:47 2013

@author: 子怿
"""
'''
no
'''
#def MCS(L):
#    print L
#    su = []
#    for i in xrange(0,len(L)-1):
#        result = L[i]
#        for j in xrange(i+2,len(L)):
#            result += L[j]
#        print result
#        su.append(result)
#    return su
#            
#            
#L = [2,-3,3,50]
#print MCS(L)

def LUCS(L):
    sum1 = []
    sum1.append(max(0,L[0]))
    if len(L) > 1:
        sum1.append(max(L[0],L[1]))
        for i in range(2,len(L)):
            if L[i] > sum1[i-1]-sum1[i-2]:
                sum1.append(sum1[i-2]+L[i])
            else:
                sum1.append(sum1[i-1])
    return max(sum1[len(L)-1],0)
    
L=[-2,-2]
print LUCS(L)
