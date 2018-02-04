from tkinter import *
root = Tk()
def printList(event):
    print ("hi %1") % event
lb = Listbox(root)
lb.bind('<Double-Button-1>',printList)   #绑定双击事件
for i in range(10):
    lb.insert(END,str(i*100))
lb.pack()
root.mainloop()