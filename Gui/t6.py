'''''13.Listbox与事件绑定'''
#  它不支持command属性来设置回调函数了，使用bind来指定回调函数,打印当前选中的值
# -*- coding: utf-8 -*-
from tkinter import *
root = Tk()
def printList(event):
    print(lb.get(lb.curselection()))
lb = Listbox(root)
#双击事件
lb.bind('<Double-Button-1>',printList)
for i in range(10):
    lb.insert(END,str(i*100))
lb.pack()
root.mainloop()

#还有一个比较实用的功能没有介绍：滚动条的添加，留到后面介绍Scrollbar的时候再一并介绍