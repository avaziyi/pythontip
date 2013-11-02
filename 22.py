# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 17:51:51 2013

@author: 子怿
"""

def TimeD(st,et):
    st1,st2,st3 = st.split(":")
    et1,et2,et3 = et.split(":")    
    print (int(et3)-int(st3)) + (int(et2)-int(st2))*60 + (int(et1)-int(st1))*60**2
    
TimeD("00:00:00","01:01:10")