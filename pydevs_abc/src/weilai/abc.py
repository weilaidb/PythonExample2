#coding=gbk
'''
Created on 2017年11月26日

@author: Administrator
'''

from Tkinter import *
from unicodedata import east_asian_width
from idlelib.ZoomHeight import zoom_height



if __name__ == '__main__':
    root = Tk()
    root.title("hello world")
    root.geometry('500x300')
    root.resizable(width=FALSE, height=TRUE)
    
    l = Label(root, text="show", bg="green", font=("Arial",12), width=5, height=2)
    l.pack(side=LEFT)
    
    Label(root, text='校训 '.decode('gbk').encode('utf8'), font=('Arial', 20)).pack()
    
    frm = Frame(root)
    #left
    frm_L = Frame(frm)
    Label(frm_L, text='厚德'.decode('gbk').encode('utf8'), font=('Arial', 15)).pack(side=TOP)
    Label(frm_L, text='博学'.decode('gbk').encode('utf8'), font=('Arial', 15)).pack(side=TOP)
    frm_L.pack(side=LEFT)
    
    
    
    root.mainloop()









































