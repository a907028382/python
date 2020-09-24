# -*- coding: utf-8 -*-
# @Time : 2020/6/17 11:06
# @Author : Fan
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askdirectory,askopenfilename
import windnd
import os
#拖拉函数
def dragged_file(files):
    msg = '\n'.join(item.decode('gbk') for item in files)
    path.set(msg)
def select_path():
    #path_ = askdirectory()
    filepath = askopenfilename()
    #path.set(path_)
    path.set(filepath)

def get_content():
    content = path.get()
    print(content)

window = tk.Tk()
window.title('安卓检测工具')
#大小
window.geometry('600x600')
#tk.Label(window,text="选择检测的包体:",font=('Arial',10)).place(x=10,y=10)
#接收包体信号
path = tk.StringVar()
value = tk.StringVar()
#e = tk.Entry(window,show=None).place(x=150,y=10)
tk.Label(window,text="目标路径").grid(row=0,column=0)
tk.Entry(window,textvariable=path).grid(row=0,column=1)
tk.Button(window,text="路径选择",command=select_path).grid(row=0,column=2)
tk.Button(window,text="显示名称",command=get_content).grid(row=0,column=3)
windnd.hook_dropfiles(window,func=dragged_file)


window.mainloop()
