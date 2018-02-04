from tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i*100))
lb.selection_set(3,8)
print (lb.selection_includes(8))             #第9个item是否被选中
print (lb.selection_includes(0))             #第一个item是否被选中

lb.pack()
root.mainloop() 