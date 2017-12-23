#!/usr/bin/python
# -*- coding: GBK -*-
'''
Created on 2017年12月23日

@author: Administrator
'''

'''
An example of reading and writing Unicode strings:Writes 
a unicode string to a file in utf-8 and reads itback in.
'''

CODEC='utf-8'
FILE='unicode.txt'

hello_out = u"Hello World 世界的力量\n"
bytes_out =  hello_out.encode(CODEC)
f = open(FILE, 'w')
f.write(bytes_out)
f.close()

f = open(FILE, 'r')
bytes_in = f.read()
f.close()

hello_in = bytes_in.decode(CODEC)
print hello_in





