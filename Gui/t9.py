from tkinter import *
# 依次点击这三个item，均显示为选中状态。
# 属性MULTIPLE允许多选，每次点击item，它将改变自己的当前选状态，与Checkbox有点相似
root = Tk()
lb = Listbox(root,selectmode = MULTIPLE)
for item in ['python','tkinter','widget']:
    lb.insert(END,item)
lb.pack()
root.mainloop()  