# -*- coding:utf-8 -*-
#Time:2020/3/5 11:17
#Author:Fan
from pyecharts.charts import Calendar
import datetime
import random
from pyecharts import options as opts

def calendar() -> Calendar:
    begin = datetime.date(2020,1,1)
    end = datetime.date(2020,3,3)
    data = [[str(begin + datetime.timedelta(days=i)),random.randint(1000,
            20000)] for i in range(0,(end - begin).days + 1,2)]#隔天统计

    calendaa = (Calendar(init_opts = opts.InitOpts(width="1200px")).add(
        "",data,calendar_opts = opts.CalendarOpts(range_='2020')).set_global_opts(
        title_opts = opts.TitleOpts(title="日历数2020"),
        visualmap_opts = opts.VisualMapOpts(
            max_ = 20000,
            min_ = 1000,
            orient = "horizontal",
            is_piecewise = True,
            pos_top = "230px",
            pos_left = "100px",
        ),
    ))
    return calendaa

calendar().render('./result/calendar.html')
