#!/usr/bin/python
# -*- coding: GBK -*-
'''
Created on 2017年12月23日

@author: Administrator
'''


hi=''' hi there'''
print hi #repr()
print hi #str()

print id(hi)

s = 'abcdefghi'
print s 

s = '%sC%s' % (s[0:2], s[3:])
print s 