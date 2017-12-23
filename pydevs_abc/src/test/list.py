#!/usr/bin/python
# -*- coding: GBK -*-
'''
Created on 2017年12月23日

@author: Administrator
'''


aList = [123, 'abc', 4.56, ['inner', 'list'], 7-9j]
anotherList = [None, 'something to see here']

print aList
print anotherList

aListThatStartedEmpty = []
print aListThatStartedEmpty

print list('foo')


print aList[0]
print aList[1:4]
print aList[:3]

aList[2] = 'float replacer'

print aList

anotherList.append("hi, i'm new here? ")
print anotherList


aListThatStartedEmpty.append("not empty anymore")
print aListThatStartedEmpty



aList.remove(123)
print aList
del aList
print aList








