# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 15:51:53 2013

@author: 子怿
"""

def numof1(num):
    i = 0
    while num != 1:
        yu = num % 2
        num = num / 2
        if yu == 1:
            i += 1
    print i+num

#numof1(13)

def num2(n):
    count = 0
    while n:
        if n & 1:
            count += 1
        n = n >> 1
    print count

num2(8)