#!/usr/bin/python
# -*- coding: GBK -*-
'''
Created on 2017年12月23日

@author: Administrator
'''


names = ('Faye', 'wang wang', 'qianqian')
print names[2]
print ('Faye', 'wang wang', 'qianqian')[1]


s = 'abcdefgh'
print s[::-1] ##可视做“翻转”操作
print s[::2]


print '\n' *2
print '=' * 10
s = 'abcde'
i = -1
for i in range(-1, -len(s), -1):
    print s[:i]
    
    
    
print s[:0]
# 
# for i in [None].extend(range(-1, -len(s), -1)):
#     print s[:i]
#     
    






















