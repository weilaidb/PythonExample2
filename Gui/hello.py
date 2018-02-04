#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import  Tkinter
from Tkinter import *

root = Tk()

li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap','Bootstrap','Bootstrap','Bootstrap','Bootstrap','Bootstrap','Bootstrap','Bootstrap','Bootstrap','Bootstrap','Bootstrap','Bootstrap','Bootstrap','Bootstrap','Bootstrap']
timer  = ['A','B','C','B','C','B','C','B','C','B','C','B','C','B','C','B','C','B','C','B','C','B','C','B','C']
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
listb3 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

for item in timer:              # 第二个小部件插入数据
    listb3.insert(0,item)

listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
listb3.pack()

# 进入消息循环
root.mainloop()


