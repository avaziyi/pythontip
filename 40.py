# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 20:25:49 2013

@author: 子怿
"""

def Zheng(a,b):
    if a<0 and b>0:
        st = a
        ed = 0
    elif a>0 and b>0:
        st = 1
        ed = a+1
    else:
        st = -10000
        ed = 10000
    for i in xrange(st,ed):
        sheng = a - i
        if i*sheng == b:
            print "Yes"
            print i,sheng
            return ''
        else:
            continue
    print "No"
    return ''
            
Zheng(1,-25)