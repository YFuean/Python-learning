'''
日历图
'''
import datetime
import random
from pyecharts import options as opts
from pyecharts.charts import Calendar


def calendar_draw() -> Calendar:
    begin = datetime.date(2019, 1, 1)
    end = datetime.date(2019, 12, 31)
    data = [[str(begin + datetime.timedelta(days=i)), random.randint(3600, 57600)]
            for i in range(0, (end-begin).days+1)
            ]
    calendar = (Calendar(init_opts=opts.InitOpts(width="1200px"))
                .add("", data, calendar_opts=opts.CalendarOpts(range_="2019"))
                .set_global_opts(title_opts=opts.TitleOpts(title="Calendar-2019 每天使用手机时长统计/单位：秒"),
                                 visualmap_opts=opts.VisualMapOpts(
                                     max_=57600, min_=3600, orient="horizontal", is_piecewise=True, pos_top="230px", pos_left="100px", ),
                                 )
                )
    return calendar


calendar_draw().render('./res/html/calendar.html')
