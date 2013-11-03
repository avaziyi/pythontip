# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 16:10:03 2013

@author: 子怿
"""

import this
s=this.s
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

#print u'python 之禅' 
print "".join([d.get(c, c) for c in s])

#print u'Python之禅'