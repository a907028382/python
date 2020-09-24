# -*- coding: utf-8 -*-
# @Time : 2020/7/2 10:43
# @Author : Fan
import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('500x300')
ll = tk.Label(window,bg='green',fg='white',width=20,text='empty')
ll.pack()

def print_selection(v):
    ll.config(text='you select '+v)

s = tk.Scale(window, label='try me', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
s.pack()
window.mainloop()