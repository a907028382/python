# -*- coding: utf-8 -*-
# @Time : 2020/5/20 11:35
# @Author : Fan
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(0, 10, 100)
y = 1+ np.random.randint(0,10,size=(100,1))*0.1
print(y)

fig, ax = plt.subplots()
line, = ax.plot(x, y, color='k')
line2, = ax.plot(x, y-0.1, color='k')


print(type(line))

def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    line.axes.axis([0, 10, 0, 2])
    line2.set_data(x[:num], (y-0.1)[:num])
    line2.axes.axis([0, 10, 0, 2])
    return line,line2  # 可以同时画两个或多个线，只要在update函数中返回多个线即可


ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line],
                              interval=25, blit=True)
ani.save('test.gif',writer='pillow')
plt.show()

