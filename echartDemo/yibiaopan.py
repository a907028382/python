# -*- coding:utf-8 -*-
#Time:2020/3/5 10:45
#Author:Fan
from pyecharts import charts
#获取仪表盘
gauge = charts.Gauge()
gauge.add("这是一个仪表盘",[("机器学习",100)])
gauge.render(path="./result/gauge.html")
print('1')