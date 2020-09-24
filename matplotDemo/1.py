# -*- coding:utf-8 -*-
#Time:2019/5/18 14:36
#Author:Fan
import numpy as np
from matplotlib import pyplot
from scipy.interpolate import interp1d

x = np.linspace(0,10*np.pi,num=20)

#三角函数
y = np.sin(x)
yn = np.cos(x)

#线性插值
f1 = interp1d(x,y,kind="linear")
#三次样条插值
f2 = interp1d(x,y,kind='cubic')
pred = np.linspace(0,10*np.pi,num=1000)
print(pred)
y1 = f1(pred)
y2 = f2(pred)
pyplot.figure(1)
pyplot.plot(pred,y1,'r',label ='linear')
pyplot.plot(pred,y2,'b-',label='cubic')
#显示图例
pyplot.legend()
pyplot.figure(2)
pyplot.plot(x,yn,label='new')
pyplot.legend()
pyplot.show()
