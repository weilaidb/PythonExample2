from tkinter import *
root = Tk()
v = StringVar()
lb = Listbox(root,listvariable = v)
for i in range(10):
    lb.insert(END,str(i*100))
print (v.get())              #输出了若干值
v.set(('1000','200'))        #Listbox只列出俩值
lb.pack()
root.mainloop()  