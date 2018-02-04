from tkinter import *
root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END,str(i*100))
print (lb.get(3))               #返回第4个数的值
print (lb.get(3,7))             #返回第4个到第8个的值（以turple的形式）
lb.pack()
root.mainloop()  