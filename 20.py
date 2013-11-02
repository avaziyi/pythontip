# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 17:31:09 2013

@author: 子怿
"""
def InfoS(a,b):
    s = []
    for i in a:
        i = ord(i)
        i = i + b
#        print i
        if i>122:
            i = i-26
        s.append(chr(i))
    return s
    
re = InfoS('cagy',3)
print ''.join(re)