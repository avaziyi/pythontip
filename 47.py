# -*- coding: utf-8 -*-
"""
Created on Sun Nov 03 20:08:21 2013

@author: 子怿
"""

def CalcValue(n):
    value=[0]*n
    print value
    for i in range(n):
        value[i]=[0]*(i+1)  #这里应该是value【i】，i不见了

    for i in range(n):
        for j in range(i+1):
            if j==0 or j==i:#这里要考虑最后一个元素
                value[i][j]=1
            else:
                value[i][j]=value[i-1][j-1]+value[i-1][j]
                
    return value

print CalcValue(4)

def pascals_triangle(n):
    x=[[1]]
    for i in range(n-1):
        x.append(list(map(sum,zip([0]+x[-1],x[-1]+[0]))))
    return x

for i in pascals_triangle(4):
    i = [str(j) for j in i]
    print ' '.join(i)