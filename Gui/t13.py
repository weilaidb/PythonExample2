from tkinter import *


root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i))
lb.selection_set(6,9)      #选择第7个到第10个item
lb.selection_clear(7,8)    #取消圈选第8个和第9个
lb.pack()
root.mainloop()  