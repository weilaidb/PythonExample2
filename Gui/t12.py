from tkinter import *

root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i))
lb.delete(1,3)                        #1-3被删除。lb.delete(0,END）会删掉所有item
lb.pack()
root.mainloop()  