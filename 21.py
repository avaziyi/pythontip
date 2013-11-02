# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 17:42:03 2013

@author: 子怿
"""

def Huiwen(a,n):
    if n == 1:
        print "YES"
        return ''
    if n > len(a):
        print "NO"
        return ''
    if n == len(a):
        if a[::-1] == a:
            print "YES"
            return ''
        else:
            print "NO"
            return ''
    for i in xrange(2,n+1):
        for j in xrange(0,len(a)-n):
            s = a[j:j+n]
            if s[::-1] == s:
                print "YES"
                return ''
            else:
                print "NO"
                return ''
    
Huiwen('ababa',5)