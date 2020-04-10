from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType


items = ['陶永新', '汪峰', '颜子皓', '杨阳', '尚宇驰', '倪涛涛', '田震', '王庆媛', '王欢乐',
         '张浩杰', '刘恋', '韩源', '赵肖龙', '秦键', '孙文龙', '位哲武', '陈宇航', '杨晶', '曾传志',
         '郑亮', '岳凡', '陈蓉琪', '候粤嘉', '袁腾飞', '赵玉杰', '曹暝桕', '郭瑞昌', '黄敬理', '苏玉溪'
         '吴家浩', '丁怡凡', '谢晓茜', '黄启佳', '许源', '郁杰原', '王林', '席光平', '杨苏祥', '唐小梁'
         '王登科', '管讲宇']
data_list1 = [2085, 2069, 2062, 2036, 2028, 2024, 2022, 2013, 2012,
              2010, 2000, 1992, 1992, 1985, 1984, 1984, 1973, 1966, 1964,
              1964, 1962, 1961, 1960, 1957, 1955, 1947, 1945, 1940, 1933,
              1930, 1930, 1930, 1924, 1889, 1887, 1846, 1845, 1841, 1739,
              1712, 1699]
bar1 = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
    .add_xaxis(items)
    .add_yaxis('后端经验值', data_list1)
    .set_global_opts(title_opts=opts.TitleOpts(title='1851后端经验值排行'))
)
bar1.render(path='./res/后端经验值排行.html')
