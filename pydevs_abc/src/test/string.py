#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2017骞�12鏈�19鏃� 22:53:54
@author: Administrator
'''
from pickle import APPEND
import string


# from test.test_funcattrs import InstancemethodAttrTest

# from string import import Template


print '\n'
print r'\n'

# f  = open(r'D:\text', 'r')
# f.readline()
# f.close()


import re

m = re.search('\\[retfvn]', r"Hello Word!\n")
if m is not None:
    print "not none" 
    print m.group()

m = re.search(r'\\[rtfvn]', r'Hellow Word!\n')
if m is not None: 
    print m.group()




# user_input = raw_input("Enter your name:")
# 
# print user_input
# 
# print "len of user name is %d" % len(user_input)


print isinstance(u'\0xAB', str)

print not isinstance('foo', unicode)

print isinstance(u'', basestring)

print not isinstance('foo', basestring)



####### chr()

print chr(65)
print ord('a')

print unichr(12345)





##string functions
quest = 'what is your favorite color? '
print quest.capitalize()
print quest.center(40)
print quest.count('or')



print  '=-' * 30
# print string.ascii_uppercase

# print string.ascii_uppercase
# print string.ascii_letters
# print string.ascii_lowercase
# print string.digits



print  '=-' * 30






# if __name__ == '__main__':
#     pass