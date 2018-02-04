'''''5.向Listbox中添加一个item'''
# 以上的例子均使用了insert来向Listbox中添加 一个item，这个函数有两个属性一个为添加的索引值，另一个为添加的项(item)
#  有两个特殊的值ACTIVE和END，ACTIVE是向当前选中的item前插入一个（即使用当前选中的索引作为插入位置）；END是向
#  Listbox的最后一项添加插入一项
# 先向Listbox中追加三个item，再在Listbox开始添加三项
from tkinter import *
root = Tk()
lb = Listbox(root)
for item in ['python','tkinter','widget']:
    lb.insert(END,item)
#只添加一项将[]作为一个item
#lb.insert(0,['linux','windows','unix'])
#添加三项，每个string为一个item
lb.insert(0,'linux','windows','unix')
lb.pack()
root.mainloop()  