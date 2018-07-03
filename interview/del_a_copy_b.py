# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 16:57:09 2017

@author: ice-fire
"""

# 字符替换和复制,删除字符串所有的a，并复制所有的b
def del_a_copy_b(s)
    n, numb, i = 0, 0, 0
    while i < len(s):
        if s[i] is not 'a':
            s[n += 1] = s[i]
        if s[i] == 'b':
            numb += 1
    s[n] = 0
        