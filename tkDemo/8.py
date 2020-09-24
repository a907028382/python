# -*- coding: utf-8 -*-
# @Time : 2020/7/3 11:08
# @Author : Fan
import tkinter as tk
window = tk.Tk()
window.title('menu')
window.geometry('400x400')
ll = tk.Label(window,text='    ',bg='green')
ll.pack()

#菜单
menubar = tk.Menu(window)
#文件菜单，默认不显示下拉
filemenu = tk.Menu(menubar,tearoff=0)
#加到菜单的名单里面，容器存放
menubar.add_cascade(label='File',menu=filemenu)
#菜单里加入功能,只能放在command 前，识别不了
counter = 0 #计数
def do():
    global counter
    ll.config(text='do'+str(counter))
    counter += 1

filemenu.add_command(label='New',command=do)
filemenu.add_command(label='Open',command=do)
filemenu.add_command(label='Save',command=do)
#分割线
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)

#编辑框
editmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=editmenu)
#增加下拉功能
def do_edit():
    pass
editmenu.add_command(label='cut',command=do_edit)
editmenu.add_command(label='copy',command=do_edit)

#二级菜单
submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='二级菜单',menu=submenu,underline=0)

#三级菜单,菜单命令
submenu.add_command(label='三级菜单',command=do)
#配置出来
window.config(menu=menubar)
window.mainloop()

