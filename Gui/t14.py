from tkinter import *

root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i))
lb.delete(3)                       #删掉3
print (lb.size())                  #输出item的个数
lb.pack()
root.mainloop()