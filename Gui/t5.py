'''''12.Listbox与变量绑定'''
# -*- coding: utf-8 -*-
from tkinter import *
root = Tk()
v = StringVar()
lb = Listbox(root,listvariable = v)
for i in range(10):
    lb.insert(END,str(i*100))
#打印当前列表中的项值
print(v.get())
#输出：('0', '100', '200', '300', '400', '500', '600', '700', '800', '900')
#改变v的值,使用tuple可以与item对应
v.set(('1000','200'))
#结果只有两项了1000和200
lb.pack()
root.mainloop()  