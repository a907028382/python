# -*- coding:utf-8 -*-
#Time:2020/3/5 10:57
#Author:Fan

from pyecharts.charts import Funnel
from random import randint
from pyecharts import options as opts

c = (Funnel().add("标题",[list(a) for a in zip(["一行","两行","三行"],
                                             [randint(1,20) for i in range(3)]
                                             )]).set_global_opts(title_opts = opts.TitleOpts(title="漏斗")))

c.render('./result/funnel.html')