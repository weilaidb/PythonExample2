#!/usr/bin/python
# -*- coding: GBK -*-
'''
Created on 2017��12��23��

@author: Administrator
'''
from test import num


print "%x " % 108

print "%X" % 108


print "%#x" % 108

print "%#X " % 108

print '%f' % 1234.567890
print '%.2f' % 1234.67890

print '%E' % 1234.567890
print '%e' % 1234.567890

print '%g' % 1234.567890
print '%G' % 1234.567890

print "%e" %(11111111111111111111111111111111L)




print "%+d" % 4
print "%+d" % -4

print "we are at %d%%" % 100
print 'Your host is: %s' % 'earth'
print 'Host:%s\tPort:%d' % ('mars', 80)

num = 123
print 'dec:%d/ oct:%#o/ hex:%#X' % (num, num, num)


print "MM/DD/YY = %02d/%02d/%d" % (2,15, 67)

w,p = 'Web', 'page'
print 'http://xxx.yyy.zzz/%s/%s.html' % (w, p)


print 'There are %(howmany)d %(lang)s Quotation Symbols' % \
    {'lang': 'Python', 'howmany': 3}
    
    
    
    
    
