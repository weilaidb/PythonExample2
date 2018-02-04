'''''6.删除Listbox中的项，使用delete，这个函数也有两个参数，第一个为开始的索引值；
第二个为结束的索引值，如果不指定则只删除第一个索引项。'''
from tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i))
lb.delete(1,3)
lb.pack()
root.mainloop()
#运行程序，只有值0456789,1-3被删除
#删除全部内容,使用delete指定第一个索引值0和最后一个参数END，即可
#lb.delete(0,END)  