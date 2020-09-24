# -*- coding: utf-8 -*-
# @Time : 2020/4/30 16:15
# @Author : Fan
import matplotlib as mat
import matplotlib.pyplot as plt
from pylab import *
from numpy import *

def mat1():
    # 值对应
    x = [1, 3, 5, 7]
    y = [80, 6, 40, 2]
    #间隔0-5生成10个点
    x1 = linspace(0, 5, 10)
    y1 = x1 ** 2
    figure()
    # r 是red
    plot(x1, y1, 'r')
    xlabel('x')
    ylabel('y')
    title("title")
    plt.plot(x, y)
    plt.show()

def mat2():
    x = linspace(0,5,10)
    y = x ** 2
    fig = plt.figure()
    #整图的比例，左右上下
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
    axes.plot(x,y,'r')
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.set_title('title')

    #插入
    axes2.plot(y,x,'g')
    axes2.set_xlabel('y')
    axes2.set_ylabel('x')
    axes2.set_title('insert title')
    plt.show()

def mat3():
    x = linspace(0, 5, 10)
    y = x ** 2
    #两列一行
    fig,axes = plt.subplots(nrows=1,ncols=3)

    for ax in axes:
        ax.plot(x,y,'r')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('title')
    fig.tight_layout()
    plt.show()

def mat4():
    x = linspace(0, 5, 10)
    y = x ** 2
    fig,ax = plt.subplots(figsize=(12,6))
    ax.plot(x,x+1,color="blue",linewidth=0.25)
    ax.plot(x,x+2,color='blue',linewidth=0.50)
    ax.plot(x, x+3, color='blue', linewidth=1.50)
    ax.plot(x, x+4, color='blue', linewidth=2.50)

    ax.plot(x,x+5,color="red",lw=2,linestyle='-')
    ax.plot(x,x+6,color="red",lw=2,ls="-.")
    ax.plot(x,x+7,color="red",lw=2,ls=":")

    line, = ax.plot(x,x+8,color="black",lw=1.5)
    line.set_dashes([5,10,15,10])
    ax.plot(x, x + 9, color="green", lw=2, ls='solid', marker='+')
    ax.plot(x, x + 10, color="green", lw=2, ls='solid', marker='o')
    ax.plot(x, x + 11, color="green", lw=2, ls='solid', marker='s')
    ax.plot(x, x + 12, color="green", lw=2, ls='solid', marker='1')

    ax.plot(x, x + 13, color="purple", lw=1, ls='-', marker='o', markersize=2)
    ax.plot(x, x + 14, color="purple", lw=1, ls='-', marker='o', markersize=4)
    ax.plot(x, x + 15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
    ax.plot(x, x + 16, color="purple", lw=1, ls='-', marker='s', markersize=8,
            markerfacecolor="yellow", markeredgewidth=2, markeredgecolor="blue")

    plt.show()

def mat5():
    x = linspace(0, 5, 10)
    y = x ** 2
    fig, ax = plt.subplots(1,1)
    ax.plot(x,x**2,x,exp(x))
    ax.set_title("scientific notation")
    ax.set_yticks([0,50,100,150])
    from matplotlib import ticker
    formatter = ticker.ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((-1,1))
    ax.yaxis.set_major_formatter(formatter)
    plt.show()

#饼状图
def mat6():
    labels = 'frogs','hogs','dogs','cats'
    sizes = 10,20,30,40
    colors = 'yellow','gold','red','blue'
    explode = 0,0.1,0,0.7
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
    plt.axis('equal')
    plt.show()

def mat7():
    fig = plt.figure()
    ax1 = plt.subplot2grid((3,3),(0,0),colspan=3)
    ax2 = plt.subplot2grid((3,3),(1,0),colspan=2)
    ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)
    ax4 = plt.subplot2grid((3,3),(2,0))
    ax5 = plt.subplot2grid((3,3),(2,1))
    fig.tight_layout()
    plt.show()

if __name__ == '__main__':
    #mat1()
    #mat2()
    #mat3()
    mat4()
    #mat5()
    #mat6()
    #mat7()