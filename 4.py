# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 14:36:46 2013

@author: 子怿
"""

a={1:1,2:2,3:3}
d = []
for i in a.keys():
    d.append(str(i))
print ','.join(d)