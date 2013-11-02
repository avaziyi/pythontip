# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 15:47:51 2013

@author: 子怿
"""

def Numof25(num):
    i2 = 0
    i5 = 0
    while num % 2 == 0:
        i2 += 1
        num = num / 2
    while num % 5 == 0:
        i5 += 1
        num = num / 5 
    return i2,i5

L = [2,8,3,50]
i2all = 0
i5all = 0
chengji = 1
for i in L:
    i2,i5 = Numof25(i)
    i2all += i2
    i5all += i5    
    chengji *= i
    
num25 = min(i2all,i5all)
hundred = 10**(num25)
sheng = chengji/(10**(num25))
last = sheng - sheng/10*10
print last & 1
