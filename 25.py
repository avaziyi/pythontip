# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 18:06:51 2013

@author: 子怿
"""

def Geshi(L):
    new = []
    for i in L:
        if len(i)<3:
            temp = '0' + i
#            print temp
            temp = temp[-2::]
            new.append(temp)
#            return temp
        else:
            new.append(i)
    return new

t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}
fir = [t['year'],t['month'],t['day']]
sed = [t['hour'],t['minute'],t['second']]


print '-'.join(Geshi(fir)),':'.join(Geshi(sed))