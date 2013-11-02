# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 21:46:16 2013

@author: 子怿
"""

l = [x for x in range(2,100) if not [y for y in range(2,x/2+1) if x%y == 0]]
l = [str(i) for i in l]
print ' '.join(l)