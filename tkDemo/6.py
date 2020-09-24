# -*- coding: utf-8 -*-
# @Time : 2020/6/9 18:01
# @Author : Fan
import tkinter

#事件处理
def handler(event,a,b,c):
    print (event)
    print('handler',a,b,c)

#中介函数
def handlerAdapter(fun,**kwds):
    return lambda event,fun = fun,kwds = kwds:fun(event,**kwds)

if __name__ == '__main__':
    root = tkinter.Tk()
    btn = tkinter.Button(text=u'按钮')
    #使用中介函数绑定
    btn.bind("<Button-1>",handlerAdapter(handler,a=1,b=2,c=3))
    btn.pack()
    root.mainloop()