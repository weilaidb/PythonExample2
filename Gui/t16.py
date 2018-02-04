from tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i*100))
lb.selection_set(3,8)                 #圈选第4个到第9个item
print (lb.curselection())             #返回圈选的item的索引
lb.pack()
root.mainloop()  