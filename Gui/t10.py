from tkinter import *
#使用鼠标进行拖动，可以看到选中的位置随之变化。
# 与BROWSE相似 的为SINGLE，但不支持鼠标移动选中位置。
root = Tk()
lb = Listbox(root,selectmode = BROWSE)
for item in ['python','tkinter','widget']:
    lb.insert(END,item)
lb.pack()
root.mainloop() 