from tkinter import *

root = Tk()
lb = Listbox(root,selectmode = EXTENDED)
for item in ['python','tkinter','widget']:
    lb.insert(END,item)
lb.pack()
root.mainloop()