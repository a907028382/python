# -*- coding:utf-8 -*-
#Time:2020/3/9 14:33
#Author:Fan
from pyecharts.charts import Graph,Page

def graph() -> Graph:
    nodes = [
        {"name":"cus1","symbolSize":10},
        {"name":"cus2","symbolSize":30},
        {"name":"cus3","symbolSize":20}
    ]
    links = []
    for i in nodes:
        if i.get('name') == 'cus1':
            continue
        for j in nodes:
            if j.get('name') == 'cus1':
                continue
                links.append()